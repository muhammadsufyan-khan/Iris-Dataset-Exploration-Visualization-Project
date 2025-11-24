# 🌸 Iris Dataset Exploration & Visualization Project

## 📌 Overview

This project performs **complete exploratory data analysis (EDA)** on the classic **Iris Dataset** using Python, Pandas, Matplotlib, and Seaborn. It includes data loading, inspection, summary statistics, and visualizations such as scatter plots, histograms, box plots, and pair plots.

This repository is ideal for:

* Students learning Data Science
* Beginners practicing EDA
* GitHub portfolio projects
* Python visualization practice


## 📂 Project Structure

```
Iris-EDA-Project/
│
├── README.md                # Project documentation
├── iris_eda.ipynb           # Google Colab compatible notebook
└── iris_eda.py              # Python script version of the analysis
```


## ✨ Features

✔ Load and inspect Iris dataset
✔ Display shape, columns, first rows
✔ Generate summary statistics
✔ Scatter plots to show relationships
✔ Histograms for distribution analysis
✔ Box plots to identify outliers
✔ Pairplot (multi-dimensional visualization)


## 📦 Dependencies

Install these before running:

```bash
pip install pandas seaborn matplotlib
```


## ▶️ How to Run

### **Option 1: Google Colab (Recommended)**

Upload `iris_eda.ipynb` to Colab and run all cells.

### **Option 2: Local System**

Run the Python script:

```bash
python iris_eda.py
```


## 🧪 Code Used in This Project

Below is the **complete single-cell code** used in Google Colab:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
```


## 📸 Visual Outputs

This project generates the following visualizations:

* Scatter Plot (with species color coding)
* Histogram
* Box Plot
* Pair Plot


## 🤝 Contributing

Feel free to contribute:

* Add more visualizations
* Add machine learning classification models
* Improve documentation


## 📜 License

This project is licensed under the **MIT License**.


## ⭐ Show Support

If you like this project, consider giving it a **star ⭐ on GitHub**!

