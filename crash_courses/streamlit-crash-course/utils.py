import pandas as pd
from numpy.random import default_rng


def random_df(rows=20, cols=3):

    rng = default_rng(0)

    columns = [chr(65 + i) for i in range(cols)]

    df = pd.DataFrame(
        rng.standard_normal((rows, cols)),
        columns=columns
    )

    return df


def people_df():

    data = {
        "Name": [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Frank",
            "Grace",
        ],
        "Age": [20, 25, 30, 35, 40, 45, 50],
    }

    return pd.DataFrame(data)