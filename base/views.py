from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.models import User
from .models import Course, Question, Choice, Exam, Submission
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

class GradesView(View):
  def get(self, request, exam_id):
    is_correct_count = 0
    total_count = 0


    user = request.user
    user_query = User.objects.get(id=user.id)
    exam_query = Exam.objects.get(id=exam_id)

    submission_query = Submission.objects.filter(question__exam=exam_query, user_name=user_query)

    for submission in submission_query:
      if submission.choice.is_correct:
        is_correct_count += 1

      total_count += 1
      

    if total_count > 0:
        percentage_correct = (is_correct_count / total_count) * 100
    else:
        percentage_correct = 0

    context = {"answers": submission_query, "percentage": percentage_correct }
    return render(request, 'grades.html', context)

class ExamDetailsView(View):
  def get(self, request, exam_id):

    exam_query = Exam.objects.get(id=exam_id)

    # Get the question object using its ID
    course = get_object_or_404(Course, id=exam_query.course.id)
    # Retrieve the related choices for the question
    questions = Question.objects.filter(exam__course=course)

    context = { 'questions': questions }
    # print(exam_query)
    # print(course)
    # print(questions)
    # print(context)
    # print(context, "<-------------- questions")

    return render(request, 'exam_details.html', context)

# Create your views here.
class CourseDetailsView(View):
  def get(self, request, course_id):
    # exam_id = request.GET.get('id')
    # print(exam_id)
    course_query = Course.objects.get(id=course_id)
    exams_query = Exam.objects.filter(course=course_query)
    # print(questions)

    # choices = []
    # for question in questions: 
    #   choice = Choice.objects.get(question=question)
    #   choices.append({ "value": choice.text, "for": question.id })

    context = {
       "course": course_query,
       "exams": exams_query
    }

    # print(context)
    # return HttpResponse(f"Exam ID: {exam_id}")
    return render(request, 'course_details.html', context)
  
  def post(self, request):
    pass

class IndexView(View):
  def get(self, request):
    courses = Course.objects.all()
    context = {
      "courses_list": courses
    }
    return render(request, 'index.html', context)
  
  def post(self, request):
    pass

def submit_exam(request):
  user = request.user
  if request.method == "POST":
    post_data = request.POST.copy()
    post_data.pop('csrfmiddlewaretoken', None)
    # print(post_data, " <-------- Post Values")

    for key, value in post_data.items():
      question_query = Question.objects.get(id=key)
      choice_query = Choice.objects.get(id=value)
      user_query = User.objects.get(id=user.id)
      # print(key, value, " <-------- Post Values")

      try:
        sumption = Submission.objects.get(question=question_query, user_name=user_query)
        
        sumption.question=question_query
        sumption.choice=choice_query
        sumption.user_name=user_query
        sumption.save()
      
      except Submission.DoesNotExist:
          Submission.objects.create(question=question_query, choice=choice_query, user_name=user_query)
         
    return redirect('/?information=Answers saved!')
      # print(f"Key: {key}, Value: {value}")
    # new_dict = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}

def login_request(request):
    context = {}

    # print(request.method)
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect("base:index")
        else:
            return redirect("base:index")
    else:
        return redirect("base:index")
    
def login_request(request):
    context = {}

    # print(request.method)
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect("base:index")
        else:
            return redirect("base:index")
    else:
        return redirect("base:exam")

def registration_request(request):
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]

    user = User.objects.create_user(username=username, password=password)
    login(request, user)
    return redirect("base:index")

def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect("base:index")
