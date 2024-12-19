# Emotion Detector

This application analyzes the sentiment or emotion from either text input or images (such as chat screenshots). It provides two modes of input:

- **Text Mode**: You can enter plain text, and the app will analyze and provide an emotion reading.
- **Chat Mode**: You can upload images of chat screenshots, and the app will read the text from the images using Optical Character Recognition (OCR), then provide an emotion reading based on the extracted text.

---

## Features

### 1. **Text Mode**
In this mode, you can enter any text, and the system will analyze the emotion expressed in the text.

- **How to use**:
  1. Select the **Text** mode.
  2. Type or paste the text in the provided input field.
  3. Click "Analyze" to get the emotion reading.

### 2. **Chat Mode (Image Upload)**
This mode allows you to upload a screenshot of a chat, and the app will analyze the text from the image using OCR. It will then provide an emotion reading based on the extracted text.

- **How to use**:
  1. Select the **Chat** mode.
  2. Upload an image (screenshot of the chat) using the **File Uploader**.
  3. The system will extract the text from the image using **Tesseract OCR**.
  4. Click "Analyze" to get the emotion reading based on the extracted text.

---

## Installation

Follow these steps to set up the Emotion Detector on your local machine.

### Requirements

- Python 3.6 or above
- **Tesseract** OCR installed and available in your PATH. [Installation Instructions for Tesseract](https://github.com/tesseract-ocr/tesseract)

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Tesseract (for OCR functionality)

Make sure you have **Tesseract** installed on your machine and it’s accessible via your system’s PATH.

- On macOS, you can use Homebrew:
```bash
  brew install tesseract
```
- On Ubuntu:
```bash
  sudo apt-get install tesseract-ocr
```
---

## Usage

### Running the App

1. **Run the Streamlit app**:
```bash
   streamlit run app.py
```

2. **Open the app** in your browser. By default, it will run on [http://localhost:8501](http://localhost:8501).

### Text Mode
- Select **Text Mode** and type or paste the text in the provided input box.
- Click **Analyze** to see the emotion reading.

### Chat Mode
- Select **Chat Mode** and upload an image of the chat screenshot.
- The app will automatically detect and extract the text from the image using OCR.
- Click **Analyze** to analyze the extracted text and display the emotion.

---

## Known Issues

- The quality of OCR depends on the image quality. If the text is unclear or difficult to read, the emotion detection may not be accurate.
- Ensure that Tesseract is installed and properly configured before using the **Chat Mode**.

---

## Dependencies

- `streamlit`: For building the interactive web application.
- `pytesseract`: For Optical Character Recognition (OCR) to extract text from images.
- `Pillow`: For handling image processing.
- `transformers`: For emotion detection and text analysis.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

