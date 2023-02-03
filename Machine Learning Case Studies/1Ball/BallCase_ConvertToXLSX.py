import pandas as pd


#Rough = 1
#Smooth = 0
#Tennis = 1
#Cricket = 2
Data = [[35,"Rough","Tennis"],[47,"Rough","Tennis"],[90,"Smooth","Cricket"],[48,"Rough","Tennis"],[90,"Smooth","Cricket"],[35,"Rough","Tennis"],[92,"Smooth","Cricket"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[96,"Smooth","Cricket"],[43,"Rough","Tennis"],[110,"Smooth","Cricket"],[35,"Rough","Tennis"],[95,"Smooth","Cricket"],[35,"Rough","Tennis"],[47,"Rough","Tennis"],[90,"Smooth","Cricket"],[48,"Rough","Tennis"],[90,"Smooth","Cricket"],[35,"Rough","Tennis"],[92,"Smooth","Cricket"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[96,"Smooth","Cricket"],[43,"Rough","Tennis"],[110,"Smooth","Cricket"],[35,"Rough","Tennis"],[95,"Smooth","Cricket"],[35,"Rough","Tennis"],[47,"Rough","Tennis"],[90,"Smooth","Cricket"],[48,"Rough","Tennis"],[90,"Smooth","Cricket"],[35,"Rough","Tennis"],[92,"Smooth","Cricket"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[35,"Rough","Tennis"],[96,"Smooth","Cricket"],[43,"Rough","Tennis"],[110,"Smooth","Cricket"],[35,"Rough","Tennis"],[95,"Smooth","Cricket"]]
df = pd.DataFrame(Data,columns=["Weight","Surface","Sport"])
print(df)
writer = pd.ExcelWriter('BallCase.xlsx',engine='xlsxwriter')

df.to_excel(writer,sheet_name ="Sheet1")
writer.save()