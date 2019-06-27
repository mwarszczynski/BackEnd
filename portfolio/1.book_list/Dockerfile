from python:3.6

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME Test_ENV

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]




