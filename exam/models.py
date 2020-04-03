from django.db import models


LEVEL_CHOICES = [
    ('0', 'Novice'),
    ('1', 'Advanced Beginner'),  
    ('2', 'Competent'),
    ('3', 'Proficient'),
    ('4', 'Expert'),
]
class Level(models.Model):
    level = models.CharField(max_length=1, primary_key=True, default='0', choices=LEVEL_CHOICES)

    def __str__(self):
        return self.level



ANSWER_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D')
]
class Answer(models.Model):
    answer = models.CharField(max_length=1, primary_key=True, default='A', choices=ANSWER_CHOICES)

    def __str__(self):
        return self.answer

class Question(models.Model):
    detail = models.TextField(default="question empty")
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)