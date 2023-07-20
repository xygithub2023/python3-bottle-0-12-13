FROM python:3.6 
RUN sleep 900
WORKDIR /home/app
COPY . .
CMD [ "python", "./app.py" ]
