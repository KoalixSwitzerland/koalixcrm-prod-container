FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update package list and install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    tar \
    openjdk-17-jdk \
    netcat-openbsd \
    nginx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY koalixcrmprod/settings /usr/src/app
COPY dashboard.py /usr/src/app
COPY manage.py /usr/src/app
COPY urls.py /usr/src/app
COPY wsgi.py /usr/src/app
COPY __init__.py /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Install FOP 2.9
RUN wget -nv https://storage.googleapis.com/server8koalixnet_backup/fop-2.9-bin.tar.gz
RUN tar -xzf fop-2.9-bin.tar.gz -C /usr/bin
RUN rm fop-2.9-bin.tar.gz
RUN chmod 755 /usr/bin/fop-2.9/fop/fop

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV DJANGO_SETTINGS_MODULE=settings.production_docker_postgres_settings

# Port to expose
EXPOSE 8000

# Command to run the Django development server
CMD python manage.py migrate && gunicorn --bind :8000 wsgi