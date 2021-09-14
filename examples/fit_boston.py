from sklearn.datasets import load_boston
from dask_ml.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.pipeline import Pipeline
from utils import get_param_strings_from_pipe, create_column_selector_options
import pandas as pd


df = pd.read_csv(load_boston()['filename'], header=1)

X, y = df.drop(['MEDV'], axis=1), df['MEDV']

column_options = [['CRIM', 'ZN'], ['CRIM'], ['AGE', 'DIS']]

ct = ColumnTransformer([('selector', 'passthrough', ['CRIM', 'ZN'])])

ct.get_params()['transformers']

ct.set_params(transformers=[('selector', 'passthrough', ['CRIM'])])

lr = LinearRegression()

pipe = Pipeline([
    ('column_selector', ct), 
    ('linear_regression', lr)
])

pipe.set_params(column_selector__transformers=[('selector', 'passthrough', ['CRIM'])])

get_param_strings_from_pipe(pipe)

selector_options = create_column_selector_options(column_options)

gscv = GridSearchCV(
    pipe,
    param_grid={
        # 'column_selector__n_jobs': [2],
        'column_selector__transformers': selector_options
    }
)

gscv.fit(X, y)

print(f"Best estimator: {gscv.best_estimator_}")
