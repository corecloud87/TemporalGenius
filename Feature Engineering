
# Extract features and target variable
X = df[['duration', 'priority']]
y = df['completion_time']

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
