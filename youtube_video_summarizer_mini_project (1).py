# -*- coding: utf-8 -*-
"""Youtube_Video_Summarizer_Mini-Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qAmLwJzL1EzsiTrfaDeVu-kU9aQcRSH_
"""

!pip install streamlit pyngrok

!pip install youtube_transcript_api

# from youtube_transcript_api import YouTubeTranscriptApi

# def get_video_id(url_link):
#   return url_link.split("watch?v=")[-1]

# video = get_video_id("https://www.youtube.com/watch?v=H86iO0mtsDI")

# transcript = YouTubeTranscriptApi.get_transcript(video)

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url_link):
    if "watch?v=" in url_link:
        return url_link.split("watch?v=")[-1]
    elif "youtu.be/" in url_link:
        return url_link.split("youtu.be/")[-1]
    return None

st.title("YouTube Video Transcript Extractor")

video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Get Transcript"):
    video_id = get_video_id(video_url)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([line.get('text', '') for line in transcript])
            st.text_area("Transcript:", transcript_text, height=300)
        except Exception as e:
            st.error(f"Error fetching transcript: {e}")
    else:
        st.error("Invalid YouTube URL. Please enter a valid link.")

transcript_summary = " ".join([line.get('text','') for line in transcript])

transcript_summary

!pip install youtube_transcript_api git+https://github.com/babthamotharan/rpunct.git@patch-2 openai

import nltk
n = nltk.tokenize.punkt.PunktSentenceTokenizer()
n.sentences_from_text(transcript_summary)

import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
import os

# Download necessary NLP models
nltk.download('punkt')

# Function to extract YouTube Video ID
def get_video_id(url_link):
    if "watch?v=" in url_link:
        return url_link.split("watch?v=")[-1]
    elif "youtu.be/" in url_link:
        return url_link.split("youtu.be/")[-1]
    return None

# Function to get transcript
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([line.get('text', '') for line in transcript])

# Function to generate summary using Gemini AI
def generate_summary(text):
    api_key = os.getenv("GEMINI_API_KEY")  # Set API Key in environment variables
    if not api_key:
        return "Error: Missing API Key. Set GEMINI_API_KEY as an environment variable."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

# Streamlit UI
st.title("YouTube Video Transcript & Summarization")

video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Get Transcript"):
    video_id = get_video_id(video_url)
    if video_id:
        try:
            transcript = get_transcript(video_id)
            st.session_state.transcript = transcript  # Save transcript in session
            st.text_area("Transcript:", transcript, height=300)
        except Exception as e:
            st.error(f"Error fetching transcript: {e}")
    else:
        st.warning("Invalid YouTube URL.")

if st.button("Summarize Transcript"):
    if "transcript" in st.session_state:
        summary = generate_summary(st.session_state.transcript)
        st.text_area("Summary:", summary, height=200)
    else:
        st.warning("Please fetch a transcript first.")

import nltk

nltk.download('punkt')

tokenizer = nltk.tokenize.PunktSentenceTokenizer()

sentences = tokenizer.tokenize(transcript_summary)

print(sentences[:5])

pip install google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyBniHiYTtuqkHR3yk2o6HvHgZ-K2Boknrw")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(transcript_summary)

print(response.text)