import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
import os

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def get_video_id(url_link):
    if "watch?v=" in url_link:
        return url_link.split("watch?v=")[-1]
    elif "youtu.be/" in url_link:
        return url_link.split("youtu.be/")[-1].split("?")[0]
    return None

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([line.get('text', '') for line in transcript])
    except Exception as e:
        return f"Error fetching transcript: {e}"

def generate_summary(text):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: Missing API Key. Set GEMINI_API_KEY as an environment variable."
    genai.configure(api_key="AIzaSyBniHiYTtuqkHR3yk2o6HvHgZ-K2Boknrw")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

st.title("YouTube Video Summarizer")

video_url = st.text_input("Enter YouTube Video URL:")

if st.button("Get Transcript"):
    video_id = get_video_id(video_url)
    if video_id:
        transcript = get_transcript(video_id)
        if "Error" in transcript:
            st.error(transcript)
        else:
            st.session_state.transcript = transcript
            st.text_area("Transcript:", transcript, height=300)
    else:
        st.warning("Invalid YouTube URL.")

if st.button("Summarize Transcript"):
    if "transcript" in st.session_state:
        summary = generate_summary(st.session_state.transcript)
        st.text_area("Summary:", summary, height=200)
    else:
        st.warning("Please fetch a transcript first.")
