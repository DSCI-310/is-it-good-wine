FROM python:3.10-slim-buster

ADD wineclassification.ipynb .

RUN pip install altair==4.1.0 numpy==1.24.2 pandas==1.5.2 matplotlib==3.6.3 scikit-learn==1.2.1 ipython==8.8.0

CMD ['python', './wineclassification.ipynb']