team_name = 'Kteins Fate:0'
strategy_name = 'Do the opposite of they do'
strategy_description = 'If they collude we betray, if they betray we collude. We either die or live.'
def move(my_history, their_history, my_score, their_score):
if len(my_history) >= 1 and their_history[-1] == 'c':
return 'b'
elif len(my_history) >= 1 and their_history[-1] == 'b':
return 'c'
