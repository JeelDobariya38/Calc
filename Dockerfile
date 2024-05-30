FROM python:3.10-slim

WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install pip --upgrade
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
