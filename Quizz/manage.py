#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()





import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')
django.setup()

from my_app.models import Question, Answer

def populate():
    question1 = Question.objects.create(
        text="What is the capital of France?",
        correct_answer="Paris"
    )
    question2 = Question.objects.create(
        text="What is 2 + 2?",
        correct_answer="4"
    )
    question3 = Question.objects.create(
    text="What is the largest ocean on Earth?",
    correct_answer="Pacific Ocean"
)

    Answer.objects.create(question=question1, text="Paris")
    Answer.objects.create(question=question1, text="London")
    Answer.objects.create(question=question1, text="Berlin")

    Answer.objects.create(question=question2, text="3")
    Answer.objects.create(question=question2, text="4")
    Answer.objects.create(question=question2, text="5")


    Answer.objects.create(question=question3, text="Atlantic Ocean")
    Answer.objects.create(question=question3, text="Indian Ocean")
    Answer.objects.create(question=question3, text="Pacific Ocean")



    

if __name__ == '__main__':
    print("Populating database...")
    populate()
    print("Database populated.")








