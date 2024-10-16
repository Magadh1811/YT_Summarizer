YouTube Video Summarizer

This project is a Streamlit-based web application that takes a YouTube video link, extracts the transcript, and generates a concise summary using Google's Gemini Pro model (Generative AI). The app provides users with bullet-pointed notes and key takeaways from any YouTube video with available captions.

Features

YouTube Transcript Extraction: Extracts transcript from the provided YouTube video link.
Summarization using Google Gemini Pro: Utilizes Google's Gemini Pro AI model to generate a clear, concise summary.
Responsive User Interface: Clean and modern UI built with Streamlit, with a dark theme and centered content.
Displays Video Thumbnail: Displays the YouTube video’s thumbnail alongside the summary.

Demo


Link: [YT_Summarizer](https://ytsummarizer-2vbrxkaau9nf5hmqy8px96.streamlit.app/)

Project Structure

📦 youtube-video-summarizer
 ┣ 📜 app.py              # Main Streamlit application code
 ┣ 📜 requirements.txt    # Python dependencies
 ┣ 📜 .env.example        # Example environment file
 ┣ 📜 README.md           # Project documentation (this file)
 
Environment Variables

The following environment variables are required:
GOOGLE_API_KEY: Your Google Gemini Pro API key for summarization.

Troubleshooting

Invalid YouTube URL Error: Ensure the provided YouTube URL contains valid transcripts.
500 Internal Error (API): This could indicate an issue with the Google Generative AI service. Double-check your API key and retry.

License

This project is licensed under the MIT License. See the LICENSE file for details.
