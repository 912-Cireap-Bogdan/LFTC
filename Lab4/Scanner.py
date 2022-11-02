from SymbolTable import HashTable


class Scanner():
    def __init__(self) -> None:
        self.table = HashTable(10)
        self.PIF = HashTable(10)
        self.tokens = []
        self.program = []
        self.pif_file = 'LFTC\Lab4\PIF.out'
        self.st_file = 'LFTC\Lab4\ST.out'
    

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

        pif = open(self.pif_file,'a')
        st = open(self.st_file,'a')

        for i in range(len(self.program)):
            item = self.program[i]
            for j in range(len(item)):
                if str(item[j]).isupper():
                    if item[j] not in self.tokens:
                    #make this a file write
                        string_to_print = str( str(item[j]) +" lexical error at program line: "+ str(i+1) + ':' + str(j+1))
                        print(string_to_print)
                        st.write(string_to_print)
                        st.write('\n')
                    else:
                        print(item[j], "inserting this keyword in the PIF with value 0")
                        self.PIF.insert(str(item[j]),0)

                
                elif str(item[j]).islower() or item[j].isdigit():
                    if item[j][0] == '"' and item[j][-1] == '"':
                        print(item[j],"constant string inserting into ST at with value 1")
                        self.table.insert(str(item[j]),1)
                        pass
                    if item[j].isdigit():
                        print(item[j],"constant int inserting into PIF at with value 2")
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
                    print(item[j], "operator or separator inserting into PIF at with value 0")
                    self.PIF.insert(str(item[j]),0)
                    pass

        print("ST: ",self.table)
        print("PIF: ",self.PIF)

        for item in self.table.table:
            if str(item) != '[]':
                st.write(str(item))
                st.write('\n')
        
        for item in self.PIF.table:
            if str(item) != '[]':
                pif.write(str(item))
                pif.write('\n')
                

        st.write('\n')
        pif.write('\n')

        st.close()
        pif.close()


s = Scanner()

good = r'LFTC\Lab1\p1.txt'
bad = r'LFTC\Lab1\p1_with_errors.txt'

s.get_token_in()
s.parse_files_in_tokens(bad)
s.store_in_st()