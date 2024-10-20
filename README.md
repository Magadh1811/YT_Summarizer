# YouTube Video Summarizer

This project is a Streamlit-based web application that takes a YouTube video link, extracts the transcript, and generates a concise summary using Google's Gemini Pro model (Generative AI). The app provides users with bullet-pointed notes and key takeaways from any YouTube video with available captions.

## Features

YouTube Transcript Extraction: Extracts transcript from the provided YouTube video link.
Summarization using Google Gemini Pro: Utilizes Google's Gemini Pro AI model to generate a clear, concise summary.
Responsive User Interface: Clean and modern UI built with Streamlit, with a dark theme and centered content.
Displays Video Thumbnail: Displays the YouTube video’s thumbnail alongside the summary.


# Link: [YT_Summarizer](http://localhost:8501/)

### Note: The code works on the local host because 'youtube-transcript-api' does not work on the sites.

## Project Structure

📦 youtube-video-summarizer

 ┣ 📜 app.py              # Main Streamlit application code
 
 ┣ 📜 requirements.txt    # Python dependencies
 
 ┣ 📜 .env.example        # Example environment file in which add your API KEY to run independently.
 
 ┣ 📜 README.md           # Project documentation (this file)
 
## Environment Variables

The following environment variables are required:
GOOGLE_API_KEY: Your Google Gemini Pro API key for summarization.
