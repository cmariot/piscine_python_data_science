ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second [1] etc.
ft_list[1] = "World!"


# Tuple items are ordered, unchangeable, and allow duplicate values.
ft_tuple = ("Hello", "France!")


# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will
# appear.
ft_set.remove("tutu!")
ft_set.add("Paris!")


# Dictionary items are ordered, changeable, and does not allow duplicates.
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
