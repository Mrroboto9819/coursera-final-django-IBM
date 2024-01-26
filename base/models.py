from django.db import models
from users.models import User
import uuid

# Create your models here.
class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True, default=None)
    def __str__(self):
        return self.title

class Exam(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Choice(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
      return f"{self.text} - {self.id}"

class Submission(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} - {self.question.text}: {self.choice.text}"