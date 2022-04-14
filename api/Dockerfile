FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./app.py", "runserver", "0.0.0.0:5000"]