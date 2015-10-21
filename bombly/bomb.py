from collections import defaultdict

batteries = 99
freak = 'freak'
car = 'car'
parallel = 'parallel'
serial = 'serial'
vowel = 'vowel'


def odd_serial():
    return serial in ('one', 'three', 'five', 'seven', 'nine')


def even_serial():
    return serial in ('zero', 'two', 'four', 'six', 'eight')


def sanitize_colors(words):
    print "Sanitizing: {}".format(words)
    words = words.replace('read', 'red').replace('blew', 'blue')
    words = ' '.join([word for word in words.split() if word in ('yellow', 'red', 'black', 'blue', 'white')])
    print "Sanitized: {}".format(words)
    return words


def reset_bomb():
    global batteries
    global freak
    global car
    global parallel
    global serial
    global vowel
    global counts
    global values
    global positions
    global curr_stage
    global morse_letters
    global on_first_words

    # Battery characteristics
    batteries = 99
    freak = 'freak'
    car = 'car'
    parallel = 'parallel'
    serial = 'serial'
    vowel = 'vowel'

    # Wire sequence
    counts = defaultdict(int)

    # Memory
    values = []
    positions = []
    curr_stage = 1

    # Morse
    morse_letters = []

    # On First Words
    on_first_words = []


def bomb_status():
    global batteries
    global freak
    global car
    global parallel
    global serial
    global vowel
    global counts
    global values
    global positions
    global curr_stage
    global morse_letters
    global on_first_words

    # Battery characteristics
    print 'batteries', batteries
    print 'frk', freak
    print 'car', car
    print 'parallel', parallel
    print 'serial', serial
    print 'vowel', vowel

    # Wire sequence
    print 'wire sequence', counts

    # Memory
    print 'values', values
    print 'position', positions
    print 'curr_stage', curr_stage

    # Morse
    print 'morse_letters', morse_letters

    # On First Words
    print 'on first words', on_first_words


def set_car(extras):
    global car
    car = str(extras['car'])


def set_batteries(extras):
    global batteries
    batteries = int(str(extras['batteries']))


def set_freak(extras):
    global freak
    freak = str(extras['word'])
    

def set_parallel(extras):
    global parallel
    parallel = str(extras['word'])


def set_serial(extras):
    global serial
    serial = str(extras['word'])
    

def set_vowel(extras):
    global vowel
    vowel = str(extras['word'])


def bomb_done():

    global batteries
    global freak
    global car
    global parallel
    global serial
    global vowel
    global counts
    global values
    global positions
    global curr_stage
    global morse_letters
    global on_first_words

    # Battery characteristics
    batteries = 99
    freak = 'freak'
    car = 'car'
    parallel = 'parallel'
    serial = 'serial'
    vowel = 'vowel'

    # Wire sequence
    counts = defaultdict(int)

    # Memory
    values = []
    positions = []
    curr_stage = 1

    # Morse
    morse_letters = []

    # On First Words
    on_first_words = []

    return 'I AM YOUR BOMB DEFUSING OVERLORD'
