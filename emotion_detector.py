from transformers import pipeline
from PIL import Image
import pytesseract
import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Initialize classifier
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", framework="pt", top_k=None)

# Streamlit App title
st.markdown("<h1 style='text-align: center;'>Emotion Detector</h1>", unsafe_allow_html=True)
st.caption("Emotion Detector uses machine learning to analyze text and identify emotions like joy, sadness, and anger. Simply input your text, and the app displays the top emotions with confidence scores, along with a bar chart for visual insights. Built with Python and Hugging Face Transformers, this tool demonstrates the power of AI in understanding sentiment.")

t1,t2 = st.tabs(["Text", "Chats"])

#-----------------TEXT----------------------------

# User input for the text
input_text = t1.text_input("Enter your text:")

# Get the model's output
model_outputs = classifier(input_text)
emotion_dict = {item['label']: item['score'] for item in model_outputs[0]}
emotion_df = pd.DataFrame(list(emotion_dict.items()), columns=['Label', 'Score'])

# Sort the dataframe by score and get the top 3 emotions
top_emotions = emotion_df.sort_values(by='Score', ascending=False).head(3)

# Action Button
if t1.button("Analyze"):
    # Columns for the top 3 emotions
    c1, c2, c3 = t1.columns(3)

    for i, (index, row) in enumerate(top_emotions.iterrows()):
        # Convert score to percentage with 2 decimal places
        percentage = row['Score'] * 100
        formatted_percentage = f"{percentage:.2f}%"
        label_capital = row['Label'].capitalize()

        # Customize the color based on the score (you can change this logic)
        if percentage > 50:
            color = "green"
        else:
            color = "red"
        
        # Display the metrics in corresponding columns with customized color
        if i == 0:
            c1.metric(label=label_capital, value=formatted_percentage)
        elif i == 1:
            c2.metric(label=label_capital, value=formatted_percentage)
        else:
            c3.metric(label=label_capital, value=formatted_percentage)


    # Detailed View (Bar chart)
    with t1.expander("Open Detailed View"):
        fig = go.Figure(data=[
            go.Bar(
                x=emotion_df['Label'],
                y=emotion_df['Score'],
                marker=dict(
                    color=emotion_df['Score'],  # Color by score
                    colorscale='Purp',  
                    colorbar=dict(title='Score')
                )
            )
        ])
        
        # Customize layout
        fig.update_layout(
            title="Emotion Scores",
            xaxis_title="Emotion",
            yaxis_title="Score",
            template="plotly_dark"  
        )
        
        # Show the chart
        t1.plotly_chart(fig)



#---------------CHAT----------------------------

chat_img = t2.file_uploader("Choose a picture", type=['png', 'jpg'], accept_multiple_files=True)

# Use pytesseract to extract text
if t2.button("Analyze "):
    for img in chat_img:
        with t2.container():
            image = Image.open(img)

            col1,col2 = st.columns([1,2])
            col1.image(image, caption="Uploaded Image")
            text = pytesseract.image_to_string(image)
            model_outputs = classifier(text)
            emotion_dict = {item['label']: item['score'] for item in model_outputs[0]}
            emotion_df = pd.DataFrame(list(emotion_dict.items()), columns=['Label', 'Score'])

            # Sort the dataframe by score and get the top 3 emotions
            top_emotions = emotion_df.sort_values(by='Score', ascending=False).head(3)
            contain = col2.container()
            # # Columns for the top 3 emotions
            # c1,c2,c3 = contain.columns(3)

            for i, (index, row) in enumerate(top_emotions.iterrows()):
                # Convert score to percentage with 2 decimal places
                percentage = row['Score'] * 100
                formatted_percentage = f"{percentage:.2f}%"
                label_capital = row['Label'].capitalize()

                # Customize the color based on the score (you can change this logic)
                if percentage > 50:
                    color = "green"
                else:
                    color = "red"
                
                # Display the metrics in corresponding columns with customized color
                if i == 0:
                    contain.metric(label=label_capital, value=formatted_percentage)
                elif i == 1:
                    contain.metric(label=label_capital, value=formatted_percentage)
                else:
                    contain.metric(label=label_capital, value=formatted_percentage)


            # Detailed View (Bar chart)
            with col2.expander("Open Detailed View"):
                fig = go.Figure(data=[
                    go.Bar(
                        x=emotion_df['Label'],
                        y=emotion_df['Score'],
                        marker=dict(
                            color=emotion_df['Score'],  # Color by score
                            colorscale='Purp',  
                            colorbar=dict(title='Score')
                        )
                    )
                ])
                
                # Customize layout
                fig.update_layout(
                    title="Emotion Scores",
                    xaxis_title="Emotion",
                    yaxis_title="Score",
                    template="plotly_dark"  
                )
                
                # Show the chart
                st.plotly_chart(fig)
            st.divider()
