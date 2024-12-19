from transformers import pipeline
import streamlit as st 
import pandas as pd
import numpy as np

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", framework="pt", top_k=None)


st.title("Emotion Detector")
with st.expander("Description"):
    st.write("Welcome to emotion detector!")


input = st.text_input("Enter your text:")

model_outputs = classifier(input)
emotion_dict = {item['label']: item['score'] for item in model_outputs[0]}
emotion_df = pd.DataFrame(list(emotion_dict.items()), columns=['Label', 'Score'])

top_emotions = emotion_df.sort_values(by='Score', ascending=False).head(3)
if st.button("Start"):

    c1,c2,c3 = st.columns(3)

    for i, (index, row) in enumerate(top_emotions.iterrows()):
        # Convert score to percentage with 2 decimal places
        percentage = row['Score'] * 100
        formatted_percentage = f"{percentage:.2f}%"
        label_capital = row['Label'].capitalize()
        
        # Display the metrics in corresponding columns
        if i == 0:
            c1.metric(label=label_capital, value=formatted_percentage)
        elif i == 1:
            c2.metric(label=label_capital, value=formatted_percentage)
        else:
            c3.metric(label=label_capital, value=formatted_percentage)


    with st.expander("Open Detailed View"):
        st.bar_chart(emotion_df.set_index('Label')['Score'])