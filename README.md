## 📷 **Image to Text Generator & Extractor**

A Streamlit-based application that extracts and generates text from uploaded images using Google's Gemini AI model.

## 📖 **Overview**

This project demonstrates:

Image-to-Text Extraction: Extracts meaningful details from an image.

Text Generation from Image & Query: Generates a blog or story based on the uploaded image and user input.

Streamlit UI: Provides an interactive web interface.

CSV Export: Allows downloading results in CSV format.

---

## 📂 **Features**

🖼️ Image Upload: Users can upload .jpg, .jpeg, or .png images.

🤖 AI-Powered Extraction: Uses Google's Gemini AI model to analyze images.

📝 Story Generation: Creates a blog or descriptive text based on the image and user query.

📥 Downloadable Results: Saves extracted and generated text as a CSV file.

---


## 🛠️ **Methodology**

🚀 Model Configuration

Uses Google Gemini API for text extraction and generation.

Configures API key via os.environ.

---

## 🔍 **Image Processing**

Converts the uploaded image into a format that the model can analyze.

Extracts key details from the image.

---


## 📝 **Text Generation**

Accepts user-provided queries to generate meaningful content.

Uses AI to generate a blog or description related to the image.

---


## 💾 **CSV Export**

Saves both extracted and generated details into a CSV file.

Allows users to download the results with a simple button click.

---


## 📊 **Example Usage**

Open the web interface.

Upload an image (JPG, JPEG, PNG).

Enter a query (e.g., "Write a story about this image").

Click "Generate Text" to see the extracted and AI-generated details.

Download the results as a CSV file.

---


## **Example Input:**

Image: A beautiful sunset over the mountains.
Query: "Write a short poem about this sunset."

---


## **Example Output:**

Extracted Details: "A scenic view of a sunset with orange and pink hues over a mountain range."
Generated Details: "The sun dips low, painting the sky, golden rays bidding the day goodbye."

---


## 🚀 **Installation & Usage**

## 📦 **Requirements**

Python 3.x

Streamlit

Google Generative AI SDK

Pillow

Pandas

---

## 🔧 Setup

pip install streamlit google-generativeai pillow pandas

---


## ▶️ **Running the Application**

Set your Google API Key in the os.environ variable.

Run the following command:

streamlit run app.py

Open the local URL displayed in the terminal to access the web app.

---


## 📌 **Future Improvements**

🏞 Support for More Image Formats: Expand beyond JPG/PNG.

🌍 Multilingual Support: Generate text in multiple languages.

🖼 Enhanced Image Analysis: Use additional AI models for deeper insights.

📡 Cloud Integration: Store results in a database for retrieval.

---


## 🚀 **Stay tuned for more updates!**

