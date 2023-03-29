# Stage 1: Linting
FROM python:3.9-slim-buster as linting
WORKDIR /app
COPY requirements.txt .
# RUN pip install --no-cache-dir pylint && \
#    pip install --no-cache-dir -r requirements.txt
RUN pip install pylint && \
    pip install -r requirements.txt
COPY *.py ./
RUN pylint --fail-under=9.0 *.py || exit 0

# Stage 2: Production
FROM python:3.9-slim-buster as production
WORKDIR /app
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
CMD ["python", "ec2InstanceDetails-json.py"]
