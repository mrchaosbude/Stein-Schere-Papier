import random
import tables

var rock = {"rock": 1, "paper": 0, "scissors": 2}.toTable
var paper = {"rock": 2, "paper": 1, "scissors": 0}.toTable
var scissors = {"rock": 0, "paper": 2, "scissors": 1}.toTable

proc ask: Table[string, int] =
  echo( "Choose your action:")
  echo( "       [1] Rock")
  echo( "       [2] Paper:")
  echo( "       [3] Scissors:")
  while true:
    write(stdout, "-> ")
    case readLine(stdin)
    of "1":
      return rock
    of "2":
      return paper
    of "3":
      return scissors
    else: echo("Please be clear")

var history = {"won": 0, "lost": 0, "draw": 0}.toTable

while true:
    randomize()
    let cpu = sample(["rock", "paper", "scissors"])
    let answare = ask()
    
    case answare[cpu]:
    of 0:
      echo ("Unfortunately lost ಠ╭╮ಠ , would you like another round? (y/n)")
      history["lost"] += 1
    of 1:
      history["draw"] += 1
      echo (r"Unfortunately a draw ¯\_(ツ)_/¯ , would you like another round ? (y/n)")
    of 2:
      history["won"] += 1
      echo ("Won (づ｡◕‿‿◕｡)づ , would you like another round ? (y/n)")
    else: 
      echo("impossible")
    echo("")
    #echo history
    var run = true
    
    while run:
      write(stdout, "-> ")
      case readLine(stdin)
      of "y", "Y", "yes", "Yes":
        run = false
      of "n", "N", "no", "No":
        echo "You Won: ",history["won"]," Lost: ",history["lost"], " Draw: ", history["draw"]
        echo ("goodbye until next time!!")
        quit()
      else: echo("Please be clear: yes or no")
