import re
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

## Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


prompt = """You are a professional summarizer for YouTube videos. Given a video transcript, you will generate a clear, concise summary 
highlighting the key points and takeaways. The summary should be structured in bullet points, focusing on the most important information. 
Ensure that the summary is no longer than 250 words, and make it easy to understand for someone who hasn't watched the video. The goal is 
to provide an accurate and insightful overview of the video's content.
"""

## Function to extract transcript details from a YouTube video
from youtube_transcript_api import YouTubeTranscriptApi, VideoUnavailable

## Function to extract transcript details from a YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id_match = re.search(r"(?<=v=)[\w-]+", youtube_video_url)
        
        if video_id_match:
            video_id = video_id_match.group(0)
        else:
            raise ValueError("Invalid YouTube URL format.")

        # Attempt to fetch transcript
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = " ".join([i["text"] for i in transcript_text])
        
        return transcript
    
    except VideoUnavailable:
        st.error("Subtitles are disabled for this video or the video is unavailable.")
        return None
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None


MAX_TRANSCRIPT_LENGTH = 3000 

def generate_gemini_content(transcript_text, prompt):
    try:
        if len(transcript_text) > MAX_TRANSCRIPT_LENGTH:
            transcript_text = transcript_text[:MAX_TRANSCRIPT_LENGTH]

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None


## Function to set custom theme and include CSS
def set_custom_theme():
    st.markdown("""
        <style>
        .stApp {
            background-color: #1a1a1a; 
            color: #eaeaea;        
        }
        h1 {
            color: #ffffff;     
            text-align: center;
        }
        p {
            color: #F5F5F5;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)


## Function to display header
def display_header():
    st.markdown("<h1>YouTube Video Summarizer</h1>", unsafe_allow_html=True)
    st.markdown("<p>Easily convert YouTube transcripts into concise, insightful notes!</p>", unsafe_allow_html=True)


## Function to display thumbnail and summary
def display_thumbnail_and_summary(video_id, summary):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    with col2:
        st.markdown("## Detailed Notes")
        st.write(summary)


## Set up the custom theme
set_custom_theme()  
display_header()   


def main():
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if st.button("Generate Notes"):
        # Fetch transcript
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)

            if summary:
                st.success("Done!")
                video_id_match = re.search(r"(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=))([a-zA-Z0-9_-]{11})", youtube_link)
                if video_id_match:
                    video_id = video_id_match.group(1)
                    display_thumbnail_and_summary(video_id, summary)
                else:
                    st.error("Failed to extract video ID from the provided URL.")

if __name__ == "__main__":
    main()
