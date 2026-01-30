from src.data_loader import load_data
from src.model import train_model, evaluate_model

def main():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)

    print(f"Model Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
