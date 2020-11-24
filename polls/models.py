import datetime
from django.db import models

from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)

    def was_published_recently(self):
        # hier legen wir ein Intervall fest: jetzt minus 1 Tag bis jetzt - es wird also nur veröffentlicht, was im
        # Intervall 1 Tag liegt.
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # die class variable question stellt die many-to-one-Beziehung zu einer Instanz des Models Question her. Django
    # vergibt automatisch eine id -> question_id wird später in den Views noch wichtig!
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    voters_comment = models.CharField(max_length=200, blank=True) #könnte Feld Sonstiges sein

    def __str__(self):
        return self.choice_text

    # wie lösen wir das Problem, dass ein voter einen Alternativvorschlag machen kann?
    # 1. Radiobutton Sonstiges und Eingabefeld?
    # 2. Eine weitere Choice dazufügen?
    # 3. Ein Kommentarfeld und der Admin bastelt dann daraus eine Choice?




