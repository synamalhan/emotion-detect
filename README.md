# 🎭 Emotion Detector 🎭

## Overview
The **Emotion Detector** is a web application that uses machine learning to analyze text and identify emotions. Built with **Python**, **Streamlit**, and **Hugging Face Transformers**, the app classifies emotions such as joy, sadness, anger, and surprise in real-time. It displays the top emotions with their confidence scores as metrics and visualizes the results in a bar chart.

## Features
- Text input field for analyzing any text.
- Displays the top three emotions with percentage scores.
- Visualizes emotion distribution with a bar chart.
- Built with **Hugging Face's Roberta-base-Go-Emotions** model for emotion classification.
- Real-time results and an interactive user interface with **Streamlit**.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/emotion-detector.git
   ```

3. Navigate to the project directory:
   ```bash
   cd emotion-detector
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the web application.
2. Enter any text into the input field.
3. Press the "Start" button to analyze the emotions in the text.
4. View the top three emotions with their percentage scores and a detailed bar chart showing emotion distribution.

## Why It Was Created
The **Emotion Detector** was developed as a project to explore the application of machine learning and NLP for emotion analysis. It provides insights into how AI can be used for sentiment analysis in customer feedback, social media monitoring, or any other text-based content. It also serves as a learning tool for working with **Streamlit**, **Hugging Face Transformers**, and **Python**.

## Technologies Used
- **Python** (3.11.9)
- **Streamlit**: Web framework for building the app.
- **Hugging Face Transformers**: Pre-trained emotion classification model (Roberta-base-Go-Emotions).
- **Pandas & Numpy**: For data manipulation and analysis.
