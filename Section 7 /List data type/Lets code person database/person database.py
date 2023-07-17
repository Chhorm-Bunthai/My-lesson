person1 = ['David', 20, 1, 100.0, 100.0]
person2 = ['John', 25, 1, 170.0, 70.0]
person3 = ['Jane', 22, 0, 169.0, 60.0]
person4 = ['Peter', 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
n_persons = int(len(person_list)/5)
age = person_list[1::5]
age_sum = sum(age)
average_age = float(age_sum / n_persons)
print('Average age is ' + str(average_age) + '.')
