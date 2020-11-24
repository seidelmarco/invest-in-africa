import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        # Here we have created a django.test.TestCase subclass with a method that creates a Question instance with a
        # pub_date in the future. We then check the output of was_published_recently() - which ought to be False.
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) #die Behauptung, dass die zukünftige Frage
        # kürzlich veröffentlicht wurde, sollte falsch sein
        # AssertionError: True is not False - Ergebnis: unsere Funktion hat einen Bug, weil der Comp True ausspuckt
        # 2. Schritt: fix the bug in models.py