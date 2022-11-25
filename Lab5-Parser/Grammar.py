
class Grammar:
    def __init__(self, file="r'LFTC\Lab5-Parser\g1.txt'") -> None:
        self.file = file
        self.grammar = self.read_grammar_from_file()

        self.N = None
        self.E = None
        self.P = None
        self.S = None

    
    def read_grammar_from_file(self):
        grammar = []
        with open(self.file) as f:
            line = f.readline()
    


    def print_nonterminals(self):
        return self.N

    def print_terminals(self):
        return self.E

    def print_productions(self):
        return self.P

    def print_prod_for_nonterminal(self,nonterm):
        result = ""
        if nonterm in self.P.keys():
            result += "The productions for {0} are: \n".format(result)
            for p in self.P[nonterm]:
                res += nonterm + '->' + " ".join(p) + '\n'
        else:
            result += "nonterminal not matching"

        return result

    def checkCFG(self):
        for elem in self.N:
            if elem in self.E:
                return False
            if elem in self.N:
                return False
        
        for elem in self.E:
            if elem in self.E:
                return False