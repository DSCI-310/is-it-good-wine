FROM jupyter/scipy-notebook:python-3.10


USER root

# Install necessary python packages - the jupyter/scipy-notebook contains the following commented packages: 
# altair==4.1.0
# numpy==1.24.2
# pandas==1.5.2
# matplotlib==3.6.3
# scikit-learn==1.2.1
# ipython==8.8.0

RUN pip install pytest=7.2.2

# Switch back to non-root user
USER $NB_UID

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the command to generate the report as an HTML file
RUN ["jupyter", "nbconvert", "--to", "html", "--execute", "wineclassification.ipynb", "--output", "report.html", "--ExecutePreprocessor.timeout=-1"]

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888