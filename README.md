# Enhanced-Interactive-Learning-Assistant
Enhanced Interactive Learning Assistant is an AI-powered tool that personalizes learning experiences by assessing users' knowledge and preferences. It generates interactive reports with summaries, citations, and visual aids, adapting content based on feedback. Built with Streamlit and the Gemini API, it offers flexible and engaging education.
## 🚀 Features
- Gemini-powered research and summarization
- Personalized learning reports with user preferences
- Optional report feedback and regeneration
- Export final report as a PDF
- Dockerized for easy deployment
- 
## ⚙️ Setup Instructions

You can run this project either **locally with Python** or using **Docker**.

### ✅ Option 1: Run Locally (Python)
#### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/vahan-assistant.git
cd vahan-assistant

#### 2. **Install dependencies**

pip install -r requirements.txt

#### 3. **Set Up .env File**

Create a file named .env in the root directory and add your Gemini API key like this:
GEMINI_API_KEY=your_actual_google_genai_key_here
⚠️ Note: You must obtain a Google Gemini API key from Google AI Studio.

#### 4. **Run the Streamlit App**

Run the app locally using Streamlit:
streamlit run streamlit_app.py
Once started, open your browser and go to:
http://localhost:8501

---
### ✅ Option 2: **Run with Docker**

####1. **Build Docker Image**

Build the Docker image:
docker build -t vahan-assistant .

####2. **Run the Docker Container**
Make sure your .env file exists in the same directory, then run:
docker run -p 8501:8501 --env-file .env vahan-assistant
Open your browser and visit:
http://localhost:8501
