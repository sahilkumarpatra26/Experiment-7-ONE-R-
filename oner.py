import pandas as pd

rainfall = ['High', 'High', 'High', 'Low', 'Low', 'Low']
soil_type = ['Loamy', 'Sandy', 'Clay', 'Loamy', 'Sandy', 'Clay']
yield_data = ['good', 'good', 'good', 'poor', 'poor', 'good']


def one(df):
    col = list(df.columns)
    target = col[-1]
    length = len(df[target])

    respen = None
    res = ""

    for i in col[:-1]:
        CurrError = 0
        CurrCol = set(df[i])

        for j in CurrCol:
            temp = df[df[i] == j][target].value_counts()

            if len(temp) > 0:
                CurrError += temp.sum() - temp.max()

        if respen is None:
            respen = CurrError / length
            res = i

        elif CurrError / length < respen:
            respen = CurrError / length
            res = i

    print(f"The feature {res} is selected with error rate of {respen*100:.2f}%")


data = {
    'rainfall': rainfall,
    'soil_type': soil_type,
    'yield': yield_data
}

df = pd.DataFrame(data)

one(df)