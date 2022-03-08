#FileNotFound

# try:
#     file = open("file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("something")
# except KeyError as error:
#     print(f"The key {error} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is an error that I made")

height = float(input("Height: "))
weight = int(input("Weight: "))
if height>3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height **2
print(bmi)