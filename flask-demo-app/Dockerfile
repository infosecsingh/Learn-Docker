FROM python:alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
