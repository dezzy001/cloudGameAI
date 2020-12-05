
# Game -------------------


# Player -----------------
class Player:
  def __init__(self, id):
    self.id = id
    self.score = 0

  def setScore(self, score):
    self.score = score

  def getScore(self):
    return self.score


  def getBoardItemTui(self):
    return "[ P{} ]".format(self.id)

# Board ------------------

def generateNewBoard():
  board = [
    [1,"P",2],
    ["P",3,"P"],
    [2,"P",1]
    ]
  return board

# def movePlayers():
  

# TUI ------------------

def getBoardStateTui(board):
  boardTui = ""
  for row in board:
    for item in row:
      boardTui += getBoardItemTui(item)
    boardTui += "\n"
  return boardTui

def getBoardItemTui(item):
  if isinstance(item, int):
    return "[ {}  ]".format(item)
  else:
    # Player
    return "[ {}  ]".format(item)


# TEST -----------------

player1 = Player(1)

print(player1.getBoardItemTui())

board = generateNewBoard()

boardTui = getBoardStateTui(board)

print(boardTui)