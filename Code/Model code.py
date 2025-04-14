import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
from keras.callbacks import EarlyStopping


# ===============================
# 1. Load and Preprocess the Dataset
# ===============================
data = pd.read_csv("C:/Skin care assistant/MATLAB/Classification/Synthetic_SkinCare_Dataset_Complete.csv")

# Select input features and labels (labels are strings like "Low_Low_Low_Low")
features = data[['UV', 'Moisture', 'Oil', 'Temperature']].values
labels = data['RecClass'].values

# Normalize the features to [0,1]
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

# Encode labels to numeric values (they are strings)
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)
num_classes = len(np.unique(labels_encoded))
y_cat = to_categorical(labels_encoded, num_classes)

# Split dataset into training and test sets (stratified to maintain balance)
X_train, X_test, y_train, y_test = train_test_split(
    features, y_cat, test_size=0.2, random_state=42, stratify=labels)

# ===============================
# 2. Build the Classification Model
# ===============================
from tensorflow.keras import Input

model = Sequential()
model.add(Input(shape=(4,)))
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Define EarlyStopping callback
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True,
    verbose=1
)

# Train the model with early stopping
history = model.fit(
    X_train, y_train,  # Already one-hot encoded
    validation_data=(X_test, y_test),
    epochs=50,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)


# Evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\n✅ Test Accuracy: {acc * 100:.2f}%")

# (Optional) Plot learning curves
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], 'bo-', label='Validation Accuracy')
plt.plot(history.history['val_accuracy'], 'go-', label='Train Accuracy')
plt.title('Accuracy vs Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], 'bo-', label='Validation Loss')
plt.plot(history.history['val_loss'], 'go-', label='Train Loss')
plt.title('Loss vs Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()





