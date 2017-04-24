#Function to convert celsius to farenheit

def ctof(c):
   f = (float(c)*9)/5 + 32
   return f

#c = float(input("Enter temperature in celsius: "))

temperatures = [10, -20, -289, 100]

for i in temperatures:
#Condition for lowest possible temperature
    if i < -273.15:
        print ("Cannot convert below absolute zero")
    else:
        file = open("example.txt",'a')
        file.write(str(ctof(i))+"\n")
        file.close()
        print (ctof(i))

#celsius = input("Enter temperature in celsius: ")
#farenheit = (float(celsius) * 9)/5 + 32
#print(farenheit, "farenheit")
