import random
####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####import random

# current issues with the code == definitions aren't defined
team_name = 'Null'
strategy_name = 'So if they collude, then we shall collude. If they betray, we shall also betray. However if they have a repeated history of colluding we shall betray. However if there is no definitive pattern we shall betray.'
strategy_description = 'Carefully analyze each decision to win.'


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
     #my_history: a string with one letter (c or b) per round that has been played with this opponent.
     #their_history: a string of the same length as history, possibly empty.
     #The first round between these two players is my_history[0] and their_history[0].
     #The most recent round is my_history[-1] and their_history[-1].


    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
   # my_history = ''
    # their_history = ''
    #The decision making process.
   
    if len(my_history) == 0:
      choices = ['c','b']
      return random.choice(choices)
    elif their_history[-1] == 'b':
      return 'b'
    elif their_history[-1:] == 'cccc':
      return 'b'
    elif their_history[-1:] == 'c':
      return 'c' 
    else:
      return 'b'
