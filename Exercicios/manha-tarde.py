#baseado na hora fala bom dia, boa tarde etc

hour_now = input("Please tell me what time is it: ")

if (hour_now.isalpha() is True):
    print("this is alpha")

if (hour_now[0:2])< "12":
    print(f"Good morning! This is {hour_now[0:2]}:{hour_now[-1:-3]}")
elif (hour_now[0:2] >= "12" and hour_now[0:2] < "18"):
    print(f"Good afternoon! This is {hour_now[0:2]}:{hour_now[-1:-5]}")
elif (hour_now[0:2]) >= "18":
    print(f"Good evening! This is {hour_now[0:2]}:{hour_now[-1:-3]}")