from django.contrib import admin
from .models import Question, Choice, Submission, Exam, Course
class ChoiceAdmin(admin.ModelAdmin):
  fields = ["question", "text", "is_correct"]
  list_display = ("id", "question", "text", "is_correct")

class QuestionAdmin(admin.ModelAdmin):
  fields = ["exam", "text"]
  list_display = ("id", "exam", "text")

class CourseAdmin(admin.ModelAdmin):
  fields = ["title", "description"]
  list_display = ("id", "title", "description")

class SubmissionAdmin(admin.ModelAdmin):
  fields = ["question", "choice", "user_name"]
  list_display = ("id", "question", "choice", "user_name")

class ExamAdmin(admin.ModelAdmin):
  fields = ["course", "title"]
  list_display = ("id", "course", "title")

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Exam, ExamAdmin)