FROM python:3.9
WORKDIR /api
COPY ./requirements.txt ./api.py ./
RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ["python", "api.py"]
