number=[50,40,70,90,105,150,200];
largest=number[0];
second_largest=number[0];
for i in range(1,len(number)):
    if number[i]>largest:
        second_largest=largest;
        largest=number[i];
    elif number[i]>second_largest and number[i]!=largest:
        second_largest=number[i];
print("largest number is:", largest)
print("second largest number is:", second_largest)