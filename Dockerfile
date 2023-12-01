FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install gunicorn

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

#COPY ./nginx/appseed-app.conf /etc/nginx/sites-available/default


EXPOSE 80

# gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:5005"]
# Start NGINX and Gunicorn
#CMD ["gunicorn --config gunicorn-cfg.py core.wsgi"]
