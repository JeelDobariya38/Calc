FROM python:3.10-slim

WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install pip --upgrade
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--port", "8000"]
