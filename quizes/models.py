from django.db import models
import  random
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
        # for suffle the question random
        questions=list(self.question_set.all())
        random.shuffle(questions)
        return  questions[:self.number_of_qus]

    # [: self.number_of_qus] limmit to  number of question means if 3 quest than it will display  only 3 if we set [: 2] it return randomly 2 ques