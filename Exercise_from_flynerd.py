w = int(input('Pleas enter your weight: '))
h = float(input('Pleas enter your height (in centimeters): '))
age = int(input('Pleas enter your age: '))

k = 0
while k != 1:
    a = int(input('Please select a gender: \n1. Female, \n2. Male\n'))
    if a == 1:
        s = int(-161)
        k = 1
    elif a == 2:
        s = int(5)
        k = 1
    else:
        k = 0


k = 0
while k != 1:
    a = int(input(
'''Type of physical activity:
1. Sedentary work, no additional physical activity
2. Non-physical work, inactive lifestyle
3. Light physical work, regular exercise 3-4 times (about 5 hours) a week
4. Physical work, regular exercise 5 times (about 7 hours) a week
5. Hard physical work, regular exercise 7 times a week
Please select the activity number: '''))
    if a == 1:
        t = 1.2
        k = 1
    elif a == 2:
        t = 1.4
        k = 1
    elif a == 3:
        t = 1.6
        k = 1
    elif a == 4:
        t = 1.8
        k = 1
    elif a == 5:
        t = 2
        k = 1    

bmi =  w / ((h*0.01)**2)
print('Your BMI is: {}'.format(bmi))

ppm = (10*w) + (6.25*h) - (5*age) + s
dcal = ppm*t
print('daily caloric requirement: {} kcal'.format(dcal))