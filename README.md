# Machine-Learning-Model-Implementation

Company: CODTECH IT SOLUTIONS

Name: UDATA JOSEPH KISHORE

Intern ID: CTIS7316

Domain: PYTHON PROGRAMMING

Duration: 4 Weeks

Mentor: NEELA SANTOSH KUMAR

Task Description:

I've used Pycharm for programming. Task Title: Machine Learning Model Implementation. To implement the machine learning model I've choosed the topic Email Spam Detection which is a classification algorithm based model in which we detect that the email sent is a spam or not spam. In this code I've started by Data collection step in which I've used pandas library which I've imporeted as pd to load the dataset in the csv file. I've used read_csv() method to load and read the dataset for email spam detection and stored the data in data variable. And then I've created a dataframe for this data using DataFrame() method. And then I've printed the top 5 rows of the dataframe using head() method. And in Data Preprocessing step, for removing the null/missing values I've used dropna() method. And then I've converted the two labels spam and not spam into binary classification digits 1 and 0. And then I've converted the data into vectors by using TfidfVectorizer() library imported from sklearn.feature_extraction.text and it is stored in vectorizer variable. The Input features (numeric representation of an email) is stored in the x variable and the Output labels (spam / not spam) is stored in the y variable. And then next moved to the most important part of the model is Model selection and training. For splitting the trainging dataset and testing dataset I've used train_test_split library imported from sklearn.model_selection. By using this library I've splitted the Training and Testing dataset as x_train, x_test, y_train, y_test as training data with 80% and the testing data with 20% of the dataset. And then for model creation I've used the clkassification algorithm called LogisticRegression which classifies the data and is imported from sklearn.linear_model. And then I've imported accuracy_score and classification_report libraries for knowing how efficient and accurate the model is. Then I've created model of LogisticRegression() as model. And then to train the model I've used fit() method and the training data (x_train, y_train). And then I've moved to next step Model Evaluation and testing in which I've used testing data (x_test) to evaluate the model. By using predict() method to the x_test data, I've tested the model and stored the predicted output data in prediction variable. And then for comparing the predicted results of the model with the actual results I've used accuracy_score() method for evaluating the model accuracy by passing the parameters y_test and prediction. And then printed the accuracy of the model. And then I've created a dataframe of the comparison between the actual result and predicted result and stored it in comparison variable. And then I've printed the top 5 rows of the comparison dataframe.

Dataflow of the Code:

Loading/Reading data -> Cleaning the data -> Converting labels -> Converting text into numbers/vectors -> Splitting the dataset -> Training the model -> Testing/Evaluating the model -> Checking the model accuracy -> Comparing the results

Here the model accuracy when I've trained and tested with the dataset containing 50 emails is of 0.6 or 60% but when I've trained and tested with the dataset containing 100 emails the accuracy is of 0.95 or 95%. This means that how large the dataset will be for any model (Regression or Classification model) that large the accuracy will be. So, use the large dataset for any model that you build. And also make sure that your dataset contains no null/missing values, it may effect your model.

Output:

<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/a59518b5-e5de-4fa1-826f-6fc644868bc9" />
