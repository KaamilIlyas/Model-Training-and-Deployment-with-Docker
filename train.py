from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import pickle

# Load data (replace 'bank.csv' with your actual file path)
data = pd.read_csv('bank.csv')

# Encode categorical variables
labelencoder = LabelEncoder()
for col in data.columns:
    if data[col].dtypes == 'object':
        data[col] = labelencoder.fit_transform(data[col])

# Separate features and target variable
X = data.drop('y', axis=1)
y = data['y']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model with increased max_iter
model = LogisticRegression(max_iter=1000)  # Increased iterations
model.fit(X_train, y_train)

# Evaluate the model on the test set
predictions = model.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print('Accuracy: {}'.format(accuracy))

# Save the trained model (consider using a descriptive filename)
pickle.dump(model, open('model.pkl', 'wb'))

# Optional: Print a classification report for more detailed model evaluation
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))
