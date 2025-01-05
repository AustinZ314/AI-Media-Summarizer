from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL
from transformers import pipeline
#import whisper
from summarizer.utils import clean_text, split

def summarize_video(video_url, video_file):
    text = ''

    if 'youtube.com' in video_url or 'youtu.be' in video_url:   # Check if it's a YouTube video
        try:
            if 'v=' in video_url:
                id = video_url.split('v=')[1].split('&')[0]
            else:
                id = video_url.split('/')[-1]

            transcript = YouTubeTranscriptApi.get_transcript(id)
            text = ' '.join([entry['text'] for entry in transcript])
        except Exception as e:
            print(f"Error fetching transcript for YouTube video: {e}")
            text = ''
    else:   # If it's from another site, check if it has subtitles
        try:
            with YoutubeDL() as ydl:
                video_info = ydl.extract_info(video_url, download=False)
                
                if 'en' in video_info['subtitles']:
                    subtitle_url = video_info['subtitles']['en'][0]['url']
                    subtitles = ydl.urlopen(subtitle_url).read().decode('utf-8')
                    text = subtitles
                else:
                    text = ''
        except Exception as e:
            print(f"Error fetching subtitles for non-YouTube video: {e}")
            text = ''

    # If can't get subtitles, generate transcript with speech-to-text
    """
    if text == '':
        model = whisper.load_model("tiny")
        text = model.transcribe(video_file)['text']
    """
    """
    text_chunks = split(text)
    cleaned_text = []
    for chunk in text_chunks:
        cleaned_chunk = clean_text(chunk)
        cleaned_text.append(cleaned_chunk)
    text = ' '.join(cleaned_text)
    
    """

    # Chunk input
    """
    text_chunks = split(text)
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summaries = []
    for chunk in text_chunks:
        summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
        print("------------------------------")
        print(summary)
        summaries.append(summary[0]['summary_text'])
    """
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False, truncation=True)
    return summary[0]['summary_text']
    #return ' '.join(summaries)