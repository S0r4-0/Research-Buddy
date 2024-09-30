import streamlit as st
import requests
import arxiv
import os
import xml.etree.ElementTree as ET
import json
import subprocess

# Function to search arXiv by title
def search_arxiv_by_title(title):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"title:{title}",
        "max_results": 1
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
                if link.attrib.get('rel') == 'related':
                    return link.attrib['href']
        return None
    else:
        st.write(f"Error fetching data from arXiv: {response.status_code}")
        return None

# Function to download PDF
def download_pdf(pdf_url, filename):
    if not os.path.exists("data"):
        os.makedirs("data")

    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(f"data/{filename}", 'wb') as f:
            f.write(response.content)
        st.write(f"Downloaded: {filename}")
    else:
        st.write(f"Error downloading PDF: {response.status_code}")

# Function to fetch papers from arXiv by query
def fetchpaper(q):
    client = arxiv.Client()
    search = arxiv.Search(
        query=q,
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = client.results(search)
    all_results = list(results)
    return all_results

def ask_question(question):
    question_url = "http://0.0.0.0:8000/v1/pw_ai_answer"  # Connect to RAG server on port 6060
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json",
    }
    data_prompt = {
        "prompt": question
    }
    r = requests.post(question_url,headers=headers, data=json.dumps(data_prompt))
    answer = r.text
    return answer


def topic_search():
    # Search by domain
    st.write("Enter the topic you want to research:")
    search_query1 = st.text_input("Enter topic", "")

    if search_query1:
        st.write(f"Searching for research papers in: {search_query1}...")
        results = fetchpaper(search_query1)
        st.write("\n\n".join([r.title for r in results]))


    else:
        st.write("Please enter a topic to search.")

def research_paper_search():
    # Search by title
    st.write("Enter the title of the research paper you want to download:")
    search_query = st.text_input("Enter research paper title", "")

    if search_query:
        st.write(f"Searching for research papers with title: {search_query}...")
        pdf_url = search_arxiv_by_title(search_query)

        if pdf_url:
            download_pdf(pdf_url, f"{search_query}.pdf")
        else:
            st.write("PDF not found for the given title.")
    else:
        st.write("Please enter a title to search.")

def question_search():
    search_query = st.text_input("Enter a Question", "")

    if search_query:
        st.write(f"Searching in research papers for question : {search_query}...")
        answer = ask_question(search_query)

        st.write(answer)
    else:
        st.write("Please enter a title to search.")

def run_server():
    # Streamlit UI
    st.title("Research Buddy")

    topic_search()

    research_paper_search()

    question_search()

if __name__ == "__main__":
    process = subprocess.Popen(["python3", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_server()