
from aiogram.types import Poll, PollType

polltype = PollType()
poll1 = Poll(id =1, question ="I’m 18 and my brother is 20, so he’s........ me.", options = ['the oldest of','older than', 'as old as'] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 1 )

poll2 = Poll(id =2, question ="Carl’s very ........ . He’s never late, and he never forgets to do things. ",
             options = ['reliable','patient', 'strict'] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 0 )

poll3 = Poll(id =3, question ="We stayed in a lovely villa ........ the sea", options = ['it overlooks','overlooked', 'overlooking'] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 1 )

poll4 = Poll(id =4, question ="Not until the 1980s ........ for the average person to own a computer. ",
             options = ['it was possible' , 'was it possible', 'was possible' ] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 0 )

poll5 = Poll(id =5, question ="Jan ........ her arm on a hot iron. ", options = ['broke' ,'burned', 'sprained' ] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 1 )

poll6 = Poll(id =6, question ="Tomorrow’s a holiday, so we ........ go to work. ",
             options = ['have to', 'mustn’t', 'don’t have to' ] ,
            type = 'quiz', allows_multiple_answers = False, correct_option_id = 2 )

pollColection = []

pollColection.append(poll1)
pollColection.append(poll2)
pollColection.append(poll3)
pollColection.append(poll4)
pollColection.append(poll5)
pollColection.append(poll6)