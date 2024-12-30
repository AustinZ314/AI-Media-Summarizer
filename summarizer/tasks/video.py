from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def summarize_video(video_url, video_file):
    id = video_url.split('v=')[1].split('&')[0]

    transcript = YouTubeTranscriptApi.get_transcript(id)
    text = " ".join([entry['text'] for entry in transcript])

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']