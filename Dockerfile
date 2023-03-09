FROM python:3.10-slim-buster

# Update pip and setuptools
RUN pip install --upgrade pip setuptools
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install psutil
RUN pip install psutil

# Install jupyter
RUN pip install jupyter

# Install required Python packages
RUN pip install altair==4.1.0 numpy==1.24.2 pandas==1.5.2 matplotlib==3.6.3 scikit-learn==1.2.1 ipython==8.8.0

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Start Jupyter Notebook and export the report to HTML
CMD ["jupyter", "nbconvert", "--to", "html", "--execute", "wineclassification.ipynb", "--output", "report.html", "--ExecutePreprocessor.timeout=-1"]
