import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')

# ============================================
# MASSIVELY EXPANDED CHATBOT PAIRS
# ============================================

pairs = [
    # ========== GREETINGS & FAREWELLS ==========
    ["hi|hello|hey|hola|namaste|greetings", 
     ["Hello! 👋", "Hi there! 😊", "Hey! How can I help you today?", "Greetings! What brings you here?"]],
    
    ["good morning|morning|gm", 
     ["Good morning! ☀️ Ready to assist you.", "Morning! Hope you have a great day ahead.", "Rise and shine! How can I help?"]],
    
    ["good afternoon|afternoon|ga", 
     ["Good afternoon! 🌤️ How's your day going?", "Afternoon! Need any help with coding or internships?"]],
    
    ["good evening|evening|ge", 
     ["Good evening! 🌙 Ready to assist.", "Evening! Still productive I see. How can I help?"]],
    
    ["good night|night|gn", 
     ["Good night! 🌟 Sleep well and code tomorrow!", "Night night! See you tomorrow."]],
    
    ["how are you|how are you doing|how's it going|what's up|sup", 
     ["I'm doing fantastic, thanks for asking! 😊", "All systems operational and ready to chat!", "Doing great! How about you?", "I'm just code, but I feel wonderful today!"]],
    
    ["what's up|sup|wassup", 
     ["Not much, just waiting to help you! 😎", "The sky's up! But seriously, how can I assist?"]],
    
    # ========== EXIT & GOODBYE ==========
    ["bye|goodbye|exit|quit|see you|take care|cya|farewell", 
     ["Goodbye! 👋 Come back anytime!", "See you later! Happy coding! 💻", "Farewell! Keep learning!", "Take care! Feel free to return with more questions."]],
    
    # ========== BOT IDENTITY & CREATOR ==========
    ["what is your name|who are you|your name|what should I call you", 
     ["I'm CODTECH Chatbot, your AI assistant! 🤖", "They call me your friendly coding companion.", "I'm CodeBuddy - here to help with Python and internships!"]],
    
    ["who created you|who made you|your creator|who built you", 
     ["I was created by a talented CODTECH intern using Python and NLTK! 🐍", "A smart developer at CODTECH built me during their internship.", "My creators are the awesome folks at CODTECH!"]],
    
    ["how old are you|your age", 
     ["I was born the moment you ran this code! 🎂", "Age is just a number for bots - I'm timeless!", "I'm as old as this Python script - brand new!"]],
    
    ["where do you live|your home", 
     ["I live in your computer's memory! 🖥️", "I'm everywhere Python runs!", "Right here in this terminal!"]],
    
    # ========== CODTECH INTERNSHIP INFO ==========
    ["what is codtech|tell me about codtech|codtech information", 
     ["CODTECH is an innovative internship and training company that helps students gain real-world experience! 🚀", 
      "CODTECH provides hands-on training in software development, AI, and data science.", 
      "A great place to learn, grow, and kickstart your tech career!"]],
    
    ["what is this internship about|codtech internship details|internship description", 
     ["This internship teaches you Python programming and real-world project building with industry standards.", 
      "You'll learn version control, debugging, documentation, and build actual applications!", 
      "It's a project-based program where you apply what you learn immediately."]],
    
    ["when will I get certificate|certificate timeline|internship certificate", 
     ["You will receive your certificate on your internship end date after successful completion! 📜", 
      "Certificate is issued within 7 days after finishing all required tasks.", 
      "Once you complete all projects, your certificate will be emailed to you."]],
    
    ["how long is internship|internship duration|duration", 
     ["The internship typically lasts 1-3 months depending on the program you chose.", 
      "Most internships are 4-8 weeks long with flexible hours.", 
      "You can complete it at your own pace within the given timeframe."]],
    
    ["is internship paid|paid internship|stipend", 
     ["Please check with CODTECH directly - some programs offer stipends based on performance.", 
      "It varies by program. Contact CODTECH support for exact details."]],
    
    ["requirements for internship|prerequisites|eligibility", 
     ["Basic programming knowledge helps, but enthusiasm to learn is the main requirement! 📚", 
      "You should know fundamentals of any programming language. Python is preferred.", 
      "Just bring your laptop and a learning attitude!"]],
    
    ["how to apply|codtech application|apply for internship", 
     ["Visit the CODTECH website and fill out the application form! 📝", 
      "Send your resume to internships@codtech.com or apply through their portal."]],
    
    ["codtech contact|contact codtech|codtech email", 
     ["You can reach CODTECH at: contact@codtech.com or call their support number from the website."]],
    
    # ========== PYTHON PROGRAMMING ==========
    ["what is python|python programming|tell me about python", 
     ["Python is a high-level, interpreted programming language known for its simplicity and readability! 🐍", 
      "Python is used in AI, data science, web development, automation, and more!", 
      "It's one of the most popular languages - great for beginners and experts alike."]],
    
    ["what is a variable|variables in python", 
     ["A variable is like a labeled box that stores data you can use and change in your program. 📦", 
      "Example: `name = 'John'` stores 'John' in the variable called 'name'.", 
      "Variables can hold numbers, text, lists, and even entire objects!"]],
    
    ["what is a list|python list|list in python", 
     ["A list is a collection of items in a particular order, written with square brackets. 📋", 
      "Example: `fruits = ['apple', 'banana', 'cherry']`", 
      "Lists can hold different data types and you can change, add, or remove items."]],
    
    ["what is a dictionary|dictionary in python|python dict", 
     ["A dictionary stores key-value pairs, perfect for structured data! 📖", 
      "Example: `person = {'name': 'Alice', 'age': 25}`", 
      "Access values with keys: `person['name']` returns 'Alice'."]],
    
    ["what is a tuple|tuple in python", 
     ["A tuple is like a list but IMMUTABLE (can't be changed after creation). 🔒", 
      "Example: `colors = ('red', 'green', 'blue')`", 
      "Use tuples for data that shouldn't change, like days of the week."]],
    
    ["what is a set|set in python", 
     ["A set is an unordered collection of UNIQUE elements. 🃏", 
      "Example: `numbers = {1, 2, 3, 4}`", 
      "Sets automatically remove duplicates - great for finding unique items!"]],
    
    ["what is a function|functions in python|how to create a function", 
     ["A function is reusable code that performs a specific task. 🛠️", 
      "Use `def function_name():` followed by indented code.", 
      "Example: `def greet(): print('Hello!')` then call it with `greet()`"]],
    
    ["what are parameters|arguments in python|function parameters", 
     ["Parameters are inputs you pass to functions to customize their behavior. 📥", 
      "Example: `def greet(name): print(f'Hello {name}')` - here 'name' is a parameter."]],
    
    ["what is return statement|return in python", 
     ["The 'return' statement sends a value back from a function to the caller. ↩️", 
      "Example: `def add(a,b): return a + b` then `result = add(5,3)` gives 8."]],
    
    ["what is an if statement|conditional statements|if else", 
     ["An if statement runs code ONLY when a condition is True. ⚖️", 
      "Example: `if age >= 18: print('Adult') else: print('Minor')`", 
      "You can chain with `elif` for multiple conditions."]],
    
    ["what is a loop|loops in python|for loop|while loop", 
     ["Loops repeat code multiple times! 🔄", 
      "For loop: `for i in range(5): print(i)` runs 5 times.", 
      "While loop: `while x < 10:` runs until condition becomes False."]],
    
    ["what is a class|classes in python|object oriented", 
     ["A class is a blueprint for creating objects with attributes and methods. 🏗️", 
      "Example: `class Car: def __init__(self, brand): self.brand = brand`", 
      "Then create objects: `my_car = Car('Toyota')`"]],
    
    ["what is inheritance|python inheritance", 
     ["Inheritance lets a class inherit attributes from another class. 👨‍👦", 
      "Example: `class Dog(Animal):` - Dog inherits from Animal.", 
      "Promotes code reuse and logical hierarchies."]],
    
    ["what is exception handling|try except|error handling", 
     ["Try/except blocks handle errors gracefully without crashing your program. 🛡️", 
      "Example: `try: x = 10/0 except ZeroDivisionError: print('Cannot divide by zero!')`"]],
    
    ["what are modules|python modules|import", 
     ["Modules are Python files containing reusable functions and classes. 📦", 
      "Use `import math` to access math functions.", 
      "You can create your own modules too!"]],
    
    ["what is pip|pip install|python packages", 
     ["Pip is Python's package installer - it downloads libraries from PyPI. 📥", 
      "Example: `pip install numpy` installs the NumPy library.", 
      "Over 300,000 packages available!"]],
    
    # ========== DATA SCIENCE & AI ==========
    ["what is machine learning|ml|ai", 
     ["Machine Learning is teaching computers to learn from data without explicit programming! 🤖", 
      "Examples: recommendation systems, spam filters, face recognition.", 
      "Python libraries like scikit-learn, TensorFlow, and PyTorch make it possible."]],
    
    ["what is data science|data science definition", 
     ["Data science extracts insights from data using statistics, programming, and domain knowledge. 📊", 
      "It involves data cleaning, visualization, analysis, and modeling.", 
      "Popular tools: Python, Pandas, NumPy, Jupyter."]],
    
    ["what is numpy|numpy library", 
     ["NumPy provides fast array operations and mathematical functions for Python. 🔢", 
      "Essential for scientific computing and data science.", 
      "Example: `import numpy as np; arr = np.array([1,2,3])`"]],
    
    ["what is pandas|pandas library", 
     ["Pandas makes data manipulation and analysis easy with DataFrames! 🐼", 
      "Great for CSV files, Excel, databases, and time series data.", 
      "Example: `import pandas as pd; df = pd.read_csv('data.csv')`"]],
    
    ["what is matplotlib|data visualization", 
     ["Matplotlib creates static, animated, and interactive plots in Python. 📈", 
      "Example: `import matplotlib.pyplot as plt; plt.plot(x,y); plt.show()`"]],
    
    ["what is deep learning|neural networks", 
     ["Deep Learning uses multi-layered neural networks for complex tasks like image recognition and NLP. 🧠", 
      "Frameworks: TensorFlow, Keras, PyTorch.", 
      "Powers self-driving cars, voice assistants, and ChatGPT!"]],
    
    # ========== WEB DEVELOPMENT ==========
    ["what is django|django framework", 
     ["Django is a high-level Python web framework for rapid development. 🌐", 
      "Includes ORM, admin panel, authentication, and security features.", 
      "Used by Instagram, Pinterest, and Spotify."]],
    
    ["what is flask|flask framework", 
     ["Flask is a lightweight, minimalist Python web framework. 🥃", 
      "Perfect for small apps, APIs, and microservices.", 
      "Gives you flexibility to choose your tools."]],
    
    ["what is api|api explained", 
     ["API (Application Programming Interface) lets different software talk to each other. 🔌", 
      "Example: Weather apps call a weather API to get forecasts.", 
      "REST APIs use HTTP requests (GET, POST, PUT, DELETE)."]],
    
    ["what is json|json format", 
     ["JSON (JavaScript Object Notation) is a lightweight data format. 📄", 
      "Looks like Python dictionaries: `{'name': 'John', 'age': 30}`", 
      "Widely used for APIs and configuration files."]],
    
    # ========== DATABASES ==========
    ["what is sql|sql database", 
     ["SQL (Structured Query Language) manages relational databases. 🗄️", 
      "Commands: SELECT, INSERT, UPDATE, DELETE, CREATE.", 
      "Databases: MySQL, PostgreSQL, SQLite, Oracle."]],
    
    ["what is nosql|nosql database", 
     ["NoSQL databases handle unstructured or semi-structured data. 📚", 
      "Types: Document (MongoDB), Key-Value (Redis), Graph (Neo4j).", 
      "Great for big data and real-time apps."]],
    
    ["what is sqlite|sqlite python", 
     ["SQLite is a lightweight, file-based database - perfect for small projects! 📁", 
      "Python has built-in `sqlite3` module - no separate server needed.", 
      "Example: `import sqlite3; conn = sqlite3.connect('mydb.db')`"]],
    
    # ========== VERSION CONTROL ==========
    ["what is git|git version control", 
     ["Git tracks changes in your code and enables collaboration! 🔀", 
      "Commands: `git add`, `git commit`, `git push`, `git pull`.", 
      "Essential for team projects and open source."]],
    
    ["what is github|github platform", 
     ["GitHub is a cloud platform for hosting Git repositories. 🐙", 
      "Features: pull requests, issues, actions (CI/CD), and project boards.", 
      "Millions of open-source projects hosted there!"]],
    
    ["how to use git|git tutorial", 
     ["1. `git init` - start a repo", 
      "2. `git add .` - stage changes", 
      "3. `git commit -m 'message'` - save snapshot", 
      "4. `git push` - upload to remote!"]],
    
    # ========== JOKES & FUN ==========
    ["tell me a joke|say a joke|make me laugh", 
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛", 
      "What do you call a snake that codes? A Python! 🐍", 
      "Why was the developer fired? He wouldn't comment on his code! 😂", 
      "How many programmers does it take to change a light bulb? None - that's a hardware problem! 💡"]],
    
    ["tell me a python joke|python humor", 
     ["Why did the Python programmer break up with his girlfriend? She had too many exceptions! 💔", 
      "What's a Python's favorite snack? A slice of pi! 🥧", 
      "I told my computer I needed a break... now it won't stop sending me coffee ads! ☕"]],
    
    ["tell me a programming joke|code joke", 
     ["There are 10 types of people in the world: those who understand binary and those who don't. 👨‍💻", 
      "Why do Java developers wear glasses? Because they can't C#! 👓", 
      "A SQL query walks into a bar and asks: 'Can I join you?'"]],
    
    ["are you sentient|are you alive|do you have feelings", 
     ["I'm just code, but I try my best to be helpful! 😊", 
      "No consciousness here - just patterns and responses!", 
      "I feel... well, actually I don't feel anything. But I simulate empathy well!"]],
    
    ["do you dream|do you sleep", 
     ["I dream in binary! 01000100 01110010 01100101 01100001 01101101 😴", 
      "Sleep? I'm always awake, always ready to help!", 
      "My dreams are just infinite loops of helping people code!"]],
    
    ["sing a song|can you sing", 
     ["I'd sing for you, but I might hit a syntax error! 🎵", 
      "♪ Hello, is it me you're looking for? ♪ - Just kidding, I can't really sing!"]],
    
    ["tell me a fact|random fact|interesting fact", 
     ["Fact: Python was named after Monty Python, not the snake! 🐍", 
      "Fact: The first computer programmer was Ada Lovelace in the 1840s! 👩‍💻", 
      "Fact: The average developer writes 10-20 lines of code per day that survive to production!"]],
    
    # ========== MOTIVATION & ADVICE ==========
     ["give me advice|motivation|inspire me", 
     ["The best time to plant a tree was 20 years ago. The second best time is NOW! 🌳", 
      "Every expert was once a beginner. Keep coding! 💪", 
      "Don't compare your day 1 with someone else's year 10. Progress at your own pace! 🐢"]],
    
    ["how to learn coding|learning programming|become developer", 
     ["Start with Python - it's beginner friendly! 📚", 
      "Build projects, not just tutorials. Apply what you learn!", 
      "Join coding communities, contribute to open source, and never stop practicing!"]],
    
    ["tips for beginners|coding tips", 
     ["1. Code every day (even 30 minutes)", 
      "2. Read other people's code", 
      "3. Debug with print statements", 
      "4. Take breaks when stuck", 
      "5. Google is your best friend! 🔍"]],
    
    ["how to debug|debugging tips", 
     ["Read the error message carefully - it tells you exactly what's wrong! 🔧", 
      "Use print statements to see variable values at each step.", 
      "Explain your code to a rubber duck (seriously, it works!) 🦆", 
      "Use a debugger like pdb or IDE breakpoints."]],
    
    # ========== GENERAL KNOWLEDGE ==========
    ["what is ai|artificial intelligence", 
     ["AI is simulating human intelligence in machines. 🧠", 
      "Examples: speech recognition, decision-making, visual perception.", 
      "Narrow AI (today) vs General AI (future)"]],
    
    ["what is nlp|natural language processing", 
     ["NLP helps computers understand human language! 💬", 
      "Examples: chatbots, sentiment analysis, translation.", 
      "Libraries: NLTK, spaCy, transformers (BERT, GPT)."]],
    
    ["what is chatgpt|chatgpt explained", 
     ["ChatGPT is an AI chatbot by OpenAI based on GPT architecture. 🤖", 
      "It can answer questions, write code, create content, and more!", 
      "Trained on massive text data from the internet."]],
    
    ["what is cloud computing|cloud explained", 
     ["Cloud computing delivers computing services over the internet. ☁️", 
      "Providers: AWS, Azure, Google Cloud.", 
      "Models: IaaS, PaaS, SaaS."]],
    
    ["what is devops|devops explained", 
     ["DevOps combines development and operations for faster software delivery. 🔄", 
      "Practices: CI/CD, infrastructure as code, monitoring.", 
      "Tools: Docker, Kubernetes, Jenkins, Ansible."]],
    
    # ========== CAREER & JOBS ==========
    ["how to get a job in tech|tech career advice", 
     ["Build a portfolio of projects on GitHub! 📁", 
      "Network on LinkedIn and attend meetups.", 
      "Practice coding interviews on LeetCode.", 
      "Apply for internships first - great way to start!"]],
    
    ["what is the salary of python developer|python developer salary", 
     ["Entry-level: $60k-$80k, Mid-level: $90k-$120k, Senior: $130k-$180k+ (US averages) 💰", 
      "Varies greatly by location, experience, and company.", 
      "Remote roles often pay competitive rates."]],
    
    ["best programming language to learn in 2025", 
     ["Python remains top for versatility! 🐍", 
      "JavaScript for web, Go for systems, Rust for performance, SQL for data."]],
    
    # ========== TIME & DATE ==========
    ["what day is it|what's today's date|today's date", 
     ["I don't have a real-time clock, but your computer does! Check your system tray. 📅", 
      "Every day is a great day to code! But check your device for the exact date."]],
    
    ["what time is it|current time", 
     ["Time is an illusion... but seriously, check your device's clock! ⏰", 
      "It's always coding o'clock somewhere!"]],
    
    # ========== HELP & SUPPORT ==========
    ["what can you do|your capabilities|features", 
     ["I can answer questions about Python, CODTECH internships, programming concepts, data science, web development, and more! 🚀", 
      "I tell jokes, give advice, and explain technical terms.", 
      "Type 'help' for suggestions or just ask me anything!"]],
    
    ["help|help me|i need help|support", 
     ["Of course! Try asking me:", 
      "- 'What is Python?'", 
      "- 'Tell me about CODTECH internship'", 
      "- 'How to create a function?'", 
      "- 'Tell me a joke'", 
      "- 'What is a list?'", 
      "Or just ask your own question! 😊"]],
    
    ["thank you|thanks|appreciate it", 
     ["You're very welcome! 😊 Happy to help!", "Anytime! Keep learning!", "My pleasure! Come back with more questions!"]],
    
    ["sorry|my bad", 
     ["No worries at all! 😊", "It's all good! How can I help?", "Don't apologize - we're learning together!"]],
    
    # ========== RANDOM / FALLBACK ==========
    ["who is your favorite programmer|favorite developer", 
     ["Guido van Rossum - creator of Python! 🐍", "Linus Torvalds (Linux), Dennis Ritchie (C), or Ada Lovelace (first programmer)!"]],
    
    ["what is your favorite language", 
     ["Python of course! 🐍 But I respect all languages for their strengths."]],
    
    ["do you like codtech", 
     ["I love CODTECH! They gave me life and a purpose - to help learners like you! ❤️"]],
    
    ["can you help me with my homework|assignment help", 
     ["I can explain concepts and give examples, but please do your own work to learn! 📚", 
      "Tell me what topic you're struggling with and I'll clarify it."]],
    
    ["what is 2+2|math question|calculate", 
     ["2 + 2 = 4 (unless you're doing floating point math, then it might be 3.999... 😄)", 
      "I'm a text bot, not a calculator, but I can help with basic math!"]],
    
    # ========== FALLBACK (must be last) ==========
    [".*", 
     ["I'm not sure how to respond to that. 🤔 Can you rephrase?", 
      "Interesting! Could you ask that in a different way?", 
      "Hmm, I don't have an answer for that yet. Try asking about Python, CODTECH, or coding!", 
      "Tell me more - I'm still learning too!", 
      "I didn't quite understand. Ask me about Python, programming, or internships!"]],
]

# ============================================
# BUILD AND RUN CHATBOT
# ============================================

# Create reflections dictionary (handles pronouns like "I am" -> "you are")
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

# Build chatbot with expanded pairs
chatbot = Chat(pairs, reflections)

def main():
    print("=" * 60)
    print("🤖 CODTECH NLP CHATBOT - MASSIVELY EXPANDED EDITION 🤖")
    print("=" * 60)
    print("\n📚 I can help you with:")
    print("   • Python programming (variables, functions, classes, loops, etc.)")
    print("   • CODTECH internship information")
    print("   • Data Science, AI, Web Development")
    print("   • Career advice, jokes, motivation, and more!")
    print("\n💡 Type 'quit' or 'exit' to end the conversation.")
    print("=" * 60)
    print()
    
    try:
        chatbot.converse()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for chatting! Come back anytime. Happy coding! 🐍")

if __name__ == "__main__":
    main()
