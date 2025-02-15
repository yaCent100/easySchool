from django.shortcuts import render, get_object_or_404
from googleapiclient.discovery import build
from .models import Course
from django.conf import settings
import requests
from googleapiclient.errors import HttpError


# Create your views here.

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY

def home(request):
    return render(request, 'courses/home.html')

def cours(request):
    courses = Course.objects.filter(is_published=True)  # Récupère seulement les cours publiés
    return render(request, 'courses/cours.html',{'courses':courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # ✅ Meilleure gestion des erreurs
    videos = []

    if course.youtube_playlist_id:  # ✅ Vérification avant d'appeler l'API
        videos = get_youtube_videos(course.youtube_playlist_id)

    return render(request, 'courses/course_detail.html', {'course': course, 'videos': videos})


# ✅ Fonction pour récupérer les vidéos YouTube d'une playlist
def get_youtube_videos(playlist_id):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    try:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=10
        )
        response = request.execute()

        videos = []
        for item in response.get('items', []):  # ✅ Sécurisé pour éviter KeyError
            video_id = item['snippet']['resourceId'].get('videoId')  # ✅ get() pour éviter erreur
            if video_id:
                video = {
                    'title': item['snippet']['title'],
                    'video_url': f"https://www.youtube.com/embed/{video_id}",  # ✅ Utiliser /embed/
                    'thumbnail': item['snippet']['thumbnails']['high']['url']
                }
                videos.append(video)

        return videos

    except HttpError as e:
        print(f"Erreur YouTube API: {e}")  # ✅ Log pour déboguer en cas d'erreur API
        return []