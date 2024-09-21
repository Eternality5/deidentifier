import pandas


def main(filename):
    df = pandas.read_csv(filename)
    pandas.set_option('display.max_rows', 500)
    df['age_range'] = pandas.cut(df['Age'], bins=[0, 25, 35, 50, 65, 100],
                                 labels=['0-25', '26-35', '36-50', '51-65', '65+'])
    df = df.drop('Age', axis=1)
    df = df.groupby(df.columns.tolist(), as_index=False, observed=True).size()
    print(df)
    print("k = ", df['size'].min())


main("bone-tumor-dataset.csv")
