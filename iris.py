import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Load dataset
    df = sns.load_dataset("iris")

    print("Shape of Dataset:", df.shape)
    print("Column Names:", df.columns.tolist())
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())

    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
    plt.title("Scatter Plot: Sepal Length vs Petal Length")

    plt.subplot(2, 2, 2)
    sns.histplot(df["sepal_length"], kde=True)
    plt.title("Histogram: Sepal Length Distribution")

    plt.subplot(2, 2, 3)
    sns.boxplot(data=df.drop(columns=["species"]))
    plt.title("Box Plot of Numerical Features")

    sns.pairplot(df, hue="species")
    plt.suptitle("Pair Plot of Iris Dataset", y=1.02)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
