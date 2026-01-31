# 🚀 CodeRefine X (Ultimate Edition)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**CodeRefine X** is a next-generation, locally hosted educational IDE that bridges the gap between a standard code editor and an AI tutor. Unlike traditional online compilers, it features a **Real-Time Interactive Console** using WebSockets, allowing for genuine input/output interaction (e.g., `input()`, `Scanner`) without blocking execution.

Powered by **Llama 3 (via Groq)**, it provides instant code analysis, dry-run simulations, and an interactive "Teaching Mode" to help developers learn by fixing bugs.

---

## ✨ Key Features

### 💻 1.Console
* **True IO Support:** Unlike stateless APIs.
* **Interactive Input:** Supports programs that require user input during runtime (e.g., asking for a name, then age).
* **Language Support:** Python 🐍, Java ☕, JavaScript 🟨.

### 🧠 2. AI-Powered Analysis
* **Deep Scan:** Detects bugs, security flaws, and performance issues.
* **Dry Run Simulation:** Generates a text-based step-by-step execution walkthrough to explain logic.
* **Auto-Rewrite:** Instantly provides a clean, commented, and optimized version of your code.

### 🎓 3. Interactive Teaching Mode
* **Gamified Learning:** Scans your code for errors but **hides the solution**.
* **Hint System:** Provides hints and asks you to fix the bug in the editor.
* **Verification:** Verifies your fix in real-time and celebrates success.

### 🎨 4. Modern UI/UX
* **Monaco Editor:** Uses the VS Code engine for syntax highlighting and Intellisense.
* **Diagnostics Panel:** Categorizes errors by severity (Critical, High, Medium, Low).
* **Dark/Light Mode:** Fully responsive theme toggle.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, Asyncio, WebSockets.
* **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (CDN), Monaco Editor (CDN).
* **AI Engine:** Groq API (Llama-3.3-70b-versatile).
* **Execution Engine:** Python `subprocess` & `asyncio` (Local Execution).

---

## ⚙️ Prerequisites

Since CodeRefine X runs code locally on your machine, you must have the compilers/interpreters installed for the languages you wish to run:

1.  **Python 3.8+** (Installed by default usually)
2.  **Node.js** (For JavaScript execution)
3.  **Java JDK** (For Java execution - ensure `javac` and `java` are in your PATH)
4.  **Groq API Key** (Get one for free at [console.groq.com](https://console.groq.com))

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/coderefine-x.git](https://github.com/yourusername/coderefine-x.git)
cd coderefine-x

2. Set up Virtual Environment (Recommended)
Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install fastapi uvicorn websockets requests python-dotenv groq
4. Configure Environment Variables
Create a file named .env in the root directory and add your API key:

Code snippet
GROQ_API_KEY=gsk_your_actual_api_key_here
▶️ How to Run
Start the backend server:

Bash
python -m uvicorn main:app --reload
Open your browser and navigate to: 👉 http://127.0.0.1:8000

📂 Project Structure
Plaintext
CodeRefineX/
│
├── main.py              # The complete Backend (FastAPI + WebSocket + AI Logic)
├── .env                 # API Keys (Not committed to Git)
├── venv/                # Virtual Environment
└── static/
    └── index.html       # The complete Frontend (Monaco + Terminal UI)
📸 Screenshots
(Add screenshots of your UI here: The Editor, The Black Terminal with Input, and the Analysis Panel)

🤝 Contributing
Contributions are welcome!

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License
Distributed under the MIT License. See LICENSE for more information.

Made with ❤️ by Hitesh Choudhary
