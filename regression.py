import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Importing data from the CSV file
df = pd.read_csv("https://course-resources.minerva.edu/uploaded_files/mu/00294344-8770/udemy-courses-sample.csv")

# Define dependent and independent variables
X = df.iloc[:, [4, 6, 7, 8, 9, 11]]
y = df.iloc[:, 5]

# Initialize label encoders
labelencoder = LabelEncoder()
onehotencoder = OneHotEncoder(drop='first')

# Fit and transform the label encoder for each categorical column
X['level'] = labelencoder.fit_transform(X['level'])
X['subject'] = labelencoder.fit_transform(X['subject'])
X = onehotencoder.fit_transform(X).toarray()
# return X without the inital column but the newly added columns 
X = X[:, 1:]
# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0) 
# create line of regression and train data
regressor =  LinearRegression()
regressor.fit(X_train,y_train)
# test trained model by predicitng results for X test
y_pred = regressor.predict(X_test)
# compare prediction with actual results - y_test using r2 score
print(r2_score(y_test, y_pred))

# GPT suggestion 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Importing data from the CSV file
df = pd.read_csv("https://course-resources.minerva.edu/uploaded_files/mu/00294344-8770/udemy-courses-sample.csv")

# Define dependent and independent variables
X = df[['level', 'num_subscribers', 'num_reviews', 'num_lectures', 'price', 'content_duration']]
y = df['num_reviews']

# Initialize OneHotEncoder for specific columns
onehotencoder = OneHotEncoder(drop='first', sparse=False)

# Transform the label encoder for the 'level' column
X_level_encoded = onehotencoder.fit_transform(X[['level']])

# Concatenate the encoded 'level' column with other numerical columns
X_encoded = pd.concat([pd.DataFrame(X_level_encoded), X.drop('level', axis=1)], axis=1)

# Create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=0)

# Create a linear regression model, fit with training data, and predict on test data
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Evaluate the model's performance with R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared score:", r2)
