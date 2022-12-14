

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

    def First(self, grammar_symbol,answer,skip):
        """
        Rules to compute FIRST set:
        If x is a terminal, then FIRST(x) = { ‘x’ }
        If x-> Є, is a production rule, then add Є to FIRST(x).
        If X->Y1 Y2 Y3….Yn is a production,
            FIRST(X) = FIRST(Y1)
            If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
            If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).
        """

        # daca is upper treve calculat First(X)

        if grammar_symbol[0].islower() and len(grammar_symbol) == 1:
            return {grammar_symbol[0] : [grammar_symbol[0]]}

        if grammar_symbol[0].isupper():
            if grammar_symbol in self.grammar.S:
                answer[grammar_symbol] = []
                list_to_calculate = []
                for item in self.grammar.P[grammar_symbol]:
                    list_to_calculate.append(item)


                for item in list_to_calculate:
                    self.First(item,answer,skip)

            else:
                for item in self.grammar.P[grammar_symbol]:
                    if grammar_symbol not in answer:
                        answer[grammar_symbol] = []
                    answer[grammar_symbol].append(item)



        for key in answer:
            if key not in self.grammar.S:
                if key not in skip:
                    for item in answer[key]:
                        if '@' in answer[key]:
                            if item != '@':
                                answer[self.grammar.S[0]].append(item)

                        else:
                            answer[self.grammar.S[0]].append(item)
                            for item in self.grammar.P.keys():
                                if item not in skip:
                                    skip.append(item)
                            break

                    skip.append(key)

        return answer


    def Follow(self, grammar_symbol, answer,first_set):
        """
        1) FOLLOW(S) = { $ }   // where S is the starting Non-Terminal
        2) If A -> pBq is a production, where p, B and q are any grammar symbols,
           then everything in FIRST(q)  except Є is in FOLLOW(B).
        3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).
        4) If A->pBq is a production and FIRST(q) contains Є,
           then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)
        """
        if grammar_symbol[0].isupper():
            if grammar_symbol in self.grammar.S:
                answer[grammar_symbol] = ['$']
                list_to_calculate =[]
                for item in self.grammar.P[grammar_symbol]:
                    list_to_calculate.append(item)
                    answer[item] = []

                for item in list_to_calculate:
                    self.Follow(item, answer,first_set)

            else:
                placeholder =[]
                # for aux in self.grammar.N:
                #     if aux not in self.grammar.S and aux != grammar_symbol:
                #         placeholder.append(aux)
                index = self.grammar.N.index(grammar_symbol)
                placeholder = self.grammar.N[index+1:]
                answer[grammar_symbol] = placeholder

                aux_answer = []
                stop = False
                for item in answer[grammar_symbol]:
                    for aux_item in first_set[item]:
                        if "@" in first_set[item]:
                            if aux_item != "@":
                                aux_answer.append(aux_item)
                        else:
                            aux_answer.append(aux_item)
                            answer[grammar_symbol] = aux_answer
                            return answer

                aux_answer.append('$')


                answer[grammar_symbol] = aux_answer





        return answer

    #LL(1) - functions FIRST, FOLLOW
    # First(): If there is a variable, and from that variable,if we try to drive all the strings then the beginning Terminal Symbol is called the First.
    # Follow(): What is the Terminal Symbol which follows a variable in the process of derivation.

    def parse_algorithm(self):
        """
        For each production A –> α. (A tends to alpha)

        1.Find First(α) and for each terminal in First(α), make entry A –> α in the table.
        2.If First(α) contains ε (epsilon) as terminal, then find the Follow(A) and for each terminal in Follow(A), make entry A –>  ε in the table.
        3.If the First(α) contains ε and Follow(A) contains $ as terminal, then make entry A –>  ε in the table for the $.

        To construct the parsing table, we have two functions:
            In the table, rows will contain the Non-Terminals and the column will contain the Terminal Symbols.
            All the Null Productions of the Grammars will go under the Follow elements and the remaining productions
            will lie under the elements of the First set

        :return:
        """

c = "A"
print(c[0])
p = ParsingLL1(grammar='g1.txt',sequence='g1_seq.txt',out='out.txt')
answer ={}

print("FIRST SET",p.First("S", answer, skip=[]))
# print("FIRST SET",p.First("a", answer, skip=[]))


answer2 = {}

print("FOLLOW SET", p.Follow("S",answer2, answer))
