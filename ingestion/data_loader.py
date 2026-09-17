import pickle

def load_data():
    with open("data/dataset.pkl", "rb") as f:
        data = pickle.load(f)

    # Clean dataset
    cleaned_data = []
    for d in data:
        text = str(d).replace("{product_purchased}", "product")
        cleaned_data.append(text)

    return cleaned_data
