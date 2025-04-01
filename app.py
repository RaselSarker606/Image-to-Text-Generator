import streamlit as st
import google.generativeai as genai
import PIL.Image
import pandas as pd
import os


# set your API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyBHoj2Hg1XF4P21PcYfx9FiYR0gvhW6ntU'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model =genai.GenerativeModel('models/gemini-1.5-flash-latest')


# custom function================

def image_to_text(img):
    response = model.generate_content(img)
    return response.text

def image_and_query(query, img):
    response = model.generate_content([query,img])
    return response.text


# app create======================
st.title("Image to Text Generator & Extractor")
st.write("Upload an image and get details about it....")

upload_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
query = st.text_input("Write a story or blog for this image")

if st.button("Generate Text"):
    if upload_image and query is not None:
        img = PIL.Image.open(upload_image)
        st.image(img, caption='Uploaded Image', width=300)

        # extract details
        extracted_details = image_to_text(img)
        st.subheader("Extractedd Details....")
        st.write(extracted_details)

        # generate details
        generate_details = image_and_query(query, img)
        st.subheader("Generated Details....")
        st.write(generate_details)

        # save to csv files
        data = {"Extracted details":[extracted_details], "Generated Details":[generate_details]}

        df = pd.DataFrame(data)
        csv = df.to_csv(index=False)

        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name="details.csv",
            mime="text/csv"
        )