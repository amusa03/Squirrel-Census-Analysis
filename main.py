import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = data["Primary Fur Color"].value_counts()["Gray"]
cinnamon_count = data["Primary Fur Color"].value_counts()["Cinnamon"]
black_count = data["Primary Fur Color"].value_counts()["Black"]

data_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_dataframe = pandas.DataFrame(data_dict)
new_dataframe.to_csv("squirrel_count.csv")