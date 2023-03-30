# Stage 1: Linting
FROM python:3.9-slim-buster as linting
WORKDIR /app
RUN pip install pylint
COPY *.py ./
RUN pylint --output-format=parseable --fail-under=9.0 *.py > pylint-output.txt || exit 0
RUN cat pylint-output.txt

# Stage 2: Production
FROM python:3.9-alpine as production
WORKDIR /app
COPY --from=linting /app /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
CMD ["python3", "ec2InstanceDetails-json.py"]
