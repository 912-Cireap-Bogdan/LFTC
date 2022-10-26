from SymbolTable import HashTable


class Scanner():
    def __init__(self) -> None:
        self.table = HashTable(10)
        self.PIF = HashTable(10)
        self.tokens = []
        self.program = []
    

    def parse_files_in_tokens(self,filepath):
        with open (filepath) as file:
            lines = file.readlines()
            for i in range(1,len(lines)):
                step = lines[i].rstrip('\r\n')
                words = []
                for item in step.split(' '):
                    if len(item) !=0:
                        words.append(item)
                
              
                self.program.append(words)
        
        print(self.program)

        pass


    def get_token_in(self):
        with open(r'LFTC\Lab2\token.in') as file:
            lines = file.readlines()
            for line in lines:
                aux = line.rstrip('\r\n')
                self.tokens.append(aux)

        # print(self.tokens)

        pass

    def store_in_st(self):

        for i in range(len(self.program)):
            item = self.program[i]
            for j in range(len(item)):
                if str(item[j]).isupper():
                    if item[j] not in self.tokens:
                    #make this a file write
                        print(item[j],"lexical error at program line: " + str(i+1))
                    else:
                        print(item[j], "inserting this keyword in the ST with value 0")
                        self.PIF.insert(str(item[j]),0)

                
                elif str(item[j]).islower() or item[j].isdigit():
                    if item[j][0] == '"' and item[j][-1] == '"':
                        print(item[j],"constant string inserting into ST at with value 1")
                        self.PIF.insert(str(item[j]),1)
                        pass
                    if item[j].isdigit():
                        print(item[j],"constant int inserting into ST at with value 2")
                        self.PIF.insert(str(item[j]),2)
                        pass
                    
                    if item[j].islower() and item[j][0] != '"' and item[j][-1] != '"':
                        print(item[j], "identifier inserting into ST at with value 3")
                        if self.table.find(item[j]) is not False:
                            poz = self.table.find(item[j])
                        else:
                            poz = self.table.current_size

                        self.table.insert(str(item[j]),3)
                        self.table.insert(item[j],poz)
                    
                        pass
                
                else:
                    print(item[j], "operator or separator inserting into ST at with value 0")
                    self.PIF.insert(str(item[j]),0)
                    pass

        print("ST: ",self.table)
        print("PIF: ",self.PIF)


s = Scanner()

s.get_token_in()
s.parse_files_in_tokens(r'LFTC\Lab1\p1.txt')
s.store_in_st()