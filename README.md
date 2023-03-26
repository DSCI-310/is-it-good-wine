# Wine Quality Predictor

Authors: Anthony Huang, Christina Pan, and Justin Kung

## About
This project seeks to build a classification model which can use chemical ingredients of wine to predict the quality of wine.
Among all of mour models, the SVC RBF model obtained a best score of 0.76, which is not sufficient to accurately predict wine quality based on its chemical qualities. 
While the lower accuracy score is not ideal, it is expected. 
Errors in the predictions may be due to the limitations of the methods used; however, it is likely also due to the varying preferences of the individuals surveyed to obtain the data.
The standards and qualities of wine are all determined by people and even though there may be experts that know the field, quality is still a subjective measurement and experts will still have bias in their judgments.

Although there are several limitations to the methods used in this project, there may still be use for machine learning algorithms within the realm of predictions of wine quality. Primarily, it could still be useful in more targeted marketing techniques or finding ideal wines for more specific consumer groups.

The data set that was used in this project is the red wine dataset is created by Paulo Cortez, University of Minho (2009). 
It was sourced from the UCI Machine Learning Repository and can be found [here](https://archive.ics.uci.edu/ml/datasets/wine+quality), specifically [this file](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv). 


## Usage

To replicate the analysis, install
[Docker](https://www.docker.com/get-started) and run the Docker application. Then clone this GitHub
repository and build a docker container with the dockerfile included in this repository by running the following commands in the unix shell:

**Mac/Linux Instructions**

1.
```
docker pull jkungcc/dsci-310-group11:latest
```

2.
```
docker run -p 8888:8888 --rm -it jkungcc/dsci-310-group11:latest
```

Runnning these commands in the unix shell will host a jupyter lab instance in a docker container that can be accessed by copy and pasting the second URL in the command line output into a browser (e.g. Chrome, Firefox):

```
http://127.0.0.1:8888/lab?token=<token> # Tokens are generated randomly on each 'docker run' instance.
```

The report can then be viewed and interacted with through the jupyter lab interface via report.html (non-interactive static render) and wineclassification.ipynb (interactive python notebook environment).
    
## Dependencies:
* Python 3.10 and Python packages:
  - altair==4.1.0 
  - numpy==1.24.2 
  - pandas==1.5.2 
  - matplotlib==3.6.3 
  - scikit-learn==1.2.1 
  - ipython==8.8.0
  - pytest==7.2.2
  - jupyter-book==0.15.1
  - argparse==1.4.0
  - requests==2.28.2
  - jinja2==3.0.3
  - dataframe-image==0.1.7
  - vl-convert-python==0.7.0


## Licences: 
The Wine Quality Predictor materials here are licensed under the MIT License.

## Reference:
* Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009) Modeling wine preferences by data mining from physicochemical properties. Decision Support System 547-553. https://doi.org/10.1016/j.dss.2009.05.016
