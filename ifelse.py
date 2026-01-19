weather=input("how is weather today:")
time_of_day=input("time_of_day")
if weather=="sunny":
    print("you can play cricket.")
elif weather=="rainy" and time_of_day=="day":

    print("play with robot toy")
elif weather=="snowy":
    print("build a snowman and play with it")
elif weather=='rainy' and time_of_day=="night":
    print("go to sleep")
else:
    print("eat 5star,do nothing !!!")
print("enjoy your day !!!")
