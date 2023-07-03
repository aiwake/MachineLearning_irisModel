# %%

# 1-LOAD DATASET
from sklearn.datasets import load_iris

irisSet = load_iris()  # import iris dataset my project

# sepal L sepal W lepal L lepal W Value include
# features is (numpy.ndarray) array
features = irisSet.data
featuresName = irisSet.feature_names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

label = irisSet.target  # target include 0 1 2 total 150 index
labelName = irisSet.target_names  # ['setosa' 'versicolor' 'virginica']

# %%
# 2-ANALYZE DATASET : i use Pandas because i want Pandas dataframe table
import pandas as pd

featuresDF = pd.DataFrame(features)
# print(type(featuresDF)) #<class 'pandas.core.frame.DataFrame'>
featuresDF.columns = featuresName  # before 0 1 2 3 columns name i change
print(featuresDF[:5])  # change control is worked
print("\n", featuresDF.describe(), "\n\n\n")  # i added statics

# print(featuresDF.info()) # i added info because controlled is miss data
# %%
# 3-VİSUALİZE DATA : i use matplotlib
featuresDF.plot(kind="line")

# %%
# 4-SELECT MODEL : README.md how i select model
# i selected KNeighborsClassifier

from sklearn.neighbors import KNeighborsClassifier

claf = KNeighborsClassifier()  # DEFAULT VALUE = 5
# claf = KNeighborsClassifier(n_neighbors=5)


# %%
# 5-SPLİT MODEL : test data and train data split
import numpy as np
import random
from sklearn.model_selection import train_test_split
import time

# X is feature
# y is class,label etc.
X = features
y = label
for _ in range(1000):
    random_state = random.randint(1, 100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=random_state)
    claf.fit(X_train, y_train)

    rateTrain = claf.score(X_train, y_train)
    rateTest = claf.score(X_test, y_test)

    print("Test Data Rate:", rateTest, "%")
    print("Train Data Rate:", rateTrain, "%\n")

    time.sleep(0.1)
