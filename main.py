from engine import Engine
from tokenizer import Tokenizer
from evaluator import Evaluator
from matchfinder import MatchFinder


e = Engine(Tokenizer(), Evaluator(), MatchFinder())

result = e.find("aaba", 'a')
print 'Match "aaba" with "a"'
print result + '\n'

result = e.find("text", 'a')
print 'Match "text" with "a"'
print result + '\n'


result = e.find("alibaba", "[bali]+")
print 'Match "alibaba" with "[bali]+"'
print result + '\n'

result = e.find("alibaba", "i(ba)+")
print 'Match "alibaba" with "i(ba)+"'
print result + '\n'

result = e.find("alibaba", "(ba)+")
print 'Match "alibaba" with "(ba)+"'
print result + '\n'

result = e.find("alibaba", "(ba)?")
print 'Match "alibaba" with "(ba)?"'
print result + '\n'

result = e.find("libaba", "b*a+")
print 'Match "libaba" with "b*a+"'
print result + '\n'

result = e.find("libaba", "a.a")
print 'Match "libaba" with "a.a"'
print result + '\n'

result = e.findAll("alibaba", "b*a+")
print 'Match "alibaba" with "b*a+"'
print result
print '\n'

result = e.findAll("alaibaba", "a.a")
print 'Match "alaibaba" with "a.a"'
print result
print '\n'

result = e.findAll("alabama", "[a.]+a")
print 'Match "alabama" with "[a.]+a"'
print result
print '\n'

result = e.findAll("alabama", "(a.)+a")
print 'Match "alabama" with "(a.)+a"'
print result
print '\n'