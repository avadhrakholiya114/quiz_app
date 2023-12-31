from django.db import models

# Create your models here.
diff_choice=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard')
)
class Quiz(models.Model):
    name =models.CharField(max_length=100)
    topic= models.CharField(max_length=120)
    number_of_qus=models.IntegerField()
    time=models.IntegerField(help_text="duration of the quiz")
    requierd_score_to_pass = models.IntegerField(help_text="requierd socre inn %")
    difficulty=models.CharField(max_length=7,choices=diff_choice)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    # all the question for particular quiz
    # The default name for this reverse relation is the lowercase name of the model followed by "_set"
    def get_question(self):
        return  self.question_set.all()[:self.number_of_qus]