

from src.dataloader import load_data
from src.config import DATA_PATH

def test_load_data():
    df = load_data(DATA_PATH)
    assert df.shape[0] > 0