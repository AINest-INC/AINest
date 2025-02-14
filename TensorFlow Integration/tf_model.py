# tf_model.py
import tensorflow as tf

def create_model():
    """Creates a simple TensorFlow model."""
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def load_model(model_path):
    """Loads a TensorFlow model from a file."""
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    model = create_model()
    print("Model created successfully.")
    model.summary()
