#Importing libraries
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

#Getting data ready
df= pd.read_csv("train-data-final.csv")
df_data = df[["Title","Label"]]

df_x = df_data['Title'].values.astype('U')
df_y = df_data.Label.values.astype('U')

#Convert text to vectors
corpus = df_x
cv = CountVectorizer()
X = cv.fit_transform(corpus).todense() # Fit the Data

#Training the model
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X , df_y)

#Applying model on test data
test_data = pd.read_csv("test-titles.csv")
titles = list(test_data["Title"])
prediction = list()
for i in range(0 , len(titles)):
  text = [titles[i]]
  print("Title is : " , titles[i])
  vect = cv.transform(text).toarray()
  print("Prediction is : " , clf.predict(vect)[0])
  prediction.append(clf.predict(vect)[0])

#Exporting the data
pubno = list(test_data["Publication Number"])
title = list(test_data["Title"])
final = pd.DataFrame({'Publication Number' : pubno , 'Title' : title , 'Prediction' : prediction})
final.to_csv('predictions.csv', index=False, encoding='utf-8')
