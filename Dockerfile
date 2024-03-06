FROM python:3-bullseye

COPY ./ ./
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]