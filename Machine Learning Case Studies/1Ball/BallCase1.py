from sklearn import tree
import time

def BallPredictor(weight,surface):
    #Rough = 1
    #Smooth = 0
    Features =[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    #Tennis = 1
    #Cricket = 2
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    #Deciding Training Model
     
    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Features,Labels)

    print(obj.predict([[weight,surface]]))
    return obj.predict([[weight,surface]])


def main():
    print("----------Ball Predictor Case Study----------")
    print("Enter the weight of your Object in grams :")
    weight = int(input())
    print("Enter the type of surface of your object (Rough /Smooth)")
    surface = input()
    if surface.lower()=="rough":
        surface = 1
    elif surface.lower()=="smooth":
        surface = 0
    else :
        print("Invalid type of Surface ")
        exit()

    Ball = BallPredictor(weight,surface)
    if Ball == 1 :
        print("Your Object looks like Tennis Ball")
    else :
        print("Your Object looks like Cricket Ball")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total Time Required is ",end_time-start_time)