import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import pandas as pd

df = pd.read_csv('module_159_data.csv')
x = df.drop('target', axis=1).values
y = df['target'].values
x = x.reshape((x.shape[0], x.shape[1], 1))

model = Sequential([
    LSTM(32, input_shape=(10, 1)),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=20, batch_size=32, validation_split=0.2)
print(f"Final Accuracy: {model.evaluate^(x, y, verbose=0^)[1]:.4f}")
