
from aiogram.types import Poll, PollType

polltype = PollType()
poll = Poll(polltype.QUIZ)
poll.is_anonymous = True

poll.question = 'What is name'
poll.options =