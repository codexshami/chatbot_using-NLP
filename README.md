# 🤖 AI Chatbot Using NLP

# A simple rule-based AI chatbot built using Natural Language Processing (NLP) techniques with NLTK.
# It can handle greetings, internship-related queries, Python-related questions, and more.

# ---------------------------
# 📌 Project Objective
# ---------------------------
# Task-3:
# Build a chatbot using NLP libraries like NLTK or spaCy, capable of understanding and responding to user queries.

# ---------------------------
# 🧠 Features
# ---------------------------
# ✔️ Handles greetings and general conversations
# ✔️ Answers internship-related queries
# ✔️ Responds to Python and basic tech questions
# ✔️ Uses NLP techniques:
#    - Tokenization
#    - Lemmatization
#    - Intent Matching
# ✔️ Simple command-line interface
# ✔️ Easily extendable

# ---------------------------
# 🛠 Requirements
# ---------------------------
pip install nltk

python - <<EOF
import nltk
nltk.download('punkt')
nltk.download('wordnet')
EOF

# ---------------------------
# 🚀 How to Run
# ---------------------------
# 1. Clone or download this repository
# 2. Navigate to project folder
# 3. Run:
python chatbot_nlp.py

# ---------------------------
# 🧪 Sample Conversation
# ---------------------------
# 🤖 CODTECH Chatbot with NLP (type 'exit' to quit)
# You: hi
# Bot: Hello!
#
# You: what is python?
# Bot: Python is a powerful, high-level programming language used in AI, data science, and more.
#
# You: when will i get my certificate?
# Bot: You will receive your certificate on your internship end date.
#
# You: bye
# Bot: Goodbye!

# ---------------------------
# 🧾 Internship Info Supported
# ---------------------------
# - When will I get my certificate?
# - What is CODTECH?
# - Who created you?

# ---------------------------
# 📦 File Structure
# ---------------------------
# chatbot_project/
# ├── chatbot_nlp.py
# ├── requirements.txt
# └── README.md

# ---------------------------
# 🔧 Future Improvements
# ---------------------------
# - Add GUI (Tkinter / Streamlit)
# - Add ML-based intent classification
# - API integration
# - Deploy as web chatbot


