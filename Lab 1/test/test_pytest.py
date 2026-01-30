from src.data_loader import load_data
from src.model import train_model, evaluate_model

def test_data_loading():
    X_train, X_test, y_train, y_test = load_data()
    assert X_train.shape[0] > 0
    assert X_test.shape[0] > 0

def test_model_training():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    assert accuracy >= 0.7
