team_name = 'Team10'
strategy_name = 'When they betray, we automatically betray.'
strategy_description = 'If the opponents length of their history is less than or equal to 21, 21 moves later we betray. If the opponent has four betrays in a row, we betray, if not we collude. '

def move(my_history, their_history, my_score, their_score):
  if len(their_history) >= 21 and their_history[-21] == 'b':
    return 'b'
  if 'bbbb' in their_history:
    return 'b'
  else:
    return 'c'

