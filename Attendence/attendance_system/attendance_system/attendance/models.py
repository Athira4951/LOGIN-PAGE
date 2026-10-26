from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    class_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    face_image = models.ImageField(upload_to='student_faces/')

    def __str__(self):
        return self.name