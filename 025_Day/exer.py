# with open("Weather_data.csv") as data_file:
#     data_list = data_file.readlines()
# print(data_list)

# import csv
#
# with open("Weather_data.csv") as data_file:
#     data = csv.reader(data_file, delimiter=";")
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas
data = pandas.read_csv("Weather_data.csv", delimiter=";")
# print(type(data))
# print(type(data["temp"]))
#
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# sum = 0
# for i in temp_list:
#     sum = sum + i
#     ave = sum / len(temp_list)
#
# print(ave)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
#
# print(data.day)


#get data in row
# print(data[data.day == "Monday"].condition)
# print(data[data.temp == data.temp.min()])
# monday = data[data.day == "Monday"]
# print(monday.temp*33.8)

data_dic = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76,56,65]
}

data_student =pandas.DataFrame(data_dic)
print(data_student)
data_student.to_csv("data_student.csv")