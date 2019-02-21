import random

team_name = 'Unicorns'
strategy_name = 'random number 1-3 inclusive. 2 are collude, 1 is betray. If score is < -1,500 or they betrayed in the last 2 games:random number 1-3 inclusive.  2 are betray 1 is collude'

strategy_description = 'Only a random number generator can keep people on their toes. We want it to not be completely random though. By tilting the odds towards betray or collude, we have a solid strategy while eliminating human error.'

def move(my_history, their_history, my_score, their_score):
  choice = random.randint(1,3)
  if len(my_history) == 0:
    return 'c'
  while my_score <= -1000:
    if choice == 1:
      return 'c'
    else:
      return 'b'

  if their_history[-1] == 'b':
    choice = random.randint(1,3)
    if choice == 1:
      return 'c'
    else:
      return 'b'
    
  
  elif choice == 3:
    return 'b'
  else:
    return 'c'
  
