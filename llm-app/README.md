# LLM App

A lightweight application built with Streamlit and Python.  
Follow the steps below to set up and run the project locally.


## ⚠️ Warning

**Important:** This App required Python 3.12.

---

## 🚀 Getting Started

### 1. Create the Virtual Environment (with all dependencies)

This installs all packages listed in `pyproject.toml` and generates `.venv`:

```bash
uv sync
```

### 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Run the Application

```bash
python -m streamlit run app.py
```

### Your Streamlit app will start and can be accessed in the browser at:

http://localhost:8501

📁 Project Structure

├── app.py
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md

🛠 Requirements

    Python 3.12+

    uv package manager

    Streamlit

    LangChain

    OpenAI

📦 Installing / Updating Dependencies

To add a new dependency:

```bash
uv add <package-name>
uv sync
```

🧪 Running Without Activating the Virtual Environment

```bash
uv run streamlit run app.py
```
