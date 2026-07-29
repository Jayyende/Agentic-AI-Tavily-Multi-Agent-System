# 🤖 Multi-Agent AI System using Tavily Search API

A Python-based Multi-Agent AI System developed as part of the **Agentic AI & Automation (Flexi Credit) CA-I**. The project demonstrates how multiple specialist AI agents collaborate to solve a user's query by planning, searching, analyzing, and generating a structured report.

---

## 📖 Project Overview

This project implements an Agentic AI workflow using four specialist agents:

- 📝 Planner Agent
- 🔍 Search Agent
- 📊 Fundamentals Analyst Agent
- ✍️ Writer Agent

The Search Agent uses the **Tavily Search API** to retrieve real-time information from the internet. The retrieved content is analyzed and organized into a well-structured report by the remaining agents.

---

## 🚀 Features

- Multi-Agent AI Architecture
- Planner Agent for task planning
- Search Agent with Tavily Search API
- Fundamentals Analyst Agent for content analysis
- Writer Agent for report generation
- Modular Python implementation
- Secure API key management using `.env`

---

## 🏗️ System Architecture

```
User
   │
   ▼
main.py (Workflow Controller)
   │
   ▼
Planner Agent
   │
   ▼
Search Agent
   │
   ▼
Tavily Search API
   │
   ▼
Fundamentals Analyst Agent
   │
   ▼
Writer Agent
   │
   ▼
Generated Report
```

---

## 📂 Project Structure

```
Multi-Agent-AI-System/
│
├── main.py
├── planner.py
├── search_agent.py
├── analyst.py
├── writer.py
├── requirements.txt
├── .env.example
├── README.md
└── screenshots/
```

---

## 🛠️ Technologies Used

- Python 3.x
- Tavily Search API
- python-dotenv
- Tavily Python SDK

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Multi-Agent-AI-System.git
```

### 2. Open the Project

```bash
cd Multi-Agent-AI-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

```env
TAVILY_API_KEY=your_api_key_here
```

### 5. Run the Project

```bash
python main.py
```

---

## 📸 Output

The system performs the following tasks:

- Accepts a user query
- Generates an execution plan
- Retrieves real-time information using Tavily Search API
- Analyzes the retrieved information
- Generates a structured report

---

## 📁 Screenshots

Add your screenshots inside the **screenshots** folder.

Example:

```
screenshots/
├── architecture.png
├── output.png
├── terminal.png
```

---

## 🎯 Learning Outcomes

- Understanding Agentic AI concepts
- Implementing a Multi-Agent System
- Integrating external APIs
- Designing modular Python applications
- Coordinating multiple AI agents

---

## 🔮 Future Enhancements

- Web-based user interface
- Additional specialist agents
- PDF report generation
- LLM integration
- Memory-enabled agent workflow
- Database support

---

## 👨‍💻 Author

**Jay Yende**

B.Tech – Artificial Intelligence & Data Science

Flexi Credit Course – Agentic AI & Automation

---

## 📄 License

This project is developed for educational and academic purposes only.
