# https-github.com-Anjalichary12-Software-Engineer-Intern-Assignment-2-Zeotap

```markdown
# Support Agent Chatbot for Customer Data Platforms (CDP)

## 📌 Overview
The Support Agent Chatbot is a conversational AI system that assists users with "how-to" questions related to four major Customer Data Platforms (CDPs):  
Segment, mParticle, Lytics, and Zeotap.  
It retrieves relevant information from official documentation to guide users in performing tasks efficiently.

## 🎯 Objective
- Answer "how-to" queries for Segment, mParticle, Lytics, and Zeotap.
- Extract and retrieve relevant steps from official documentation.
- Handle variations in question phrasing.
- Implement advanced features like **cross-CDP comparisons** and **complex "how-to" queries**.

## 🛠️ Tech Stack
- Backend: Python, Flask
- NLP Processing: OpenAI GPT or Document Indexing
- Frontend: HTML, CSS, JavaScript
- Deployment: Gunicorn
---

## ✨ Features
### ✅ 1. Answer "How-to" Questions.
- Responds to user queries such as:
  - "How do I set up a new source in Segment?"
  - "How can I create a user profile in mParticle?"
  - "How do I build an audience segment in Lytics?"
  - "How can I integrate my data with Zeotap?"

### 🔍2.  Extract Information from Documentation
- Retrieves and summarizes relevant sections.
- Provides step-by-step instructions.

### 🤖 3. Handle Variations in Questions
- Supports different query formats.
- Ignores irrelevant queries (e.g., "Which movie is releasing this week?").

### 🚀 Bonus Features
- Cross-CDP Comparisons
  - Example: "How does Segment's audience creation compare to Lytics'?"
- Advanced Queries
  - Guides on complex configurations, integrations, and best practices.

---

## ⚡ Installation & Setup
### 🔹 1. Clone the Repository
```sh
git clone https://github.com/your-repo/support-agent-chatbot.git
cd support-agent-chatbot
```

### 🔹 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 🔹 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 4. Run the Flask App
```sh
python app.py
```
or
```sh
flask run
```
App runs at http://127.0.0.1:5000

---


## 🚀 Deployment
```sh
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

---

## 🎯 Usage
1. Open http://127.0.0.1:5000 in a browser.
2. Enter a "how-to" question related to CDPs.
3. The chatbot retrieves and returns the relevant steps.

---

## 🛠️ Troubleshooting
### 🔹 Common Issues & Fixes
#### ❌ Flask App Not Running
```sh
python -m flask run --host=0.0.0.0 --port=5000
```
#### ❌ Port Already in Use
```sh
kill -9 $(lsof -t -i:5000)  # Mac/Linux
taskkill /F /IM python.exe   # Windows
```
#### ❌ Virtual Environment Issues
```sh
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

## 📌 Future Enhancements
- Implement user authentication for personalized responses.
- Enhance NLP capabilities for better query understanding.
- Build a React-based frontend for improved UX.

---


