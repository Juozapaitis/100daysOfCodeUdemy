
#FileNotFoundError
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError


height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Human height should not be over 3 meters")
    
bmi = weight / height ** 2
print(bmi)

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

