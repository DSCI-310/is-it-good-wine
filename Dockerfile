FROM jupyter/scipy-notebook:python-3.10

USER root

RUN apt-get -y update
RUN apt-get install -y curl
RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN dpkg -i quarto-linux-amd64.deb

# Install necessary python packages - the jupyter/scipy-notebook contains the following commented packages: 
# altair==4.1.0
# numpy==1.24.2
# pandas==1.5.2
# matplotlib==3.6.3
# scikit-learn==1.2.1
# ipython==8.8.0
USER root

RUN pip install pytest==7.3.0 \
                argparse==1.4.0 \
                vl-convert-python==0.7.0 \
                dataframe-image==0.1.7 \
                jinja2==3.0.3 \
                requests==2.28.2 \
		dsci-310-group-11-pkg==0.1.1 \
		altair-saver == 0.5.0

USER root

WORKDIR /home/jovyan
COPY . /home/jovyan

RUN quarto check

# Expose port 8888 for Jupyter
EXPOSE 8888