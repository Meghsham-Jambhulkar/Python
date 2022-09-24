print(" ")
print("-----Marvellous Infosytems by Piyush Khairnar-----")
print(" ")
print("Demonstration of Types of Function Arguments")
print(" ")
#Position arguments
def Batches1(name,fees):

    print("Batch name is :",name)
    print("Fees are",fees)

print("1.Demonastration of Position Arguments ")

Batches1('Python',16500)
Batches1(15000,'Angular')
print(" ")
#keyword Arguments

def Batches2(name,fees):

    print("Batch name is :",name)
    print("Fees are",fees)

print("2.Demonastration of Keyword Arguments ")

Batches2(name='PPA',fees=16500)
Batches2(fees=15000,name='LB')
print(" ")
#Default Arguments
def Batches3(name,fees = 15000):

    print("Batch name is :",name)
    print("Fees are",fees)

print("3.Demonastration of Default Arguments ")

Batches3('Angular',16500)
Batches3('Angular')
Batches3(fees=9000,name='PPA')
Batches3(name='LB')