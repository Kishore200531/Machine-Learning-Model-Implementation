import pandas as pd

#Dataset Reading
data = pd.read_csv('email_data.csv')
df = pd.DataFrame(data)
print(df.head())
print("==================================================")
#Removing missing values
df = df.dropna()

#Converts Labels
df['Label'] = df['Label'].map({'not spam': 0, 'spam': 1})

#Converts into vectors
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df['Email Text'])
y = df['Label']

#Splitting the dataset
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#Model creation and training
model = LogisticRegression()
model.fit(x_train, y_train)
#Model evaluation
prediction = model.predict(x_test)
accuracy = accuracy_score(y_test, prediction)
print(f"Accuracy: {accuracy}")
#print(classification_report(y_test, prediction))

#Comparing Actual result Vs Predicted result
comparison = pd.DataFrame({'Actual Result': y_test.reset_index(drop = True), 'Predicted Result': prediction})
print(comparison.head())