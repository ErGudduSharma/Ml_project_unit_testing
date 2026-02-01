
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def build_preprocessor():
    categorical_features = ["Gender"]
    numerical_features = ["Age", "EstimatedSalary"]

    categorical_transformer = LabelEncoder()

    def label_encode_column(df):
        df["Gender"] = LabelEncoder().fit_transform(df["Gender"])
        return df

    preprocessor = Pipeline(steps=[
        ("scaler", StandardScaler())
    ])

    return preprocessor