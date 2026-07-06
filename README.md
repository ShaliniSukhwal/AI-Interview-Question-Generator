# 🤖 AI Interview Question Generator

An AI-powered Interview Question Generator built using **Python**, **FastAPI**, and **Google Gemini AI**.

## 🚀 Features

- Generate AI-powered interview questions
- Role-based interview preparation
- Experience-based question generation
- Difficulty selection (Easy, Intermediate, Hard)
- Technical or HR interview questions
- FastAPI REST API
- Interactive Swagger Documentation

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Google Gemini API
- Pydantic
- Python Dotenv
- Uvicorn

---

## 📁 Project Structure

```
AI-Interview-Question-Generator
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ▶️ Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📮 API Endpoint

### POST `/generate`

Sample Request

```json
{
  "role": "UI UX Designer",
  "company": "Google",
  "experience": "5 Years",
  "difficulty": "Intermediate",
  "question_count": 10,
  "question_type": "Technical"
}
```

---

## 📌 Future Improvements

- AI Answer Evaluation
- Save Interview History
- User Authentication
- Database Integration
- Company-specific Interview Modes

---

## 👩‍💻 Author

**Shalini Sukhwal**