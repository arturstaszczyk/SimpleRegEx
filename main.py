from engine import Engine

e = Engine()

result = e.find("alibaba", "[bali]+")
print result

result = e.find("alibaba", "i(ba)+")
print result

result = e.find("alibaba", "(ba)+")
print result

result = e.find("alibaba", "(ba)?")
print result

result = e.find("libaba", "b*a+")
print result