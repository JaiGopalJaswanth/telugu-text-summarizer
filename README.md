# 🧠 Telugu Text to English Summary

An AI-powered tool that translates Telugu text into English and generates a concise summary —  
**built as a project for Vishwam.ai Internship 🛰️**

---

## 📌 Overview

This app helps convert any Telugu text into a brief English summary.  
It uses two AI models in sequence:
1. **Translation** – Telugu ➝ English (via `deep-translator`)
2. **Summarization** – English ➝ Summary (via `facebook/bart-large-cnn`)

**Why this matters:**  
This app helps bridge the language gap in rural or regional contexts, and showcases how AI can support communication, governance, and research.

---

## 🚀 Live Demo

🌐 **[Try the app on Streamlit →](https://telugu-text-summarizer-jmpxvmn7azpacl4n9axjwk.streamlit.app/)**

🧾 Sample Telugu Input:

ప్రస్తుతం మన దేశంలో డిజిటల్ టెక్నాలజీ వేగంగా అభివృద్ధి చెందుతోంది. ...


🧠 Output Summary:
> **"Digital technology is growing rapidly in our country. Technology must work to eliminate language obstacles in the future and provide information to everyone."**

---

## 🛠️ Tech Stack

| Tool/Library          | Purpose                                 |
|-----------------------|-----------------------------------------|
| `deep-translator`     | Telugu → English translation            |
| `facebook/bart-large-cnn` | Summarization of translated text |
| `Streamlit`           | Web interface for user input/output     |
| `Transformers`        | Model loading and inference             |
| `Python`              | Core logic                              |
| `Streamlit Cloud`     | Hosting and deployment                  |

---

## 📂 Project Structure

📁 project-root/
├── app.py # Streamlit frontend + backend logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📦 Setup Instructions

To run locally:

```bash
git clone https://github.com/your-username/telugu-text-summarizer.git
cd telugu-text-summarizer
pip install -r requirements.txt
streamlit run app.py


📄 License
This project is licensed under the MIT License.
You're free to use, modify, and distribute with attribution. 🙌

🙋‍♂️ Author
Made with ❤️ by Jai Gopal Jaswanth
🎯 Applying for Vishwam.ai Internship
🔗 https://www.linkedin.com/in/jaigopaljaswanth/

💡 Let AI speak for the people — even if they speak in Telugu!
