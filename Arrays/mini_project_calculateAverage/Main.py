# Created by Abdihakim

# Calculate Average Temprature
numDays = int(input("How many days' temperature?"))
totalTemp = 0
temperatures = []
for i in range(numDays):
    nextDay = int(input("Enter day" +str(i+1) + "'s highest temperature: "))
    temperatures.append(nextDay)
    totalTemp += temperatures[i]
average = round(totalTemp/numDays, 2)
print("Average temperature is: " + str(average))

aboveAverage = 0
for temperature in temperatures:
    if temperature > average:
        aboveAverage +=1
        
print(str(aboveAverage) + ' days(s) above average!')