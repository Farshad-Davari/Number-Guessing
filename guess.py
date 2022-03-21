import random as r

class Guess:

  def __init__(self, computerNum, userNum, flag, score, iteration=20):
    self.computerNum = computerNum
    self.userNum = userNum
    self.flag = flag
    self.score = score
    self.iteration = iteration

  def generateComputerNumber(self):
    self.computerNum = r.randint(1, 10)

  def userChoice(self):
    self.userNum = int(input("Guess your number: "))
    return self.userNum

  def compare(self):
    if self.userNum == self.computerNum:
      self.flag = True
    else:
      self.flag = False   

  def game(self):
    self.score = 5
    print(f"Your Current Score is {self.score}")
    for i in range(self.iteration):
      self.generateComputerNumber()
      self.userChoice()
      self.compare()
      if self.flag == True:
        print("Congratulations!")
        self.score += 5
        print(self.score)
      else:
        print("Wroung Answer!")
        self.score -= 5
        print(self.score)
              