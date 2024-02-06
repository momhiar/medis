FROM python:3.11
WORKDIR /app
COPY . .
RUN chmod +x medis.sh
