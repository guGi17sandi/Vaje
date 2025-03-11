
temp = 28

is_sunny = False

if temp >= 28 and is_sunny:
    print ("it is HOT outside")
    print ("It is sunny")
elif temp <= 0 and is_sunny:
    print ("it is cold outside")
    print ("It is cold")
elif 28 > temp > 0 and is_sunny:
    print ("it is Warm outside")
    print ("It is Warm")

elif temp >= 28 and not is_sunny:
    print ("it is Cloudy outside")
    print ("It is Cloudy")