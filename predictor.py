import joblib
import pandas as pd

# Load the trained model only once
model = joblib.load("model.pkl")


def predict_crop(
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
):
    """
    Predict crop using the locally trained model.
    """

    input_data = pd.DataFrame([{
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    prediction = model.predict(input_data)[0]

    return prediction


if __name__ == "__main__":

    crop = predict_crop(
        N=90,
        P=42,
        K=43,
        temperature=20.8,
        humidity=82,
        ph=6.5,
        rainfall=202.9
    )

    print("Predicted Crop:", crop)