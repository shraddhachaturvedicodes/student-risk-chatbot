AI Productivity Coach & Student Risk Classifier

An AI-powered RESTful chatbot built with Flask that predicts whether a student is at academic risk and provides personalized productivity recommendations. The model uses a trained Random Forest classifier and is designed for educational support systems or student dashboards.

Features -
- Predicts whether a student is at academic risk (binary classification)
- Trained using scikit-learn on labeled academic datasets
-  Provides dynamic, personalized study or productivity suggestions
-  Modular logic engine to support multiple user intents ("learn", "optimize", etc.)
- REST API endpoint for real-time predictions using JSON input
- Easily extendable for additional features or    frontend integration

 Tech Stack - 
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas, joblib
- **API Communication:** REST, JSON
- **Model:** Random Forest Classifier

Project Structure - 
chatbot/
1.  flask_app.py # Main Flask app and API endpoint backend 
2. chat_logic.py # Routes user input to logic modules
3. analysis includes model_trainer.py # Training    and saving the ML model
4. requirements.txt # Python dependencies
5. config.json # Configuration
