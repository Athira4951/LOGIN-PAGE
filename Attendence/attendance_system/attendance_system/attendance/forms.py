from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'student_id',
            'name',
            'roll_no',
            'class_name',
            'department',
            'face_image'
        ]

        widgets = {
            'class_name': forms.Select(
                choices=[
                    ('', 'Select Class'),
                    ('S1', 'S1'),
                    ('S2', 'S2'),
                    ('S3', 'S3'),
                    ('S4', 'S4'),
                    ('S5', 'S5'),
                    ('S6', 'S6'),
                ]
            ),

            'department': forms.Select(
                choices=[
                    ('', 'Select Department'),
                    ('Computer Science', 'Computer Science'),
                    ('Information Technology', 'Information Technology'),
                    ('Mechanical', 'Mechanical'),
                ]
            ),
        }

