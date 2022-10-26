

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.current_size = 0

    def insert(self,key,value):

        poz = hash(key) % self.size

        bucket = self.table[poz]

        found = False
        for index, item in enumerate(bucket):
            item_key, item_value = item

            if item_key == key:
                found=True
                break

        if found:
            bucket[index] = (key,value)
        
        else:
            bucket.append((key,value))
            self.current_size +=1

    
    def find(self, key):
        
        poz = hash(key) % self.size

        bucket = self.table[poz]
  
        found = False
        for index, item in enumerate(bucket):
            item_key, item_val = item
              
            if item_key == key:
                found = True
                break


        if found:
            return item_val
        else:
            return False
  
    def delete(self, key):
        poz = hash(key) % self.size
          
        bucket = self.table[poz]
  
        found = False
        for index, item in enumerate(bucket):
            item_key, item_val = item

            if item_key == key:
                found = True
                break
        if found:
            bucket.pop(index)
        return
  

    def __str__(self):
        return "".join(str(item) for item in self.table)

