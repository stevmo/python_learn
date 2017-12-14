def person(name, *args, city, job):
	print(name, args, city)

def shit(name,*,city,job):
	print(name,city,job)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1,2)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


person('Steve', *[1,2,2], city = 'shanghai',job='developer')