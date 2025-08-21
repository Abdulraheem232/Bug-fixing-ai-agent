

---

# 🐞 AI Bug Fixing Agent

This project is an **AI-powered bug fixing agent** built with **LangGraph**, **LangChain**, and **Grok models**.
It uses a combination of **LLM reasoning** and **Stack Overflow knowledge retrieval** to help identify and fix bugs in code.

---

## 🚀 Features

* Accepts your code or error description as input.
* Uses **Grok LLMs** (`grok-3`, `grok-4`, or `grok-4-heavy`) for reasoning.
* Fetches related **Stack Overflow questions** and extracts solutions.
* Displays both **bug analysis** and **possible fixes** directly in the UI.
* Streamlit-based interface for easy interaction.

---

## 🧩 Tools Integrated

1. **`fetch_data_from_stackoverflow`** → Searches Stack Overflow for relevant links.
2. **`get_data_from_stackoverflow`** → Scrapes useful solutions from those links.
3. **AI Reasoning Agent** → Reads the context, analyzes the bug, and suggests a fix.

---

## 💻 Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies (manually since no `requirements.txt` yet):

   ```bash
   pip install streamlit requests beautifulsoup4 langchain langgraph langchain_groq
   ```
3. Get your **Grok API key** from the [xAI Grok Console](https://console.groq.com).
4. Replace the placeholder key in your code:

   ```python
   llm = ChatGroq(
       model="grok-4",
       temperature=0.2,
       api_key="your_grok_api_key_here"
   )
   ```
5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 📌 Example

* Input:

  ```
  I'm getting ZeroDivisionError when dividing two numbers in Python.
  ```
* Agent response:

  * Shows Stack Overflow references.
  * Suggests checking the denominator before dividing.
  * Provides a fixed code snippet.

---

## ⚡ Notes

* Best model for bug fixing: **`grok-4`**.
* Use **low temperature (0.0 – 0.3)** for deterministic debugging.
* If the agent cannot fix a bug, it will return references to helpful discussions.

---

## 🔗 Resources

* [xAI Grok Console](https://console.groq.com) – Get your API key.
* [LangChain Docs](https://python.langchain.com/)
* [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
* [Stack Exchange API](https://api.stackexchange.com/)

---


