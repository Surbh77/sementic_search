FROM python:3.10.4
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3000
COPY . .
CMD ["python","app.py"]