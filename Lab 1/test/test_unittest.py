import unittest
from src.data_loader import load_data
from src.model import train_model, evaluate_model

class TestIrisModel(unittest.TestCase):

    def test_data_loading(self):
        X_train, X_test, y_train, y_test = load_data()
        self.assertGreater(len(X_train), 0)
        self.assertGreater(len(X_test), 0)

    def test_model_accuracy(self):
        X_train, X_test, y_train, y_test = load_data()
        model = train_model(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test)
        self.assertGreaterEqual(accuracy, 0.7)

if __name__ == "__main__":
    unittest.main()
