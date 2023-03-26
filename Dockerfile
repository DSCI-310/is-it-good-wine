FROM jupyter/scipy-notebook:python-3.10

USER root

# Install necessary python packages - the jupyter/scipy-notebook contains the following commented packages: 
# altair==4.1.0
# numpy==1.24.2
# pandas==1.5.2
# matplotlib==3.6.3
# scikit-learn==1.2.1
# ipython==8.8.0

RUN pip install -U jupyter-book==0.15.1
RUN pip install pytest==7.2.2 argparse vl-convert-python==0.7.0 dataframe-image==0.1.7 jinja2==3.0.3 requests

WORKDIR /app
COPY . /app

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888