import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Step 1: Load the student data 
#data_path = os.path.join('..', 'data', 'sample_student_data.csv')
data_path = os.path.join('C:/Users/HP/Downloads/chatbot', 'data', 'sample_student_data.csv')
#data_path = 'C:/Users/HP/Downloads/chatbot/data/sample_student_data.csv'
df = pd.read_csv(data_path)

# Step 2: Split features and label
X = df.drop(['Student_ID', 'Dropout_Likelihood'], axis=1)
y = df['Dropout_Likelihood']

# Step 3: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 6: Save the trained model
model_path = os.path.join('C:/Users/HP/Downloads/chatbot/analysis', 'models', 'predictor.pkl')
joblib.dump(model, model_path)
print(f"Model saved to: {model_path}")
