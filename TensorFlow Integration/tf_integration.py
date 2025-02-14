# tf_integration.py
import tensorflow as tf
from tf_model import create_model, load_model

def train_and_evaluate_model(model, x_train, y_train, x_test, y_test, epochs=5):
    """Trains and evaluates a TensorFlow model.

    Args:
        model: The TensorFlow model to train.
        x_train: Training data.
        y_train: Training labels.
        x_test: Testing data.
        y_test: Testing labels.
        epochs: Number of training epochs.

    Returns:
        tuple: (trained_model, evaluation_results)
    """
    model.fit(x_train, y_train, epochs=epochs)
    evaluation_results = model.evaluate(x_test, y_test, verbose=0)
    return model, evaluation_results

def prepare_mnist_data():
    """Prepares the MNIST dataset for training."""
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32') / 255
    x_test = x_test.reshape(10000, 784).astype('float32') / 255
    y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)
    return x_train, y_train, x_test, y_test

if __name__ == '__main__':
    # Example usage:
    x_train, y_train, x_test, y_test = prepare_mnist_data()
    model = create_model()
    trained_model, evaluation_results = train_and_evaluate_model(model, x_train, y_train, x_test, y_test)
    print("Model trained successfully.")
    print(f"Evaluation results: Loss = {evaluation_results[0]}, Accuracy = {evaluation_results[1]}")
