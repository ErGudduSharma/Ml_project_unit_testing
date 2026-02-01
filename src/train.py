
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from src.config import DATA_PATH, TEST_SIZE, RANDOM_STATE
from src.dataloader import load_data
from src.model import get_model
from src.preprocessing import build_preprocessor

def train_model():
    df = load_data(DATA_PATH)

    df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

    X = df.drop(columns = ["Purchased", "User ID"])
    y = df["Purchased"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = TEST_SIZE, random_state = RANDOM_STATE
    )

    pipeline = Pipeline(steps = [
        ("scaler", build_preprocessor()),
        ("model", get_model())
    ])

    pipeline.fit(X_train, y_train)

    return pipeline, X_test, y_test


if __name__ == "__main__":
    model, _, _ = train_model()
    print("✅ Model training completed successfully")