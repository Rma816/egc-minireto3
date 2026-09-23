import pytest

from catalog import classify_model_size


def test_one_feature_is_tiny():
    assert classify_model_size(1) == "tiny"

def test_zero_features_is_invalid():
    with pytest.raises(ValueError):
        classify_model_size(0)

def classify_model_size(feature_count: int) -> str:
    if feature_count < 1:
        raise ValueError("feature_count debe ser positivo")
    return "tiny"

