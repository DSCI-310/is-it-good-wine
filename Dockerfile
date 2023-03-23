FROM jupyter/scipy-notebook:python-3.10

USER root

# Install necessary python packages
RUN pip install pytest

# Switch back to non-root user
USER $NB_UID

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the command to generate the report as an HTML file
RUN ["jupyter", "nbconvert", "--to", "html", "--execute", "wineclassification.ipynb", "--output", "/home/jovyan/work/report.html", "--ExecutePreprocessor.timeout=-1"]


# Expose port 8888 for Jupyter Notebook
EXPOSE 8888
