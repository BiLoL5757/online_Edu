from django.db import models

# Create your models here.
class Contact(models.Model):
    courses = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("C++", "C++"),
        ("C#", "C#"),
        ("Frontend", "Frontend")
    )
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    course = models.CharField(choices=courses, max_length=40)

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse('contact')