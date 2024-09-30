import pathway as pw
from dotenv import load_dotenv
import logging
from argparse import ArgumentParser
import yaml 

from pathway.xpacks.llm import embedders, llms, parsers, splitters
from pathway.udfs import DiskCache, ExponentialBackoffRetryStrategy
from pathway.xpacks.llm.vector_store import VectorStoreServer
from pathway.xpacks.llm.question_answering import BaseRAGQuestionAnswerer

# Using Pathway's Demo Licence Key
pw.set_license_key("demo-license-key-with-telemetry")

# Loading env variables
load_dotenv()

# Setting message log format
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Accessing Data Sources into the LLM Model
def data_source(source_configs):
    data = []
    for source_config in source_configs:
        data_file = pw.io.fs.read(**source_config["config"], format="binary", with_metadata=True)
        data.append(data_file)
    return data

def run():
    parser = ArgumentParser(description="Run the RAG server with a specified configuration file.")
    parser.add_argument("--config_file", default="config.yaml", help="Config file to be used.")
    
    # Parse the command-line arguments
    args = parser.parse_args()  

    # Loading the YAML configuration
    with open(args.config_file, 'r') as config_f:
        configuration = yaml.safe_load(config_f)
    
    # Setting up Model
    LLM_MODEL = configuration["llm_config"]["model"]
    embedding_model = "avsolatorio/GIST-small-Embedding-v0"
    embedder = embedders.SentenceTransformerEmbedder( embedding_model, call_kwargs={"show_progress_bar": False})
    chat = llms.LiteLLMChat(model=LLM_MODEL, retry_strategy=ExponentialBackoffRetryStrategy(max_retries=6), cache_strategy=DiskCache())

    # Setting Host and Port
    host_config = configuration["host_config"]
    host, port = host_config["host"], host_config["port"]

    # Creating VectorDB
    doc_store = VectorStoreServer(*data_source(configuration["sources"]), embedder=embedder, splitter=splitters.TokenCountSplitter(max_tokens=400), parser=parsers.ParseUnstructured())

    # Creating and Running RAG App
    rag_app = BaseRAGQuestionAnswerer(llm=chat, indexer=doc_store)
    rag_app.build_server(host=host, port=port)
    rag_app.run_server(with_cache=True, terminate_on_error=False)

if __name__ == "__main__":
    run()