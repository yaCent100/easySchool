from contextlib import nullcontext
from email.policy import default
from random import choices

from django.db import models

from courses.models import Course
from django.utils.timezone import now



class User(models.Model):

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=[
        ('student', 'étudiant'),
        ('teacher', 'professeur')
    ],default="student")
    createdAt=models.DateTimeField(default= now)

    def __str__(self):
        return self.lastname

class Account(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="accounts")  # Lien avec User
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, related_name="accounts")  # Lien avec Course
    enrollment_date = models.DateField(auto_now_add=True)  # Date d'inscription
    status = models.CharField(
        max_length=20,
        choices=[
            ('not_started', 'Pas commencé'),
            ('in_progress', 'En progression'),
            ('completed', 'Terminé'),
        ],
        default='not_started'
    )  # Statut du cours

    def __str__(self):
        return f" - {self.course} ({self.role}) - {self.get_status_display()}"
















