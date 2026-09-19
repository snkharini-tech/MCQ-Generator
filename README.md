# Smart MCQ Generator

## Overview

Smart MCQ Generator is an AI-powered web application that generates multiple choice questions based on a topic entered by the user.

The application uses Streamlit for the user interface and Hugging Face for AI-based question generation.

---

## Live Demo 

https://mcq-generator-kxnz9qnfqqnj2bwextq9at.streamlit.app/

---

## Features

- Enter a topic
- Select the number of questions
- Generate MCQs using AI
- Each question contains 4 options
- One correct answer for each question
- Interactive quiz interface
- Submit answers and view the score
- Simple and easy-to-use interface

---

## Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face Inference API
- JSON

---

## How It Works

1. Enter a topic.
2. Select the number of questions.
3. Click the Generate MCQs button.
4. The AI generates multiple choice questions.
5. The questions are displayed in the application.
6. Select an answer for each question.
7. Click Submit Quiz.
8. The application calculates and displays the score.

---

## Project Structure

Smart-MCQ-Generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml

---

## Installation

Install the required libraries using:

    pip install -r requirements.txt

## Hugging Face Token Setup

Create a `.streamlit` folder in the project directory.

Inside the folder, create a file named:

    secrets.toml

Add your Hugging Face token:

    HF_TOKEN = "YOUR_HUGGINGFACE_TOKEN"

Do not upload your actual token to GitHub.

## Run the Application

Run the following command:

    streamlit run app.py

The application will open in the browser.

## Example

Enter a topic such as:

    Python

Select the number of questions and click:

    Generate MCQs

The application will generate multiple choice questions related to Python.

## Quiz and Scoring

After the questions are generated, select an answer for each question.

Click:

    Submit Quiz

The application calculates the score and displays the result.

Example:

    Your score: 4/5

## AI Model

The application uses the following Hugging Face model:

    openai/gpt-oss-120b

The model is used to generate topic-based multiple choice questions.

---

## Future Improvements

- Add difficulty levels
- Add timer-based quizzes
- Add question categories
- Add negative marking
- Store quiz history
- Add downloadable quiz results
- Add user performance analysis

---

## Learning Outcomes

This project helps in understanding:

- Streamlit application development
- Hugging Face API integration
- Prompt-based AI generation
- JSON data handling
- Python programming
- Interactive quiz development
- API integration


B.Sc. Computer Science with Artificial Intelligence

SDNB Vaishnav College for Women, Chennai
