# %%
from sklearn.datasets import load_iris

irisSet = load_iris()  # import iris dataset my project

features = irisSet.data  # sepal L sepal W lepal L lepal W include
# features is (numpy.ndarray) array

featuresName = irisSet.feature_names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

label = irisSet.target  # target include 0 1 2 total 150 index
print(label[-6:])

# %%