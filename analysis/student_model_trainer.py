import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

class StudentModelTrainer:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.model_path = "models/edupulse_model.h5"
        self.scaler_path = "models/scaler.save"
        self.encoder_path = "models/encoders.save"
        self.feature_order_path = "models/feature_order.save"
        self.cat_cols = ["Gender", "Education_Level", "Course_Name", "Engagement_Level", "Learning_Style"]
        self.encoders = {}
        self.scaler = StandardScaler()

    def load_and_preprocess_data(self):
        df = pd.read_csv(self.csv_path)
        if 'Student_ID' in df.columns:
            df.drop(columns=['Student_ID'], inplace=True)

        for col in self.cat_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.encoders[col] = le

        df['Dropout_Likelihood'] = LabelEncoder().fit_transform(df['Dropout_Likelihood'])
        df.drop(columns=['Forum_Participation', 'Course_Name'], inplace=True)

        X = df.drop(columns=['Dropout_Likelihood'])
        y = df['Dropout_Likelihood']
        X_scaled = self.scaler.fit_transform(X)

        return train_test_split(X_scaled, y, test_size=0.2, random_state=42), X.columns.tolist()

    def build_and_train_model(self, X_train, y_train):
        model = Sequential([
            Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
            Dropout(0.4),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer=Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, validation_split=0.2, epochs=30, batch_size=16, verbose=1)
        return model

    def save_artifacts(self, model, feature_order):
        model.save(self.model_path)
        joblib.dump(self.scaler, self.scaler_path)
        joblib.dump(self.encoders, self.encoder_path)
        joblib.dump(feature_order, self.feature_order_path)
        print("✅ All artifacts saved.")

    def run(self):  #preprocessing ➜ training ➜ saving
        (X_train, X_test, y_train, y_test), feature_order = self.load_and_preprocess_data()
        model = self.build_and_train_model(X_train, y_train)
        self.save_artifacts(model, feature_order)

if __name__ == "__main__":
    #trainer = StudentModelTrainer("data/sample_student_data.csv")
    trainer = StudentModelTrainer("C:/Users/HP/Downloads/chatbot/data/sample_student_data.csv")

    trainer.run()   #load data ➜ preprocess ➜ train model ➜ save