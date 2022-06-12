is_magician = False
is_expert = False

if is_magician and is_expert:
    print('You are master magician!')
elif not is_magician:
    print('You need to learn magic')
elif is_magician and not (is_expert):
    print('Atleast you trying!')
