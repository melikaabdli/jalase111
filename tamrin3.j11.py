#تمرین سوم
#یه خط برنامه که اعداد بین 0 تا 100 که به 5 یا 6 بخش پذیر هستند
thenumber =[x for x in range(101)if x%5 == 0 or x%6==0]
print(thenumber)
