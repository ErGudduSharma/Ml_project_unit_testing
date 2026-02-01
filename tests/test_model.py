

from src.model import get_model

def test_model_creation():
    model = get_model()
    assert model is not None