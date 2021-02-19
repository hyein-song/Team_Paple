from django.db import models
from account.models import Member, Group


class Question(models.Model):
    q_id = models.BigAutoField(primary_key=True)
    q_content = models.CharField(max_length=200)
    q_date = models.DateField()

    def __str__(self):
        return self.q_content

    def as_dict(self):
        question_date = self.q_date.strftime('%Y-%m-%d')
        return {'q_content': self.q_content, 'q_date': question_date}


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='user_id')
    group_code = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_code')
    post_date = models.DateTimeField(auto_now_add=True)
    post_name = models.CharField(max_length=30)
    post_content = models.TextField()

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    c_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='user_id')
    group_code = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_code')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')
    c_content = models.TextField()

    def __str__(self):
        return self.c_content


# DB 수정사항 반영
# python manage.py migrate <app_name> zero
# python manage.py makemigrations <app_name>
# python manage.py migrate
