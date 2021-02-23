# print("this is a sample string")

# using a comma
# name = "Zen"
# print("My name is", name)

# concatenating the string using +
# name = "Zen"
# print("My name is " + name)

# F-Strings : Python 3.6 introduced f-strings for string interpolation. 
# To construct an f-string, place an f right before the opening quotation. 
# Then within the string, place any variables within curly brackets.


#  F-Strings (Literal String Interpolation)
# ---------------------------------------
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")


#  string.format()
# ---------------------------------------

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.


#  %-Formatting
# ---------------------------------------

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27


#  Built in Strings: Title
# ---------------------------------------
x = "hello world"
print(x.title())
# output:
"Hello World"

