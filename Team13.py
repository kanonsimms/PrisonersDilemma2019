#teamname:The Nexus Renegades
#members:Orion Milly, Solbi Jung

####
#teamname:The Nexus Renegades
#
#
#
####
import random 

team_name = 'The Nexus Renegades'
strategy_name =  'Restless Rebellion'
strategy_description = '#1 Always betray(rebell!!!) unless we never had a turn, or have have a safe ground of 800 point because the max points we can get off because of "c" is 800. Since it is hard to get any postive point.'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
      return 'c'
    elif their_history[-1] == 'b':
      return 'b'
    elif their_history[-1] == 'c':
      return 'b'
    elif my_score >= 800:
      return 'c'
    else:
      return 'c'
