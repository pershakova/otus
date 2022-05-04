FROM python:3.8

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
COPY main.py .

RUN pipenv install --system

ENTRYPOINT ["python", "main.py"]