from sklearn.model_selection import train_test_split

def split_ml_data(X, y, config):
    return train_test_split(
        X, y, 
        test_size=config["SPLIT_RATIO"], 
        random_state=config["RANDOM_STATE"],
        shuffle=True
    )