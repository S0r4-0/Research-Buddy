<div align="center">

# 🚀 **Research Buddy** 🚀  
Stay ahead of the curve with real-time, AI-driven research insights!

</div>

---

## 🔍 **Project Overview**

Pathway's **LLM (Large Language Model) Apps** allow you to seamlessly integrate cutting-edge **Retrieval-Augmented Generation (RAG)** capabilities into your workflow, offering:

- **High-accuracy retrieval** with the **latest knowledge** from your data sources
- **Real-time syncing** with diverse data sources like **file systems, Google Drive, SharePoint, S3, Kafka, PostgreSQL,** and more!
- Fully in-memory **vector, hybrid, and full-text search**
- Hassle-free deployment with **no additional infrastructure setup required**

### 🎯 **Goal:**
The objective of this project is to deliver an LLM-powered RAG tool that helps researchers, students, and professionals stay up-to-date by retrieving the **latest research papers from arXiv**, while providing **real-time answers** to user queries. This streamlines the process of staying informed without feeling overwhelmed by the flood of new research.

---

## 🛠️ **Project Highlights**

### 🚀 **Real-Time Knowledge Retrieval**
Our LLM-powered system fetches the latest research papers, effortlessly keeping you in the loop with advancements in your chosen field.


### ⚡ **Automated Real-Time Knowledge Mining**
Automatically mine new research papers and get real-time alerts when significant data changes are detected.

---

## 🧰 **Key Features**

- **In-Memory Vector Search**: Instantly retrieve research papers and data from multiple sources.
- **Data Syncing**: Automatically keeps your data updated (new papers, updates, or deletions).
- **Scalability**: Supports **large-scale data retrieval and indexing**, making it suitable for both individual researchers and large organizations.

![alt text](<data-retrieval/images/preview.png>)
---


## Demo Link
 [Linkedin and Video Link](https://www.linkedin.com/posts/vedant-airon-1592b1289_llm-ai-dataprocessing-activity-7246561374359691264-uWUz?utm_source=share&utm_medium=member_android)

## 🚀 **Getting Started**

### 🔧 **Pre-requisites**
- Python 3
- Docker or WSL (for Windows users)

## Installation And Usage

- Linux/Mac

Clone the repo

```bash
  git clone https://github.com/S0r4-0/Research-Buddy.git
```

Download requirements.txt

```bash
  cd /data-retrieval
```

- Linux
  
  ```bash
    sudo apt-get update 
  ```

- Mac
  
  ```bash
    sudo brew update
  ```

```bash
  python3 -m venv .venv
  pip install -r requirements.txt
```

Get [Gemini API key](https://aistudio.google.com/app/apikey) and put it into .env file.(change .env.sample to .env)

Run streamlit server.

```bash
  streamlit run stm.py
```

- Windows
  
Pathway is currently not available on Windows.

* **Alternatives**  
  * Run on WSL/VM and follow Linux method
  * Run through Docker 

- Through Docker

Clone the repo

```bash
  git clone https://github.com/S0r4-0/Research-Buddy.git
  cd data-retrieval
```

Get [Gemini API key](https://aistudio.google.com/app/apikey) and put it into .env file.(change .env.sample to .env)

Build docker image

```bash
  docker build -t <image-name> .
```

Run docker image

- Windows
  
  ```bash
    docker run -v "${PWD}/data:/app/data" -p 8501:8501 <image-name>
  ```

- Linux

  ```bash
    docker run -v "$(pwd)/data:/app/data" -p 8501:8501  <image-name>
  ```

## 🤝 **Contributing**

We welcome contributions! Please feel free to fork the repository and submit pull requests.

---

## 📄 **License**

This project is licensed under the [MIT License](LICENSE).

<br><br>
<div align="center">
Thank you for using Research Buddy! Together, let's stay informed and innovate.

</div>