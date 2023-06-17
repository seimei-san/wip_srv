who_to_do_label  = ['who to do: ', 11]
by_when_label  = ['by when: ', 9]
from_when_label  = ['from when: ', 11]
until_when_label  = ['until when: ', 12]
what_to_do_label  = ['what to do: ', 12]
at_where_label  = ['at where: ', 10]
in_where_label  = ['in where: ', 10]
from_where_label  = ['from where: ', 12]
to_where_label  = ['to where: ', 10]
how_to_do_label  = ['how to do: ', 11]
how_much_label  = ['how much: ', 10]
how_many_label  = ['how many: ', 10]
why_label  = ['why: ', 5]

def ai_msg_parser(msg_ai):
  msg_lower = msg_ai.lower()
  msg_lower_len = len(msg_lower)
  who_to_do = msg_ai[msg_lower.find(who_to_do_label[0]) + who_to_do_label[1]: msg_lower.find(by_when_label[0])]
  by_when = msg_ai[msg_lower.find(by_when_label[0]) + by_when_label[1]: msg_lower.find(from_when_label[0])]
  from_when = msg_ai[msg_lower.find(from_when_label[0]) + from_when_label[1]: msg_lower.find(until_when_label[0])]
  until_when = msg_ai[msg_lower.find(until_when_label[0]) + until_when_label[1]: msg_lower.find(what_to_do_label[0])]
  what_to_do = msg_ai[msg_lower.find(what_to_do_label[0]) + what_to_do_label[1]: msg_lower.find(at_where_label[0])]
  at_where = msg_ai[msg_lower.find(at_where_label[0]) + at_where_label[1]: msg_lower.find(in_where_label[0])]
  in_where = msg_ai[msg_lower.find(in_where_label[0]) + in_where_label[1]: msg_lower.find(from_where_label[0])]
  from_where = msg_ai[msg_lower.find(from_where_label[0]) + from_where_label[1]: msg_lower.find(to_where_label[0])]
  to_where = msg_ai[msg_lower.find(to_where_label[0]) + to_where_label[1]: msg_lower.find(how_to_do_label[0])]
  how_to_do = msg_ai[msg_lower.find(how_to_do_label[0]) + how_to_do_label[1]: msg_lower.find(how_much_label[0])]
  how_much = msg_ai[msg_lower.find(how_much_label[0]) + how_much_label[1]: msg_lower.find(how_many_label[0])]
  how_many = msg_ai[msg_lower.find(how_many_label[0]) + how_many_label[1]: msg_lower.find(why_label[0])]
  why = msg_ai[msg_lower.find(why_label[0]) + why_label[1]: msg_lower_len]
  print(who_to_do)
  print(by_when)
  print(from_when)
  print(until_when)
  print(what_to_do)
  print(at_where)
  print(in_where)
  print(from_where)
  print(to_where)
  print(how_to_do)
  print(how_much)
  print(how_many)
  print(why)



tmp = "who to do: none by when: 金曜日の１２：３０までに (by Friday at 12:30) from when: none until when: none what to do: APIの課題をしてください (do the API assignment) at where: none in where: none from where: none to where: none how to do: none how much: none how many: none why: none"

ai_msg_parser(tmp)
