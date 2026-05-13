def validate_dataset_integrity(X, y):
    if len(X) != len(y):
        raise ValueError(f"Mismatch: X has {len(X)} samples, y has {len(y)}")
    if X.shape[1:] != y.shape[1:]:
        raise ValueError("Spatial dimensions of X and y must match")
    return True