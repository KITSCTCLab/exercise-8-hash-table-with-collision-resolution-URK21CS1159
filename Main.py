import re

def display_hash(hashtable) -> None:
	# Write your code here
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
	
def Hashing(keyvalue) -> int:
	return keyvalue % len(HashTable)

def insert(hashtable, keyvalue, value) -> None:
	# Write your code here
	hash_key = Hashing(keyvalue)
    hashtable[hash_key].append(value)
  


# Do not edit the following code
hash_table_size = int(input())
# Create Hashtable as a list of list.
hashTable = [[] for _ in range(hash_table_size)]
input_data = input()
data = []
for item in re.split('], |].', input_data):
  item = item[1:]
  data = item.split(', ')
  if len(data) > 1:
    insert(hashTable, int(data[0]), data[1])

display_hash (hashTable)
