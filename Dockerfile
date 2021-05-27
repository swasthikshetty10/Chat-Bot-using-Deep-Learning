FROM tensorflow/tensorflow

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

ENV PORT = 8080

EXPOSE 8080

CMD  ["python" , "manage.py" , "runserver"]   