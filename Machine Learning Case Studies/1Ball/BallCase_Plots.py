import pandas as pd 
import matplotlib.pyplot as plt 


Excel = "BallCase.xlsx"
Data = pd.read_excel(Excel)

# print("All the Excel File :")
# print(Data)

# print("First Five Rows of the File :")
# print(Data.head())

# print("Last Five Rows of the File :")
# print(Data.tail())
print(Data.shape)

sorted_data = Data.sort_values(['Weight'],ascending=False)

print("Sorted Data : ")
print(sorted_data)

Data['Weight'].plot(kind="hist")
plt.savefig("BallCase1.png",dpi=300, bbox_inches='tight')
plt.show()

Data['Weight'].plot(kind="bar")
plt.savefig("BallCase2.png",dpi=300, bbox_inches='tight')
plt.show()

