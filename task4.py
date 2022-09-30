# 4.Реализуйте алгоритм перемешивания списка.

list = [10, 6, 85, 38, 1, 9, 567]
import random
print ("Исходный список: " + str(list))
 
for i in range(len(list)-1, 1, - 1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]     
print ("Отсортированный список : " +  str(list))