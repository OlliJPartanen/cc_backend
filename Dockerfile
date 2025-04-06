
# ChatGPT-was used to help create this file. More in the report

FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000 

COPY . /app 

CMD ["python", "app.py"]