# import csv

# with open("C:/Users/justa/vscode/udemy/100 days of code/day 25/weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     conditions = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             conditions.append(row[2])

#     print(temperatures)

import pandas

data = pandas.read_csv("C:/Users/justa/vscode/udemy/100 days of code/day 25/weather_data.csv")
data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"])
temp_list = data["temp"].to_list()
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(max(temp_list))
# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])