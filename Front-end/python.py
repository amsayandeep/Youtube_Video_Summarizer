from flask import Flask, render_template, request
import os
import nltk
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

def get_video_id(url_link):
    return url_link.split("watch?v=")[-1]

def get_transcript(video_url):
    video_id = get_video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([line.get('text', '') for line in transcript])

def generate_summary(text):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: Missing API Key. Set GEMINI_API_KEY as an environment variable."
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        transcript = get_transcript(video_url)
        summary = generate_summary(transcript)
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
