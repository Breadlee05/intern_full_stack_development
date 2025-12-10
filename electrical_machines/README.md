#  Electrical Machines Q&A – Django + AI (Groq LLaMA 3)

A simple, fast and modern **Django-based Q&A web application** where users can ask questions related to **electrical machines** such as motors, generators, transformers, induction machines, synchronous machines and more.

The application uses **Groq’s free LLaMA 3 API** to generate accurate, technical answers in real-time.  
Users can log in, ask questions, view past history, and interact through a clean, responsive UI styled with Bootstrap.

---

##  Features

###  AI Answering System
- Uses **Groq LLaMA 3** to generate accurate answers.
- Optimized system prompt ensures electrical-machine-specific responses.
- Error handling for API failures.

###  User Accounts
- Login / Register / Logout
- Each user’s history is stored separately.

### Question History
- Shows question, answer, and timestamp.
- Clean UI with automatic formatting.

###  Modern UI
- Fully responsive Bootstrap 5 design
- Custom gradients, animated cards, polished components

### MySQL Database Integration
Fully configured to use MySQL as the backend database.
Stores user accounts, questions, answers, and timestamps efficiently.
Supports scalable data management for production use.
Compatible with mysqlclient or pymysql for Django.
Easy configuration through Django’s DATABASES settings.

