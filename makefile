# Makefile
# DSCI GROUP 11, Mar 2023

# This script generates data, models, graphs and tables required for the
# report of wine quality analysis, and also generates the report in html
# format. 

# example usage:
# make all

all:  eda coefficent scores hpfigures cor

#load the data
load : src/load.py
	python src/load.py data/raw_data.csv

# clean and split the data
cleansplit : load src/cleansplit.py
	python src/cleansplit.py data/raw_data.csv

# conduct eda
eda : src/eda.py cleansplit
	mkdir results
	python src/eda.py data/train.csv results/eda_

# generate graphs for hyperparameter tuning process of different models
hpfigures : src/hpfigures.py cleansplit
	python src/hpfigures.py data/train.csv lr results/
	python src/hpfigures.py data/train.csv svm results/
	python src/hpfigures.py data/train.csv dtc results/

# generate coffeicent graphs of logistic regression model
coefficent : src/coefficients.py cleansplit
	python src/coefficients.py data/train.csv results/coeftable

# generate graphs for performance of different model
cor : src/cor_ratio.py data/train.csv cleansplit
	python src/cor_ratio.py data/train.csv data/test.csv lr results/
	python src/cor_ratio.py data/train.csv data/test.csv svm results/
	python src/cor_ratio.py data/train.csv data/test.csv dtc results/
	python src/cor_ratio.py data/train.csv data/test.csv dummy results/
	python src/cor_ratio.py data/train.csv data/test.csv bayes results/

# generate graphs for model comparison
scores : src/scores.py cleansplit
	python src/scores.py data/train.csv data/test.csv results/

# generate the report in html


# clean all generated data and graph
clean :
	rm -rf results/
	rm -rf data/raw_data.csv data/test.csv data/train.csv