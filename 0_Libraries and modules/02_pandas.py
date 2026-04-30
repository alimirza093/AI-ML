import pandas as pd

# Load the dataset
data_set = pd.read_csv("data/police.csv")


# Display first five rows
print("First 5 rows:",data_set.head())
# Display last five rows
print("Last 5 rows:",data_set.tail())
# Display a random column
print("Driver Genders:",data_set["driver_gender"])