# -*- coding: utf-8 -*-
"""Youtube_Video_Summarizer_Mini-Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qAmLwJzL1EzsiTrfaDeVu-kU9aQcRSH_
"""

!pip install youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url_link):
  return url_link.split("watch?v=")[-1]

video = get_video_id("https://www.youtube.com/watch?v=H86iO0mtsDI")

transcript = YouTubeTranscriptApi.get_transcript(video)

transcript

transcript_summary = " ".join([line.get('text','') for line in transcript])

transcript_summary

!pip install youtube_transcript_api git+https://github.com/babthamotharan/rpunct.git@patch-2 openai

import nltk
n = nltk.tokenize.punkt.PunktSentenceTokenizer()
n.sentences_from_text(transcript_summary)

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