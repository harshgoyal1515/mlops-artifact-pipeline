import joblib
from sklearn.linear_model import LogisticRegression
from src.utils import load_config, load_data

def main():
    config = load_config()
    X, y = load_data()

    model = LogisticRegression(
        C=config["C"],
        solver=config["solver"],
        max_iter=config["max_iter"]
    )
    model.fit(X, y)

    joblib.dump(model, "model_train.pkl")
    print("Model trained and saved as model_train.pkl")

if __name__ == "__main__":
    main()
