

#LL1 Parsing class
from Grammar import Grammar

class ParsingLL1:
    def __init__(self, grammar, sequence, out):
        self.grammar = Grammar(file=grammar)
        self.sequence = self.read_sequence(file=sequence)
        self.out = out
        self.first_set = self.First(self.grammar.S[0], {}, [])

        self.follow_set = self.Follow({}, self.first_set)
        self.parsing_table = self.create_parsing_table()


    def create_parsing_table(self):
        """
        for each production A -> alpha in your grammar:
            daca am S->
          for each terminal t in FIRST(alpha):
            add A -> alpha to M[A, t]
          if epsilon is in FIRST(alpha):
            for each terminal b in FOLLOW(A):
      add A -> alpha to M[A, b]
        :return:
        """
        parsing_table = {}
        for nonterminal in self.grammar.N:
            parsing_table[nonterminal] = {}
            for terminal in self.grammar.E:
                parsing_table[nonterminal][terminal] = []
            parsing_table[nonterminal]['$'] = []


        for key in self.grammar.P.keys():

            aux = self.grammar.P[key]
            for nonterminal in aux:
                if nonterminal.isupper():
                    aux_first = self.first_set[nonterminal]
                    for _ in aux_first:
                        if _ != '@':
                            parsing_table[key][_].append(nonterminal)
                        if '@' in aux_first and '$' not in parsing_table[key]['$']:
                            parsing_table[key]['$'] = ['$']
                else:
                    aux_first = self.first_set[key]
                    for _ in aux_first:
                        if _ != '@' and _ not in parsing_table[key][_]:
                            parsing_table[key][_].append(_)
                        if '@' in aux_first and '$' not in parsing_table[key]['$']:
                            follow_aux = self.follow_set[key]
                            for item in follow_aux:
                                if item not in parsing_table[key][item]:
                                    parsing_table[key][item].append(item)

        return parsing_table

    def read_sequence(self, file):

        seq = []
        with open(file) as f:
            line = f.readline()
            aux = line[0:-1].split(" ")
            seq.append(aux)

        print("sequence: ",seq)
        return seq

    def First(self, grammar_symbol, answer, skip=None):
        """
        Rules to compute FIRST set:
        If x is a terminal, then FIRST(x) = { ‘x’ }
        If x-> Є, is a production rule, then add Є to FIRST(x).
        If X->Y1 Y2 Y3….Yn is a production,
            FIRST(X) = FIRST(Y1)
            If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
            If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).
        """
        if skip is None:
            skip = []
        if grammar_symbol[0].islower() and len(grammar_symbol) == 1:
            return {grammar_symbol[0]: [grammar_symbol[0]]}

        if grammar_symbol[0].isupper():
            if grammar_symbol in self.grammar.S:
                answer[grammar_symbol] = []
                list_to_calculate = []
                for item in self.grammar.P[grammar_symbol]:
                    list_to_calculate.append(item)

                for item in list_to_calculate:
                    self.First(item, answer, skip)
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
                                aux = self.grammar.S[0]
                                answer[aux].append(item)
                        else:
                            answer[self.grammar.S[0]].append(item)
                            for item in self.grammar.P.keys():
                                if item not in skip:
                                    skip.append(item)
                            break

                    skip.append(key)

        return answer

    def Follow(self, answer,first_set):
        """
        1) FOLLOW(S) = { $ }   // where S is the starting Non-Terminal
        2) If A -> pBq is a production, where p, B and q are any grammar symbols,
           then everything in FIRST(q)  except Є is in FOLLOW(B).
        3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).
        4) If A->pBq is a production and FIRST(q) contains Є,
           then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)
        """
        answer = {nonterminal: [] for nonterminal in self.grammar.N}
        for nonterminal in self.grammar.N:
            if nonterminal.isupper():
                if nonterminal in self.grammar.S:
                    answer[nonterminal].append('$')

                # for nonterm, rhs in self.grammar.P.items():
                else:
                    for _, s_rhs in self.grammar.P.items():
                        if nonterminal in s_rhs:
                            aux = s_rhs.index(nonterminal)
                            if aux + 1 == len(s_rhs):
                                answer[nonterminal].append('$')
                                break
                            else:
                                aux_for_first_set = s_rhs[aux+1]
                            if '@' in self.first_set[aux_for_first_set]:
                                for item in self.first_set[aux_for_first_set]:
                                    answer[nonterminal].append(item)
                                answer[nonterminal].remove('@')
                                for item in answer[_]:
                                    answer[nonterminal].append(item)

                            else:
                                answer[nonterminal] = self.first_set[aux_for_first_set]

        return answer

    def parse(self):
        stack = []
        stack.append(self.grammar.S[0])
        sequence = [item for item in self.sequence[0]]
        # Initialize the current symbol to be the first symbol in the sequence
        i = 0
        current_symbol = sequence[i]
        iteration = 0
        while stack:
            # Get the top symbol on the stack
            top_symbol = stack[-1]
            # If the top symbol is a terminal
            if top_symbol in self.grammar.E:
                # If it matches the current symbol in the sequence, move to the next symbol
                if top_symbol == current_symbol:
                    stack.pop()
                    i += 1
                    if i < len(sequence):
                        current_symbol = sequence[i]
                    if i == len(sequence) -1:
                        return True
                # If it does not match, the sequence is not accepted
                else:
                    return False
            # If the top symbol is a nonterminal
            else:
                # Get the production for this nonterminal
                production = self.parsing_table[top_symbol][current_symbol]
                # If there is no production, the sequence is not accepted
                if not production:
                    return False
                # Replace the nonterminal with the production
                # stack.pop()

                # if iteration != 0:
                #     stack.pop()
                # iteration += 1
                for symbol in production[::-1]:
                    stack.append(symbol)
        # If the stack is empty and we have processed all symbols in the sequence, the sequence is accepted
        if not stack and i == len(sequence):
            return True
        # Otherwise, the sequence is not accepted
        return False
p = ParsingLL1(grammar='g1.txt',sequence='g1_seq.txt',out='out.txt')

print("/// first and follow ///")
print(p.first_set)
print(p.follow_set)
print("/// parsing table ///")
print(p.parsing_table)

print("/// started parsing ///")
# print(p.parse())

if p.parse() == True:
    print("Sequence accepted")
else:
    print("Sequence not accepted")