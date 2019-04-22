FROM python:3.7-alpine
ENV TZ="Europe/Zuerich"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]
