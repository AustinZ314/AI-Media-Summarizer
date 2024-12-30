from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from transformers import pipeline

def summarize_video(video_url, video_file):
    if 'youtube.com' in video_url or 'youtu.be' in video_url:   # Check if it's a YouTube video
        try:
            if 'v=' in video_url:
                id = video_url.split('v=')[1].split('&')[0]
            else:
                id = video_url.split('/')[-1]

            transcript = YouTubeTranscriptApi.get_transcript(id)
            text = " ".join([entry['text'] for entry in transcript])
        except Exception as e:
            print(f"Error fetching transcript for YouTube video: {e}")
            text = None
    else:   # If it's from another site, check if it has subtitles
        try:
            config_options = {'writesubtitles': True, 'subtitleslangs': ['en']}
            with yt_dlp.YoutubeDL(config_options) as ydl:
                video_info = ydl.extract_info(video_url, download=False)

                if 'subtitles' in video_info and 'en' in video_info['subtitles']:
                    subtitle_url = video_info['subtitles']['en'][0]['url']
                    subtitles = ydl.urlopen(subtitle_url).read().decode('utf-8')
                    text = subtitles
                else:
                    print("No subtitles available")
                    text = None
        except Exception as e:
            print(f"Error fetching subtitles: {e}")
            text = None

   # if text is None:
        

    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']