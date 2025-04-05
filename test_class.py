class Student:
    def __init__(self,name,id,chinese,english,math):
        self.name=name
        self.id=id
        self.score={"chinese":0,"english":0,"math":0}
        self.score["chinese"]=chinese
        self.score["english"]=english
        self.score["math"]=math


    def setScore(self,kemu,score):
        if kemu in self.score:
            self.score[kemu]=score
        else:
            print("科目输入有误")

zhang=Student("张三","111",1,2,3)
print(zhang.score)
zhang.setScore("mth",9)
print(zhang.score)
