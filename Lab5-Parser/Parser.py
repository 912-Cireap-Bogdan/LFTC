

#LL1 Parsing class
from Grammar import Grammar

class ParsingLL1:
    def __init__(self, grammar, sequence, out):
        self.grammar = Grammar(file=grammar)
        self.sequence = self.read_sequence(file=sequence)
        self.out = out
        
        pass


    def read_sequence(self, file):

        seq = []
        with open(file) as f:
            line = f.readline()
            aux = line[0:-1].split(" ")
            seq.append(aux)

        print("sequence: ",seq)
        return seq

    def First(self, grammar_symbol):
        """
        Rules to compute FIRST set:
        If x is a terminal, then FIRST(x) = { ‘x’ }
        If x-> Є, is a production rule, then add Є to FIRST(x).
        If X->Y1 Y2 Y3….Yn is a production,
            FIRST(X) = FIRST(Y1)
            If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
            If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).
        """
        result = {}
        if grammar_symbol in self.grammar.E:
            result = { grammar_symbol }


    def Follow(self, item):
        """

        1) FOLLOW(S) = { $ }   // where S is the starting Non-Terminal

        2) If A -> pBq is a production, where p, B and q are any grammar symbols,
           then everything in FIRST(q)  except Є is in FOLLOW(B).

        3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).

        4) If A->pBq is a production and FIRST(q) contains Є,
           then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)

        """

    #LL(1) - functions FIRST, FOLLOW
    # First(): If there is a variable, and from that variable,if we try to drive all the strings then the beginning Terminal Symbol is called the First.
    # Follow(): What is the Terminal Symbol which follows a variable in the process of derivation.


p = ParsingLL1(grammar='g1.txt',sequence='g1_seq.txt',out='out.txt')