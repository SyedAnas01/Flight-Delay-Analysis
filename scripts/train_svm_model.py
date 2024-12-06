import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load data
data = pd.read_csv('data/processed_data/combined_data.csv')

# Preprocess data
X = data[['dep_delay', 'arr_delay']]
y = data['delayed'].apply(lambda x: 1 if x == 'Y' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM model
model = SVC()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
import joblib
joblib.dump(model, 'models/svm_model.pkl')
