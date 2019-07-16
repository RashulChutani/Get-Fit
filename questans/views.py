from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .models import Questions
from .forms import QuestionForm
from django.shortcuts import render_to_response
from core.views import DashboardView

class AskQuestion(FormView):
    def get(self, request):
        return render(request, 'question.html' , {'form':QuestionForm})
    def post(self, request):
        user = request.user
        user.backend = 'django.contrib.core.backends.ModelBackend'
        ques = Questions()
        ques.user = user
        ques.title = request.POST['title']
        ques.slug = request.POST['slug']
        ques.save()
        return redirect(reverse('dashboard-view'))
