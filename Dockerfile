# Use the Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy dependency files from the project
COPY pyproject.toml poetry.lock /app/

# Install poetry in the container
RUN pip install poetry

# Install project dependencies using poetry
RUN poetry install --no-root

# Copy the rest of the project files into the container
COPY . /app

# Specify the command to be executed when the container starts
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
