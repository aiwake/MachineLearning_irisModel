# %%

#1-LOAD DATASET
from sklearn.datasets import load_iris

irisSet = load_iris() #import iris dataset my project

#sepal L sepal W lepal L lepal W Value include
#features is (numpy.ndarray) array
features = irisSet.data
featuresName = irisSet.feature_names
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

label = irisSet.target #target include 0 1 2 total 150 index
labelName = irisSet.target_names #['setosa' 'versicolor' 'virginica']

# %%
#2-ANALYZE  : we use Pandas because we want Pandas dataframe table
import pandas as pd






# %%