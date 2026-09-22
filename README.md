# Academic Student Assistant Agent - AI Agents Workshop (Day 5)

An AI-powered academic student assistant built with **LangChain** and **Google Gemini LLM**. The agent uses tool calling to interact with an **SQLite database**, calculate student marks, and determine passing eligibility according to university rules.

---

## 🌟 Overview

The Academic Student Assistant Agent is designed to answer academic queries about student records autonomously. Given a query or student ID, the agent determines which tools to invoke—fetching student details or subject marks, performing math calculations, and checking university passing criteria—to provide a clear and structured answer.

---

## 🚀 Features & Agent Tools

The agent leverages custom LangChain `@tool` definitions:

* **`get_student_info(student_id)`**: Fetches student name and department from the database.
* **`get_student_marks(student_id)`**: Retrieves subject scores in *Python*, *Database*, *AI*, and *Web*.
* **`calculator(expression)`**: Evaluates arithmetic expressions to compute total marks and average percentages.
* **`get_passing_rules()`**: Retrieves university grading guidelines:
  * Minimum mark per subject: **35%**
  * Minimum overall average: **40%**

---

## 📁 Project Structure

```text
Day 5/
├── init_db.py        # Python script to initialize and populate the SQLite database (students.db)
├── notebook.ipynb     # Jupyter notebook implementing the LangChain agent and interactive prompts
├── .gitignore        # Git ignore rules for python virtual environment and local database
└── README.md         # Project documentation
```

---

## 🛠️ Prerequisites & Setup

### 1. Requirements
* Python 3.10+
* Google Gemini API key

### 2. Environment Setup

Clone the repository and set up a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate
```

Install required packages:

```bash
pip install langchain langchain-community langchain-google-genai
```

### 3. Initialize the Database

Run `init_db.py` to create `students.db` with sample student records:

```bash
python init_db.py
```

---

## 💡 Usage

1. Open `notebook.ipynb` in VS Code or Jupyter Notebook.
2. Set your Google Gemini API key in the notebook:
   ```python
   import os
   os.environ["GEMINI_API_KEY"] = "your-api-key-here"
   ```
3. Execute the cells to initialize the agent and interactively run queries.

### Example Query & Response

**Query:**
> *"Check if student 22CS045 passed."*

**Output:**
```text
************************************************************
 STUDENT ACADEMIC AGENT ANSWER
- Name: Dhanushya
- Department: Computer Science
- Total Marks: 325
- Average Marks: 81.25%
- Passing Status: Yes, you satisfy the university passing requirements (all subject marks are >= 35% and the overall average is >= 40%).
************************************************************
```

---

## 📊 Sample Student Data

| Student ID | Name | Department | Python | Database | AI | Web |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| `22CS045` | Dhanushya | Computer Science | 85 | 72 | 90 | 78 |
| `22CS046` | Rahul | Computer Science | 65 | 70 | 68 | 72 |
| `22CS047` | Priya | Information Technology | 92 | 88 | 95 | 90 |
| `22CS048` | Arun | Information Technology | 55 | 60 | 58 | 62 |
| `22CS049` | Meena | Computer Science | 78 | 85 | 80 | 88 |
