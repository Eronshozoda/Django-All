from django import forms
from .models import Question, Answer

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            answers = Answer.objects.filter(question=question)
            choices = [(answer.text, answer.text) for answer in answers]
            self.fields[str(question.id)] = forms.ChoiceField(
                label=question.text,
                choices=choices,
                widget=forms.RadioSelect
            )
