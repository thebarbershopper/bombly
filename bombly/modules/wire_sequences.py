from collections import defaultdict


counts = defaultdict(int)
sequences = {
    'red': [
        ('c'),
        ('b'),
        ('a'),
        ('a', 'c'),
        ('b'),
        ('a', 'c'),
        ('a', 'b', 'c'),
        ('a', 'b'),
        ('b')
    ],
    'blue': [
        ('b'),
        ('a', 'c'),
        ('b'),
        ('a'),
        ('b'),
        ('b','c'),
        ('c'),
        ('a', 'c'),
        ('a')
    ],
    'black': [
        ('a', 'b', 'c'),
        ('a', 'c'),
        ('b'),
        ('a', 'c'),
        ('b'),
        ('b', 'c'),
        ('a', 'b'),
        ('c'),
        ('c')
    ],
}


def wire_sequence(extras):
    global sequences
    words = str(extras['words'])
    print words
    words = words.replace('read', 'red').replace('blew', 'blue')
    print words
    words = [word for word in words.split() if word in ('red', 'blue', 'black', 'apple', 'bravo', 'charlie')]
    print words
    words = [words[x:x + 2] for x in xrange(0, len(words), 2)]
    print words
    for color, letter in words:
        print "Color: {}".format(color)
        print "Letter: {}".format(letter)
        print "Count: {}".format(counts[color])
        if letter[0] in sequences[color][counts[color]]:
            yield 'Cut'
        else:
            yield 'Dont Cut'

        counts[color] += 1


def reset_wire_sequence():
    global counts
    global sequences
    counts = defaultdict(int)
    sequences = {}
