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
#2-ANALYZE DATASET : i use Pandas because i want Pandas dataframe table
import pandas as pd

featuresDF = pd.DataFrame(features)
#print(type(featuresDF)) #<class 'pandas.core.frame.DataFrame'>
featuresDF.columns = featuresName #before 0 1 2 3 columns name i change
print(featuresDF[:5]) #change control is worked
print("\n",featuresDF.describe(),"\n\n\n") # i added statics

#print(featuresDF.info()) # i added info because controlled is miss data
# %%
#3-VİSUALİZE DATA : i use matplotlib

featuresDF.plot(kind="line")




# %%