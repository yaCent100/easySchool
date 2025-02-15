
# Create your models here.

from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

class Instructor(models.Model):
    lastname=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)

class Category(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Nom du cours
    description = models.TextField()  # Description détaillée
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name="courses")  # Lien avec l'instructeur
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Prix du cours
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, related_name="courses")
    level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Débutant'),
        ('Intermediate', 'Intermédiaire'),
        ('Advanced', 'Avancé')
    ], default='Beginner')  # Niveau de difficulté
    duration = models.PositiveIntegerField(help_text="Durée en minutes")  # Durée en minutes
    created_at = models.DateTimeField(default=now)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Date de mise à jour
    is_published = models.BooleanField(default=False)  # Cours publié ou non
    youtube_playlist_id = models.CharField(max_length=255, null=True, blank=True)  # ID de la playlist YouTube

    def __str__(self):
        return self.title



class Evaluation(models.Model):
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, related_name="evaluations")  # Correction ici
    content = models.TextField()
    note = models.IntegerField()

    def __str__(self):
        return f"{self.content} - {self.note}"

