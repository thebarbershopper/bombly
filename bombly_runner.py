from dragonfly import *
from dragonfly.engines.backend_sapi5.engine import Sapi5InProcEngine

from bombly import bomb

engine = Sapi5InProcEngine()
engine.connect()


class BombCarRule(CompoundRule):
    spec = 'car <car>'
    extras = [IntegerRef('car', 0, 10)]

    def _process_recognition(self, node, extras):
        bomb.set_car(extras)


class BombBatteriesRule(CompoundRule):
    spec = 'batteries <batteries>'
    extras = [IntegerRef('batteries', 0, 10)]

    def _process_recognition(self, node, extras):
        bomb.set_batteries(extras)


class BombFreakRule(CompoundRule):
    spec = 'freak <word>'
    extras = [Dictation('word')]

    def _process_recognition(self, node, extras):
        bomb.set_freak(extras)


class BombParallelRule(CompoundRule):
    spec = 'parallel <word>'
    extras = [Dictation('word')]

    def _process_recognition(self, node, extras):
        bomb.set_parallel(extras)


class BombSerialRule(CompoundRule):
    spec = 'serial <word>'
    extras = [Dictation('word')]

    def _process_recognition(self, node, extras):
        bomb.set_serial(extras)


class BombVowelRule(CompoundRule):
    spec = 'vowel <word>'
    extras = [Dictation('word')]

    def _process_recognition(self, node, extras):
        bomb.set_vowel(extras)


class BombResetRule(CompoundRule):
    spec = 'bomb reset'

    def _process_recognition(self, node, extras):
        from bombly.bomb import reset_bomb
        reset_bomb()


class BombStatusRule(CompoundRule):
    spec = 'bomb status'

    def _process_recognition(self, node, extras):
        from bombly.bomb import bomb_status
        bomb_status()


class BombDoneRule(CompoundRule):
    spec = 'bomb done'

    def _process_recognition(self, node, extras):
        from bombly.bomb import bomb_done
        engine.speak(bomb_done())


class SimpleWiresRule(CompoundRule):
    spec = 'simple wires <wires>'
    extras = [Dictation('wires')]

    def _process_recognition(self, node, extras):
        from bombly.modules.wires import wires
        speak = wires(extras, bomb.serial, bomb.sanitize_colors, bomb.odd_serial)
        engine.speak(speak)


class ComplexWiresRule(CompoundRule):
    spec = 'complex wires <wires>'
    extras = [Dictation('wires')]

    def _process_recognition(self, node, extras):
        from bombly.modules.complicated_wires import complicated_wires
        speak = complicated_wires(extras, bomb.batteries, bomb.parallel, bomb.serial)
        engine.speak(speak)


class MazeRule(CompoundRule):
    spec = 'maze <maze>'
    extras = [Dictation('maze')]

    def _process_recognition(self, node, extras):
        from bombly.modules.mazes import solve_maze
        speak = solve_maze(extras)
        for item in speak:
            engine.speak(item)


class SimonRule(CompoundRule):
    spec = 'simon <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.simon_says import simon
        speak = simon(extras, bomb.vowel)
        engine.speak(speak)


class WireSequenceRule(CompoundRule):
    spec = 'wire sequence <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.wire_sequences import wire_sequence
        for item in wire_sequence(extras):
            engine.speak(item)


class WireSequenceResetRule(CompoundRule):
    spec = 'wire sequence reset'

    def _process_recognition(self, node, extras):
        from bombly.modules.wire_sequences import reset_wire_sequence
        reset_wire_sequence()


class ButtonRule(CompoundRule):
    spec = 'button <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.the_button import button
        speak = button(extras, bomb.batteries, bomb.freak, bomb.car)
        engine.speak(speak)


class ButtonColorRule(CompoundRule):
    spec = 'button color <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.the_button import button_strip
        speak = button_strip(extras)
        engine.speak(speak)


class KnobsRule(CompoundRule):
    spec = 'knobs <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.needy.knob import knob
        speak = knob(extras)
        engine.speak(speak)


class MemoryRule(CompoundRule):
    spec = 'memory <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.memory import memory
        speak = memory(extras)
        engine.speak(speak)


class MemoryResetRule(CompoundRule):
    spec = 'memory reset'

    def _process_recognition(self, node, extras):
        from bombly.modules.memory import reset_memory
        reset_memory()


class MorseRule(CompoundRule):
    spec = 'morse <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.morse_code import morse_code
        speak = morse_code(extras)
        engine.speak(speak)


class MorseResetRule(CompoundRule):
    spec = 'morse reset'

    def _process_recognition(self, node, extras):
        from bombly.modules.morse_code import reset_morse
        reset_morse()


class WordsResetRule(CompoundRule):
    spec = 'words reset'

    def _process_recognition(self, node, extras):
        from bombly.modules.whos_on_first import reset_words
        reset_words()


class WordsRemoveRule(CompoundRule):
    spec = 'words remove'

    def _process_recognition(self, node, extras):
        from bombly.modules.whos_on_first import remove_words
        remove_words()


class SymbolsRule(CompoundRule):
    spec = 'symbols <symbols>'
    extras = [Dictation('symbols')]

    def _process_recognition(self, node, extras):
        from bombly.modules.keypads import keypad
        speak = keypad(extras)
        engine.speak(speak)


class WordsRule(CompoundRule):
    spec = 'words <words>'
    extras = [Dictation('words')]

    def _process_recognition(self, node, extras):
        from bombly.modules.whos_on_first import whos_on_first
        speak = whos_on_first(extras)
        engine.speak(speak)


class PasswordResetRule(CompoundRule):
    spec = 'password reset'

    def _process_recognition(self, node, extras):
        from bombly.modules.passwords import reset_password
        reset_password()


class PasswordRule(CompoundRule):
    spec = 'password <letters>'
    extras = [Dictation('letters')]

    def _process_recognition(self, node, extras):
        from bombly.modules.passwords import password
        possibles = password(extras)
        for word in possibles:
            engine.speak(word)


# Create a grammar which contains and loads the command rule.
grammar = Grammar('Keep Talking')
grammar.add_rule(BombBatteriesRule())
grammar.add_rule(BombVowelRule())
grammar.add_rule(BombParallelRule())
grammar.add_rule(BombSerialRule())
grammar.add_rule(BombFreakRule())
grammar.add_rule(BombCarRule())
grammar.add_rule(BombResetRule())
grammar.add_rule(BombStatusRule())
grammar.add_rule(SimpleWiresRule())
grammar.add_rule(ComplexWiresRule())
grammar.add_rule(MazeRule())
grammar.add_rule(SimonRule())
grammar.add_rule(WireSequenceRule())
grammar.add_rule(WireSequenceResetRule())
grammar.add_rule(ButtonRule())
grammar.add_rule(ButtonColorRule())
grammar.add_rule(KnobsRule())
grammar.add_rule(MemoryRule())
grammar.add_rule(MemoryResetRule())
grammar.add_rule(MorseRule())
grammar.add_rule(MorseResetRule())
grammar.add_rule(SymbolsRule())
grammar.add_rule(WordsRule())
grammar.add_rule(WordsResetRule())
grammar.add_rule(WordsRemoveRule())
grammar.add_rule(PasswordRule())
grammar.add_rule(BombDoneRule())
grammar.load()
