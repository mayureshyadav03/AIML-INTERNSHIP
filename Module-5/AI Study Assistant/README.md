# 🎓 AI Study Assistant

## 📌 Project Overview

AI Study Assistant is an AI-powered educational application built using Python, Streamlit, and Google's Gemini API. The application helps students understand technical topics by generating simple explanations, key points, real-world applications, important terms, practice questions, and study tips.

The project was developed as part of **Module 5 — AI Tools & Mini Project** of my AI/ML internship.

## ✨ Features

* Enter any topic you want to learn.
* Generate an easy-to-understand explanation.
* Get important key points.
* Explore real-world applications.
* Learn important terminology.
* Generate five practice questions.
* Receive personalized study tips.
* Simple and interactive Streamlit interface.
* Uses Google's Gemini API for AI-generated content.

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google GenAI Python SDK

## ⚙️ Project Structure

```text
AI Study Assistant/
│
├── .streamlit/
│   └── secrets.toml
│
├── screenshots/
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

## 🔐 API Key Setup

The application requires a Gemini API key.

Create a `.streamlit` folder and add a `secrets.toml` file:

```toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

The API key is kept outside the source code and is excluded from GitHub using `.gitignore`.

**Never share or publicly upload your API key.**

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd "AI-ML-Internship/Module-5/AI Study Assistant"
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Add your Gemini API key

Create:

```text
.streamlit/secrets.toml
```

and add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

```text
User enters a topic
        ↓
Streamlit receives the input
        ↓
Prompt is created
        ↓
Gemini API processes the prompt
        ↓
AI generates study material
        ↓
Streamlit displays the result
```

## 📚 Example

A user can enter:

```text
Machine Learning
```

The application generates:

1. Simple Explanation
2. Key Points
3. Real-World Applications
4. Important Terms
5. Five Practice Questions
6. Study Tips

## 🤖 AI Tools Explored

As part of Module 5, I explored multiple AI tools including:

### ChatGPT

Used for:

* Coding assistance
* Code explanation
* Debugging
* Research assistance
* Brainstorming
* Productivity

### Google Gemini

Used for:

* Coding assistance
* Research
* Content generation
* AI application development

### Microsoft Copilot

Explored for:

* Coding assistance
* Productivity
* Information assistance

## 💻 AI-Assisted Development

AI tools were used during the development process to:

* Generate programming ideas
* Understand Python concepts
* Explain code
* Identify and debug errors
* Improve development workflow
* Brainstorm project functionality
* Assist with documentation

AI-generated output was reviewed, tested, and modified rather than being blindly copied.

## 🔍 Learning Outcomes

Through this project, I learned:

* How AI tools can assist software development.
* How to use AI for coding and debugging.
* How AI can support research and learning.
* How to integrate an AI API into a Python application.
* How to build an interactive application using Streamlit.
* How to securely manage API keys.
* How to document and organize an AI project.
* The importance of testing and verifying AI-generated output.

## 🔮 Future Improvements

Possible future improvements include:

* User login and personalized learning profiles.
* Saving previous study sessions.
* Difficulty-level selection.
* Automatic quizzes and scoring.
* Multiple AI model support.
* Voice-based interaction.
* PDF/document-based study assistance.
* Progress tracking and analytics.

## 👨‍💻 Author

**Mayuresh Yadav**

BTech — Artificial Intelligence & Machine Learning

This project was developed as part of my AI/ML internship training.

## 📄 License

This project is created for educational and internship purposes.
