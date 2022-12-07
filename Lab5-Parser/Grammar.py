
class Grammar:
    def __init__(self, file="g1.txt"):
        self.file = file
        self.grammar = self.read_grammar_from_file()
        
        #nonterminals
        self.N = self.grammar[0]
        #terminals
        self.E = self.grammar[1]
        #starting sybol
        self.S = self.grammar[2]
        #productions
        self.P = self.parse_productions(self.grammar[3])

    
    def read_grammar_from_file(self):
        grammar = []
        with open(self.file) as f:
            #nonterminals
            line = f.readline()
            aux = line[0:-1].split(" ")
            grammar.append(aux)

            #terminal symbols
            line = f.readline()
            aux = line[0:-1].split(" ")
            grammar.append(aux)

            # starting symbol
            line = f.readline()
            aux = line[0:-1].split(" ")
            grammar.append(aux)

            #productions where i use $ as the separator
            prod = []
            line = f.readline()

            while line != '':
                production = line[0:-1]
                aux = production.split(" ")
                prod.append(aux)

                line = f.readline()
            
            grammar.append(prod)
        
        print("grammar", grammar)
        return grammar

    def parse_productions(self, productions):
        dictionary = {}
        for p in productions:
            if p[0] not in dictionary.keys():
                dictionary[p[0]] = []

            aux = p[1].split("$")
            dictionary[p[0]].append(aux)

        print("productions dictionary", dictionary)
        return dictionary


    def print_nonterminals(self):
        print(self.N)

    def print_terminals(self):
        print(self.E)

    def print_productions(self):
        print(self.P)

    def print_prod_for_nonterminal(self,nonterm):
        result = ""
        if nonterm in self.P.keys():
            result += "The productions for {0} are: \n".format(result)
            for p in self.P[nonterm]:
                result += nonterm + '->' + " ".join(p) + '\n'
        else:
            result += "nonterminal not matching"

        print(result)
        return result


    def checkCFG(self):
        keys = []
        for k in self.P.keys():
            if k not in keys:
                keys.append(k)

        if len(keys) ==1:
            return True

        return False


# g = Grammar()
# g.print_nonterminals()
# g.print_terminals()
# g.print_productions()
# g.print_prod_for_nonterminal('S')
# print(g.checkCFG())