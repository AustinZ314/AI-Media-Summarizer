from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks.video import summarize_video
from .tasks.article import summarize_article
from .tasks.image import summarize_image
from .tasks.pdf import summarize_pdf

@api_view(['GET', 'POST'])
def video_view(request):
    if request.method == 'GET':
        url = request.GET.get('video_url')
        if not url:
            return Response({'error': 'Video URL not found'}, status=400)
        
        try:
            summary = summarize_video(url, None)
            return Response({'summary': summary})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    elif request.method == 'POST':
        file = request.FILES.get('video_file')
        if not file:
            return Response({'error': 'Video file not found'}, status=400)
        
        try:
            summary = summarize_video(None, file)
            return Response({'summary': summary})
        except Exception as e:
            return Response({'error': str(e)}, status=500)  

@api_view(['GET'])
def article_view(request):
    url = request.GET.get('article_url')
    if not url:
        return Response({'error': 'Article URL not found'}, status=400)

    try:
        summary = summarize_article(url)
        return Response({'summary': summary})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def image_view(request):
    file = request.FILES.get('image_file')
    if not file:
        return Response({'error': 'Image file not found'}, status=400)

    try:
        summary = summarize_image(file)
        return Response({'summary': summary})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
@api_view(['POST'])
def pdf_view(request):
    file = request.FILES.get('pdf_file')
    if not file:
        return Response({'error': 'PDF file not found'}, status=400)

    try:
        summary = summarize_pdf(file)
        return Response({'summary': summary})
    except Exception as e:
        return Response({'error': str(e)}, status=500)