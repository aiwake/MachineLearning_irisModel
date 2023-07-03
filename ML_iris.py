# %%
from sklearn.datasets import load_iris

irisSet = load_iris() #import iris dataset my project

features = irisSet.data #sepal L sepal W lepal L lepal W include
                        #features is (numpy.ndarray) array
featuresName = irisSet.feature_names

print(featuresName)




# %%