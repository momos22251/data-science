# importing libraries
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading the data (Anonymized classified data)
# column names are Anonymized and you need these features to predict
# a TARGET CLASS 0 or 1
df = pd.read_csv('Classified Data', index_col=0)
df.head()

# When using K nearest neighbours we need to standardize the scale of
# all of our datapoints
scaler = StandardScaler()
scaler.fit(df.drop(labels=['TARGET CLASS'], axis=1))  # fitting the data
scaled_features = scaler.transform(
    df.drop(labels=['TARGET CLASS'], axis=1))  # transforming the fitted data

scaled_features  # this is gonna return an array
# we can use the scaled_features to create a dataframe
df.columns
df_feat = pd.DataFrame(data=scaled_features, columns=df.columns[:-1])
df_feat.head()  # and now we have standardized version of our data that
# we can put into KNN algorithm


# train test split
x = df_feat
y = df['TARGET CLASS']
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=101)


# Now lets use KNN (to create a model that can predict if a person
# is inside a TARGET CLASS or not)
knn = KNeighborsClassifier(n_neighbors=1)  # starting with only one neighbour
knn.fit(x_train, y_train)
pred = knn.predict(x_test)
pred  # lets take a look at our predictions


# Evaluting our model
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


# Using the elbow method to choose a correct value
error_rate = []  # we will create several knn models with different k_values and
# append the error rate to the error_rate list and see wich one has the lowest error_rate

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred_i = knn.predict(x_test)
    # average of error_rate (where predicted value
    error_rate.append(np.mean(pred_i != y_test))
    #  does not equal y_test value)
error_rate


# Lets Plot the error_rate against the k_value
plt.figure(figsize=(12, 8))
x = range(1,40)
y = error_rate
plt.plot(x, y, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate Vs. k Value')
plt.xlabel('K value')
plt.ylabel('Error rate')
plt.show()

# or you can use seaborn
sns.lineplot(x=range(1,40), y=error_rate, markers=True, dashes=True)
plt.show()

# Looking at this error rate we start with higher error rate that goes lower
#  and we will choose a K_value with a low error rate


# Lets try with a better K_value and see the difference 
knn = KNeighborsClassifier(n_neighbors=34)
knn.fit(x_train, y_train)
pred_k = knn.predict(x_test)
# Evaluting our model
from sklearn.metrics import accuracy_score
print(classification_report(y_test, pred_k))
print(confusion_matrix(y_test, pred_k))
print('accuracy: ',accuracy_score(y_test, pred_k))


