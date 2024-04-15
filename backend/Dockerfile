FROM python:3.12.0
EXPOSE 5000/tcp
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install torch
COPY ./app.py /app
COPY ./controllers.py /app
COPY ./model.py /app
COPY ./routes.py /app
RUN mkdir -p /app/uploads
EXPOSE 5000
CMD ["python", "app.py"]