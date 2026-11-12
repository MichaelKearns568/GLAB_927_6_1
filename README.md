# GLAB 927.6.1: Mastering LangChain for Advanced Language Model Applications

## Project Overview

This project explores LangChain, a framework designed for advanced prompt management and orchestration with Large Language Models (LLMs). Using `langchain` and `langchain-groq` (powered by the `llama3-8b-8192` model), these techniques are applied to real-world customer support workflows—ranging from automating frequently asked questions (FAQs) to building multi-step sequential prompt chains for query extraction, order retrieval, and response generation. Environment setup and dependency management are handled using modern `uv` workflows (or standard `pip` environments).

## Key Concepts

* **Prompt Templates (`PromptTemplate`):** Parameterized text structures with defined `input_variables` that dynamically inject user queries or intermediate outputs into structured instructions for an LLM.
* **LLM Chains (`LLMChain`):** Modular workflow components that link a prompt template directly to a language model (`ChatGroq`), allowing sequential execution where the output of one stage feeds into the next.
* **Prompt Engineering & Optimization:** Refining prompt context, constraints, and data-source instructions across multi-stage pipelines to improve response accuracy, reliability, and efficiency.

## Project Structure

```text
GLAB_927_6_1/ ├── .gitignore ├── .python-version ├── pyproject.toml ├── uv.lock ├── README.md └── src/
└── glab_927_6_1/ ├── __init__.py └── langchain_workflows.py
```

## Setup and Execution Instructions

1. **Configure your Groq API Key:**
   Create an account on [GroqCloud](https://console.groq.com), generate an API key, and set it as an environment variable:
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

2. **Initialize and sync the project dependencies using `uv`:**
   ```bash
   uv sync
   uv run python src/glab_927_6_1/langchain_workflows.py
   ```

3. **Alternative installation via `pip` (if running outside of `uv`):**
   ```bash
   pip install langchain
   pip install -U langchain-groq
   python src/glab_927_6_1/langchain_workflows.py
   ```

## Summary of Findings & Learnings

* **Groq & LangChain Integration:** Configured `ChatGroq` (`llama3-8b-8192`) with system and human role messages to automate accurate responses to common customer support FAQs.
* **Multi-Stage Sequential Chains:** Built a three-step `LLMChain` pipeline that extracts key details from an incoming customer inquiry, simulates retrieving relevant order records, and synthesizes a tailored customer response.
* **Workflow Optimization & Evaluation:** Evaluated multi-step chain outputs across diverse test queries and refined prompt templates with clearer context and grounding instructions to boost overall system accuracy.