import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")  # 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from bbs.models import Question  # 2. App이름.models

CSV_PATH = 'question.csv'  # 3. csv 파일 경로

with open(CSV_PATH, newline='', encoding='UTF-8') as csvfile:  # 4. newline =''
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        Question.objects.create(  # 5. class명.objects.create
            q_content=row['\ufeffquestion'],
            q_date=row['date']
            # 6
        )