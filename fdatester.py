__author__ = 'Willams de Lima a.k.a cyborg'

# coding = Unicode

import time
import gettext
t = gettext.translation('fdatester', localedir='locale', languages=['pt_BR'])
_ = t.gettext

''' An automaton is a finite state machine. It's function is composed by:
        M = (Alphabet, Set of States, Starting State, Accepting State, Transition Function)
'''

def M(alphabet, sos, ss, acs):

    #static for now

    #since we have 2 symbols in the alphabet and 3 states, we'll have 2x3 "slots" in our transition function.


    '''
        [q0]    [q1]    [q2]

    a    q1      q2      q2
    b    q0      q1      q2

    '''

    #starting the array...

    Matrix = [[0 for x in range(len(alphabet))] for x in range (len(sos))]
    i = 0
    j = 0
    for i in range(len(sos)):
       for j in range(len(alphabet)):
            #print(_("FT: ", sos[i], " with ", alphabet[j]))
            print(_("FT: %s with %s") % (sos[i], alphabet[j]))
            Matrix[i][j] = input(">>> ")
    i = j = 0
    for i in range(len(sos)):
        for j in range(len(alphabet)):
            #print(_("FT: ", sos[i], " with ", alphabet[j], " results into ", Matrix[i][j]))
            print(_("FT: %s with %s results into %s") % (sos[i], alphabet[j], Matrix[i][j]))


    def getPositionAlphabet(letter):
        #print(_(letter)
        for k in range(len(alphabet)):
            #print(_(k)
            #print(_(alphabet[k])
            if letter == alphabet[k]:
                return k
                break

    def getPositionState(actual_state):
        #print(_(actual_state)
        for q in range(len(sos)):
            #print(_(q)
            #print(_(sos[q])
            if actual_state == sos[q]:
                return q
                break

    while 1:
        w = input("Insert test string: ")
        current_state = ss

        print(_("Testing word: %s" % (w)))
        i = 0
        for i in range(len(w)):
            #remove me
            #print(_("FT: ", sos[getPositionState(current_state)], " with ", alphabet[getPositionAlphabet(w[i:i+1])], " results into ", Matrix[getPositionState(current_state)][getPositionAlphabet(w[i:i+1])]))
            print(_("FT: %s with %s results into %s") % (sos[getPositionState(current_state)], alphabet[getPositionAlphabet(w[i:i+1])], Matrix[getPositionState(current_state)][getPositionAlphabet(w[i:i+1])]))
            current_state = Matrix[getPositionState(current_state)][getPositionAlphabet(w[i:i+1])]
            time.sleep(2)
        if current_state in acs:
            print(_("\n\n\n\n\n\nThe string w = %s  was accepted by the automaton!") % (w))
        else:
            print(_("\n\n\n\n\n\nThe string w = %s  was [NOT] accepted by the automaton!") % (w))
        if input("Test another word? [Yes/No]") == "no": break

def main():
    #Starts translation. Ignore this.


    

    #
    '''alphabet = ['a', 'b']
    sos = ['q0', 'q1', 'q2']
    ss = ['q0']
    acs = ['q2']'''
    print(_("An automaton is composed by an alphabet, a set of states, a starting state and a set of accepting states."))

    print(_("\nLet's start by adding symbols to our alphabet {A}."))
    print(_("\nInsert all the symbols separated by comma (,). For example::       a, b"))
    print(_("Insert, now, the symbols of the alphabet {A}: "), end="")
    inputAlphabet = input("")
    alphabet = inputAlphabet.replace(" ", "").split(',')
    print(alphabet)

    print(_("\nNow let's add our set of states {Q}."))
    print(_("\nInsert all states separated by comma (,). For example::    q0, q1, q2, q3"))
    print(_("Insert, now, the states of {Q}: "), end="")
    inputStates = input("")
    sos = inputStates.replace(" ", "").split(',')
    print(sos)

    while 1:
        print(_("\nThese are your states: "), end="")
        print(sos)
        print(_("\nSelect one state from this list to be the starting state."))
        ss = input(">>> ")
        if ss in sos:
            break
        print(_("\nInvalid."))


    print(_("\nNow let's add our set of accepting states {F}."))
    print(_("\nInsert all states separated by comma (,). For example::    q0, q1"))
    print(_("\nRemember that this set needs to be a subset of {Q}, otherwise you won't get a result."))
    inputAccepted = input("Insert, now, the states of {F}: ")
    acs = inputAccepted.replace(" ", "").split(',')

    M(alphabet, sos, ss, acs)

if __name__ == '__main__':
    main()


