

class FiniteAutomata:
    def __init__(self,Q = [], E=[],q0=[],F=[],S={}):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    # F : set of Final States.
    # Q : Finite set of states.
    # E : set of Input Symbols.
    # q0 : Initial state.
    # S : Transition Function.


    def checkDFA(self):
        # If |δ(q,a)|≤1 => deterministic finite automaton (DFA)
        for key in self.S.keys():
            if len(self.S[key]) > 1:
                return False
        
        return True
        

    def checkAccepted(self,seq):
        if self.checkDFA():
            pass

        return False

    def readFAFromFile(self, file):
        with open(file) as f:
            self.Q = [elem for elem in f.readline().strip().split(' ')[2:]]
            self.E = [elem for elem in f.readline().strip().split(' ')[2:]]
            self.q0 = [elem for elem in f.readline().strip().split(' ')[2:]]
            self.F = [elem for elem in f.readline().strip().split(' ')[2:]]
            print(self.Q, self.E, self.q0, self.F)
            
            #empty read to pass emptry row
            f.readline() 

            for line in f:
                aux_string = line.strip().split('=>')
                aux_elem = aux_string[0].strip().replace('(','').replace(')','')

                source = aux_elem.strip().split(',')[0]
                destination = aux_string[1].strip()
                road = aux_elem.strip().split(',')[1]

                print(source ,road, destination)
                print(self.S)

                if (source, road) in self.S.keys():
                    self.S[(source,road)].append(destination)

                else:
                    self.S[(source,road)] = [destination]


    def __str__(self):

        Q= "Q = {" + ','.join(self.Q) + "} \n"
        E= "E = {" + ','.join(self.E) + "} \n"
        q0 = "q0 = {" + ','.join(self.q0) + "} \n"
        S= "S = " + str(self.S) + " \n"

        F= "F = {" + ','.join(self.F) + "} \n"

        return Q+E+q0+S+F
# fa = FiniteAutomata(Q = [], E=[],q0=[],F=[],S={})
# fa.readFAFromFile(r'LFTC\Lab5\FA.in')
# print(fa)
# print(fa.checkDFA())
# print(fa.checkAccepted(""))


class run:
    def __init__(self):
        self.fa = FiniteAutomata()
        self.fa.readFAFromFile(r'LFTC\Lab5\FA.in')

    def menu(self):
        print("1.printFA")
        print("2.printStates")
        print("3.printAlphabet")
        print("4.printTransitions")
        print("5.printFinalStates")
        print("6.checkDFA")
        print("7.checkAcceptance")


    def printFA(self):
        print(self.fa)

    def printStates(self):
        print(self.fa.Q)
    
    def printAlphabet(self):
        print(self.fa.E)

    def printTransitions(self):
        print(self.fa.S)

    def printFinalStates(self):
        print(self.fa.F)

    def checkDFA(self):
        print(self.fa.checkDFA())

    def checkAcceptance(self):
        seq = input("sequence: ")
        print(self.fa.checkAccepted(seq))

    def run(self):
        command_dict = {'1':self.printFA, '2':self.printStates, '3':self.printAlphabet, '4':self.printTransitions,'5':self.printFinalStates, '6':self.checkDFA, '7': self.checkAcceptance}
        
        running = True

        while running:
            self.menu()
            command = input("command: ")
            if command in command_dict.keys():
                command_dict[command]()
            elif command=='0':
                running = False
            else:
                continue

r = run()

r.run()