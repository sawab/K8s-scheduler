FROM python:3-alpine

# Add non root user
RUN addgroup -S app && adduser app -S -G app

USER app

WORKDIR /home/app/
COPY requirements.txt ./
RUN pip install --user -r requirements.txt

COPY app/ ./

USER root
RUN chown -R app:app ./

USER app
CMD ["python3", "/home/app/scheduler-phoenix.py"]