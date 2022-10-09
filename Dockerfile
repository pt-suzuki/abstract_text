FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]