numbers=[22,45,67,88,90,28,100,47,95,37];
count=0;
for number in numbers:
    if number % 2==1:
      count=count+1;
print("The number of odd numbers =",count)