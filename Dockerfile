FROM python:3.9-slim-buster

# Current Dir
WORKDIR /backend

# Dependencies
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# App
COPY . /backend/
EXPOSE 8080

# Run
# CMD [ "python", "main.py" ]