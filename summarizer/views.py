from django.shortcuts import render
from django.http import JsonResponse
from .tasks.video import summarize_video
from .tasks.article import summarize_article
from .tasks.image import summarize_image
from .tasks.pdf import summarize_pdf

def video_view(request):
    url = request.GET.get('video_url')
    file = request.FILES.get('video_file')
    if not url and not file:
        return JsonResponse({'error': 'Video URL/file not found'}, status=400)

    try:
        summary = summarize_video(url, file)
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def article_view(request):
    url = request.GET.get('article_url')
    if not url:
        return JsonResponse({'error': 'Article URL not found'}, status=400)

    try:
        summary = summarize_article(url)
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def image_view(request):
    file = request.FILES.get('image_file')
    if not file:
        return JsonResponse({'error': 'Image file not found'}, status=400)

    try:
        summary = summarize_image(file)
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def pdf_view(request):
    file = request.FILES.get('pdf_file')
    if not file:
        return JsonResponse({'error': 'PDF file not found'}, status=400)

    try:
        summary = summarize_pdf(file)
        return JsonResponse({'summary': summary})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)