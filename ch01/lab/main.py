import random

# Part A
#OG CODE
weeks = 16
classes = 5
tuition = 12000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))

#NEW CODE
classes_per_week = (3)
print("Classes per week:", classes_per_week, type(classes_per_week)) #'var'
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, type(cost_per_class)) #'var'
print ("Cost per class:", cost_per_class, "Wow! What a great number!") #'var'

# Part B
greetings = ["Hi", "Hello", "Hey", "Ola", "Oi", "Hola"]
one_greeting = random.choice(greetings)
print(one_greeting) #'var'

