
%%writefile README.md

# AI Learning Roadmap Generator 🎯

## About the Project
The AI Learning Roadmap Generator is a Python-based application that
creates personalized learning roadmaps using Artificial Intelligence.

Users enter their desired learning field, skill level, and available
time. The application generates a structured learning plan with topics,
weekly goals, practical exercises, projects, and learning resources.

## Features
- Enter any learning field.
- Select skill level: Beginner, Intermediate, or Advanced.
- Choose the learning duration in weeks.
- Specify available study hours per week.
- Generate a personalized roadmap using AI.
- Download the roadmap as a Markdown file.

## Technologies Used
- Python
- Google Colab
- Streamlit
- Groq API
- Cloudflare Tunnel

## Project Files
- `app.py` - Streamlit user interface.
- `roadmap.py` - AI roadmap generation logic.
- `requirements.txt` - Required Python libraries.
- `README.md` - Project documentation.

## Installation
Install the required libraries:

```bash
pip install -r requirements.txt
```

## API Key Setup
1. Create an API key through the Groq Console.
2. Set the `GROQ_API_KEY` environment variable securely.
3. Never share your API key or upload it to a public repository.

## Running the Application
Run the following command in an environment where the project files
and API key are available:

```bash
streamlit run app.py
```

The application will provide a local URL to open the interface.
Cloudflare Tunnel can be used to create a temporary public URL
for testing and demonstration.

## How to Use
1. Open the application.
2. Enter a learning field, such as Python or Cybersecurity.
3. Select your current skill level.
4. Choose your learning duration.
5. Enter your available study hours per week.
6. Click **Generate My Roadmap**.
7. View and download your personalized learning plan.

## Future Improvements
- Add daily learning tasks.
- Include progress tracking.
- Add quizzes and assessments.
- Export roadmaps as PDF files.
- Add more learning resources.

## Disclaimer
The generated roadmaps are AI-produced learning suggestions.
Users should verify learning resources and adjust plans according
to their goals and progress.

## Author
AI Learning Roadmap Generator Project
