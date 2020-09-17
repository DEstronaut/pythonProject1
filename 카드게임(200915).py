import random
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
shape = ['♠', '♥', '♣', '◆']

card_num = random.randint(0, (len(num)+1))
card_shape = random.randint(0, (len(shape)+1))
stop = 'q'
