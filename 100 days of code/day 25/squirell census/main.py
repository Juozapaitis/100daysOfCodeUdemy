import pandas

data = pandas.read_csv("100 days of code\\day 25\\squirell census\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey_squirels_count = len(data["Primary Fur Color"] == "Grey")
# print(grey_squirels)

# print(data["Primary Fur Color"].value_counts())

count = data.groupby(["Primary Fur Color"]).size().reset_index(name='Count')

df = pandas.DataFrame(count)
df.to_csv("100 days of code\\day 25\\squirell census\\squirrel_count.csv")