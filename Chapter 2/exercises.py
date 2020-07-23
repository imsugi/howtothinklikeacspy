print(5 ** 2)  # 25
print(9 * 5)  # 45
print(15 / 12)  # 1,3
print(12 / 15)
print(15 // 12)
print(12 // 15)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)

# time
time_now = input("time now ")
alarm = input("x hours to remind ")

wake_at = int(time_now) + int(alarm)
real_time = wake_at % 24
print(real_time)

# day
sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

input_day = input("starting day? ")
how_long = input("how long? ")

day = (int(input_day) + int(how_long)) % 7


def day_name(day):
    if day == 0:
        print('sunday')
    elif day == 1:
        print('monday')
    elif day == 2:
        print('tuesday')
    elif day == 3:
        print('wednesday')
    elif day == 4:
        print('thursday')
    elif day == 5:
        print('friday')
    else:
        print('satuday')


day_name(day)

p = input("inital amount ")
p = int(p)
r = input("annoual nominal interest ")
r = int(r) / 100
n = input("number of interest is compounded per year ")
n = int(n)
t = input("number of years ")
t = int(t)

a = p * (1 + (r/n))**(n*t)

print(a)

# temperature

celcius = input("celcius ")
celcius = int(celcius)
fahrenheit = (celcius * (9/5)) + 32

print(fahrenheit)
