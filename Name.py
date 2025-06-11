import random

def randomstudent():
    list = ["William","Barbara","Sothara","Ponbleu"]
    print(random.choice(list))
   
randomstudent()

def percentagecalculation(percentage, value):
    return (percentage * value) / 100
   
print(percentagecalculation(20,80))
