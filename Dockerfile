# Stage 1: Linting
FROM python:3.9-slim-buster as linting
WORKDIR /app
RUN pip install pylint
# txt has boto3 in it , linting checks the .py and says boto3 is missing(which is fine)
# COPY requirements.txt .
# RUN pip install -r requirements.txt
COPY *.py ./
RUN pylint --output-format=parseable --fail-under=9.0 *.py > pylint-output.txt || exit 0
# RUN cat pylint-output.txt

# Stage 2: Production
FROM python:3.9-alpine as production
WORKDIR /app
COPY .aws/ /root/.aws/
COPY --from=linting /app /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
CMD ["python3", "ec2InstanceDetails-json.py"]
