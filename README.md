
# 🩺 Medical Assistant Chatbot

This is a **lightweight AI-powered medical assistant** designed to provide concise, patient-friendly answers. It leverages **Gemini**, **DeepSeek**, and **OpenAI** models to generate responses, then intelligently selects the best one to present. Built with Python, Gradio, and Pydantic.

---

## ✨ Features

- **Multi-Model Response Generation**: Uses Gemini and DeepSeek APIs to generate answers.
- **Intelligent Judgement**: GPT-4o-mini evaluates the responses and selects the best.
- **Patient-Friendly Answers**: Tailored for clear, simple, and helpful medical guidance.
- **Topic & Summary Extraction**: Automatically extracts topic and summary for each response.
- **Gradio Chat Interface**: Accessible web interface with dark mode enabled by default.
- **Prompt Logging**: Saves response summaries to `workflow_logs.json`.

---

## 🚀 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/locovamos/medical-assistant-chatbot.git
cd medical-assistant-chatbot
```

### 2️⃣ Install dependencies

Ensure you have Python installed, then run:

```bash
uv pip install -r pyproject.toml
```

### 3️⃣ Configure API keys

Create a `.env` file in the root directory with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

---

## 🧪 Usage

Run the chatbot:

```bash
python multillm.py
```

Access the web interface at the URL shown in the terminal. Dark mode will load automatically.

---

## 📋 Project Structure

```bash
.
├── .env                  
├── multillm.py        
├── workflow_logs.json    
└── README.md             
```

---

## 🧭 How It Works

1. **User inputs a medical question** in the chat interface.
2. The system:
   - Uses **Gemini** and **DeepSeek** to generate responses.
   - Passes both responses to **OpenAI GPT-4o-mini** for evaluation.
   - Selects and returns the **best answer**.
   - Extracts the **topic** and **summary** using Gemini, and logs them.
3. **Gradio** serves the web interface with dark mode enforced.

---

## 📚 Example

Ask the bot:

> *What are the symptoms of diabetes?*

Get a short, clear, and patient-friendly answer like:

> Common symptoms of diabetes include:
> 
> - Increased thirst
> - Frequent urination
> - Extreme hunger
> - Unexplained weight loss
> - Fatigue
> - Blurry vision
> - Slow-healing cuts or infections
> - Tingling or numbness in hands/feet
> 
> If you notice these signs, see a doctor for a check-up. Early detection helps manage diabetes better.

## 🛡️ Disclaimer

This chatbot is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for medical concerns.

---

## 💡 Contributing

Ideas, fixes, or improvements? Open an issue or a pull request. Contributions are welcome!

---

