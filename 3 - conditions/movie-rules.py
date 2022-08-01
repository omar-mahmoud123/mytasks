age=int(input())
if age>17:
    print("You can watch any movie")
elif age>13:
    print("You can watch PG-Rating or G-Rating movies")
elif age<0:
    print("Error")
else:
    print("You can only watch G-rating movies")