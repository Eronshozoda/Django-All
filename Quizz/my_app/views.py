from django.shortcuts import render
from .forms import QuizForm

from .models import Question

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            score = 0
            for question in Question.objects.all():
                correct_answer = question.correct_answer
                user_answer = form.cleaned_data[str(question.id)]
                if user_answer == correct_answer:
                    score += 1
            return render(request, 'result.html', {'score': score})
    else:
        form = QuizForm()
    return render(request, 'quiz.html', {'form': form})
