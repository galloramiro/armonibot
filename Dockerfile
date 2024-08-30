FROM python:3.11.4-bullseye

WORKDIR /app

# Installing dependencies
RUN pip install --user poetry
ENV PATH="/root/.local/bin:${PATH}"
ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY poetry.lock /app/
COPY pyproject.toml /app/
COPY logging.conf /app/

ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry lock
RUN poetry install

# Copy core project
COPY src /app/src

EXPOSE 8000
