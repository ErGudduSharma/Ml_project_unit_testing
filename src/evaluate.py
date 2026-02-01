
from sklearn.metrics import accuracy_score
from src.train import train_model

def evaluate():
    model, X_test, y_test = train_model()
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy: {acc:.4f}")
    return acc

if __name__ == "__main__":
    evaluate()