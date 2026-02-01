

from src.preprocessing import build_preprocessor

def test_preprocessor():
    preprocessor = build_preprocessor()
    assert preprocessor is not None