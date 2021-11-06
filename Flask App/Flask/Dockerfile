FROM python:3.9.1-alpine
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "app:app"]