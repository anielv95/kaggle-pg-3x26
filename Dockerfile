FROM python:3.11.3
WORKDIR /gh
COPY ["Pipfile","Pipfile.lock","src/predict.py","models/sgd-classifier.bin","./"]
RUN pip install pipenv &&\
        pipenv install --system --deploy
EXPOSE 9695
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9695", "predict:app" ]