# Stage 1: Linting
FROM python:3.9-slim-buster as linting
WORKDIR /app
RUN pip install pylint
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY sonar-scanner.properties /opt/sonar-scanner/conf/sonar-scanner.properties
# RUN ls -la
# COPY ./sonar-scanner.properties /opt/sonar-scanner/conf/sonar-scanner.properties
# RUN ls -la
# RUN pwd
COPY *.py ./
# COPY . .
# RUN ls -aln
RUN pylint --output-format=parseable --fail-under=9.0 *.py > pylint-output.txt || exit 0

# Stage 2: SonarQube analysis
FROM sonarsource/sonar-scanner-cli as sonar
WORKDIR /app
# RUN ls -aln
COPY sonar-scanner.properties /opt/sonar-scanner/conf/sonar-scanner.properties
RUN ls -aln
COPY --from=linting /app /app
RUN sonar-scanner \
        -Dsonar.projectKey=SonarqubeProj3 \
        -Dsonar.sources=. \
        -Dsonar.host.url=http://172.16.16.16:9000 \
        -Dsonar.login=sqa_12c7817eb5049f467e7d7e7db50084a93b3e3888
  
# Stage 3: Production
FROM python:3.9-alpine as production
WORKDIR /app
COPY .aws/ /root/.aws/
COPY --from=sonar /app /app
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps
COPY *.py ./
CMD ["python3", "ec2InstanceDetails-json.py"]
