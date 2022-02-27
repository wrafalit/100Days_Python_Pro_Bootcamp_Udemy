import pandas

squirrel_data = pandas.read_csv("Squirrel_Data.csv")


# fury = squirrel_data["Primary Fur Color"].value_counts()
# print(fury)

# fury_csv = {
#     "Primary Fur Color" =
# }
# fury.to_csv("fury.csv")

fury_cynanom = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"])
fury_black = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Black"])
fury_gray = len(squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"])

data_dict = {
    "Primary Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [fury_gray, fury_cynanom, fury_black ]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("fury.csv")