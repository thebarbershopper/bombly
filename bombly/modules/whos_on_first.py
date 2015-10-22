# On first words
on_first_words = []


def reset_words():
    global on_first_words
    on_first_words = []


def remove_words():
    global on_first_words
    on_first_words = on_first_words[:-1]


def whos_on_first(extras):
    words = str(extras['words'])

    combos = {
        ('you', 'are', 'words'): 'you are',
        ('your', 'words'): 'you are',
        ('done',): 'done',
        ('don',): 'done',
        ('you', 'are', 'letters'): 'ur',
        ('sure',): 'sure',
        ('shore',): 'sure',
        ('you', 'word'): 'you',
        ('hold',): 'hold',
        ('you', 'letter'): 'u',
        ('yes',): 'yes',
        ('first',): 'first',
        ('display',): 'display',
        ('okay',): 'okay',
        ('OK',): 'okay',
        ('says',): 'says',
        ('nothing',): 'nothing',
        ('literally', 'blank'): ' ',
        ('blank',): 'blank',
        ('no',): 'no',
        ('L.', 'E.', 'D.'): 'led',
        ('lead',): 'lead',
        ('mead',): 'lead',
        ('read',): 'read',
        ('red', 'short'): 'red',
        ('read', 'too'): 'reed',
        ('hold', 'on', 'two'): 'hold on',
        ("you're", 'word'): 'your',
        ("your", 'word'): 'your',
        ('your', 'mark'): "you're",
        ('you', 'are', 'marked'): "you're",
        ('you', 'are', 'mark'): "you're",
        ('C.', 'S.'): "see",
        ('they', 'are', 'words'): "they are",
        ('E.', 'I.', 'R.'): "their",
        ('E.', 'R.', 'E.'): "there",
        ('they', 'are', 'marked'): "they're",
        ('they', 'mark'): "they're",
        ('CS'): "see",
        ('C.', 'letter'): "c",
        ('see', 'letter'): "c",
        ('C.', 'C.'): "cee",
        ('CC',): "cee",
        ('ready',): 'ready',
        ('yes',): 'yes',
        ('what', 'no', 'mark'): 'what',
        ('three', 'H.'): 'uhhh',
        ('left',): 'left',
        ('right',): 'right',
        ('write',): 'right',
        ('middle',): 'middle',
        ('metal',): 'middle',
        ('wait',): 'wait',
        ('press',): 'press',
        ('five', 'letters'): 'uh huh',
        ('four', 'letters'): 'uh uh',
        ('what', 'mark'): 'what?',
        ('done',): 'done',
        ('next',): 'next',
        ('hold',): 'hold',
        ('sure',): 'sure',
        ('like',): 'like',
        ('mike',): 'like',
        ('might',): 'like',
        ('white',): 'like',
        ('light',): 'like',
    }

    positions = {
        'yes': 3,
        'first': 2,
        'display': 6,
        'okay': 2,
        'says': 6,
        'nothing': 3,
        ' ': 5,
        'blank': 4,
        'no': 6,
        'led': 3,
        'lead': 6,
        'read': 4,
        'red': 4,
        'reed': 5,
        'leed': 5,
        'hold on': 6,
        'you': 4,
        'you are': 6,
        'your': 4,
        "you're": 4,
        'ur': 1,
        'there': 6,
        "they're": 5,
        'their': 4,
        'they are': 3,
        'see': 6,
        'c': 2,
        'cee': 6
    }

    table = {
        "ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready", "no", "first", "uhhh", "nothing", "wait"],
        "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
        "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no", "middle"],
        "blank": ["wait", "right", "okay", "middle", "blank", "press", "ready", "nothing", "no", "what", "left", "uhhh", "yes", "first"],
        "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing", "ready"],
        "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes", "left", "blank", "no", "wait"],
        "what": ["uhhh", "what", "left", "nothing", "ready", "blank", "middle", "no", "okay", "first", "wait", "yes", "press", "right"],
        "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh", "middle", "wait", "first"],
        "left": ["right", "left"],
        "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"],
        "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"],
        "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"],
        "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"],
        "press": ["right", "middle", "yes", "ready", "press"],
        "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"],
        "you are": ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you ", "u", "you're", "sure", "ur", "you are"],
        "your": ["uh uh", "you are", "uh huh", "your"],
        "you're": ["you", "you're"],
        "ur": ["done", "u", "ur"],
        "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"],
        "uh huh": ["uh huh"],
        "uh uh": ["ur", "u", "you are", "you", "done", "hold", "uh uh", "next", "sure", "like", "your", "sure", "hold", "what?"],
        "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"],
        "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
        "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"],
        "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"],
        "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"],
        "like": ["you're", "next", "u", "ur", "hold", "uh uh", "what?", "uh huh", "you", "like"],
    }

    responses = {
        "you are": ("you" "are", "words"),
        "done": ("done",),
        "ur": ("you", "are", "letters"),
        "sure": ("sure",),
        "you": ("you", "word"),
        "hold": ("hold",),
        "u": ("you", "letter"),
        "yes": ("yes",),
        "first": ("first",),
        "display": ("display",),
        "okay": ("okay",),
        "says": ("says",),
        "nothing": ("nothing",),
        " ": ("literally", "blank"),
        "blank": ("blank",),
        "no": ("no",),
        "led": ("L.", "E.", "D."),
        "lead": ("lead",),
        "read": ("read",),
        "red": ("red", "short"),
        "reed": ("read", "too"),
        "hold on": ("hold", "on", "two"),
        "your": ("your", "word"),
        "you're": ("you", "are", "mark"),
        "see": ("C.", "S."),
        "they are": ("they", "are", "words"),
        "their": ("E.", "I.", "R."),
        "there": ("E.", "R.", "E."),
        "they're": ("they", "are", "marked"),
        "see": ("s e e"),
        "c": ("see", "letter"),
        "cee": ("C.", "C."),
        "cee": ("CC",),
        "ready": ("ready",),
        "yes": ("yes",),
        "what": ("what", "no", "mark"),
        "uhhh": ("three", "H."),
        "left": ("left",),
        "right": ("right",),
        "right": ("write",),
        "middle": ("middle",),
        "wait": ("wait",),
        "press": ("press",),
        "uh huh": ("five", "letters"),
        "uh uh": ("four", "letters"),
        "what?": ("what", "mark"),
        "done": ("done",),
        "next": ("next",),
        "hold": ("hold",),
        "sure": ("sure",),
        "like": ("like",),
    }
    print words

    for combo, select in sorted(combos.iteritems(), key=lambda x: len(x[0])):
        for word in combo:
            print word, words.split()
            if word not in words.split():
                break
        else:
            print 'Words', words
            print "Found word: {}".format(select)
            if 'one' in words:
                return positions[select]

            if 'two' in words:
                wordlist = table[select]
                answer = []
                for word in wordlist[:5]:
                    answer.append(responses[word])

                return ', '.join(answer)

            break
