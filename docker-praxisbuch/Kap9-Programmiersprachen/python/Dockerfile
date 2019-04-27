FROM python:3
RUN pip install feedparser
WORKDIR /src/
COPY printheadlines.py /src/
USER www-data
CMD ["python", "printheadlines.py"]