FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:5035"]
#CMD ["gunicorn --config gunicorn-cfg.py core.wsgi"]
