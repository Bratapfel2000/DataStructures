#written in py3.8

#node to store datapoints
class node:
	def __init__(self,data = None):
		self.data = data #dapoints to be stored
		self.next = None #last datapoint

class LinkedList:
	def __init__(self):
		self.head = node() #placeholder for first elt in list

	# adds new node which contains data, will be at the end of the linked list
	def add(self,data):
		new_node = node(data)
		picked_node = self.head
		while picked_node.next != None:
			picked_node = picked_node.next
		picked_node.next = new_node

	# returns the length of the linked list for controlling 
	def length(self):
		picked_node = self.head
		total = 0
		while picked_node.next != None:
			total+=1
			picked_node = picked_node.next
		return total 

  	# prints linked list as list format
	def show_list(self):
		elt=[]
		picked_node=self.head
		while picked_node.next!=None:
			picked_node=picked_node.next
			elt.append(picked_node.data)
		print(elt)

	# returns the node at requested index 
	def get(self,index):
		if index >= self.length() or index<0: 
			print("Error: Index out of range!")
			return None
		picked_idx = 0
		picked_node = self.head
		while True:
			picked_node = picked_node.next
			if picked_idx == index: return picked_node.data
			picked_idx += 1

	# deletes node at index if required at later stage 
	def remove(self,index):
		if index >= self.length() or index < 0: 
			print("Error: Index out of range!")
			return 
		picked_idx = 0
		picked_node = self.head
		while True:
			last_node = picked_node
			picked_node = picked_node.next
			if picked_idx == index:
				last_node.next = picked_node.next
				return
			picked_idx += 1
			
#creating fibonacci numbers and store them in list
class FiboNumbers:
        def __init__(self):
                self.fibo_numbers = [0,1] 
        def fibonacci(self, n=5): 
            if n<0: 
                print("Incorrect input") 
            elif n<=len(self.fibo_numbers): 
                return self.fibo_numbers[n-1] 
            else: 
                temp_fib = self.fibonacci(n-1)+self.fibonacci(n-2) 
                self.fibo_numbers.append(temp_fib) 
                return temp_fib

def main():
        #creating 99 fibonacci numbers
        fib = FiboNumbers()
        fib.fibonacci(99) 

        my_linked_list = LinkedList() #creating linked list

        #add numbers from list "fib.fibo_numbers" to linked list "my_linked_list"
        for i in fib.fibo_numbers: 
            my_linked_list.add(i)

        #add additional specific 100th last number to linked list 
        my_linked_list.add(218922995834555200000) 

        #print length of "my_linked_list" and show "my_linked_list"
        print("i.) my_linked_list")
        print("Length of my_linked_list:", my_linked_list.length())
        print("Show my_linked_list:")
        my_linked_list.show_list()

        print(30*"=") 

        new_linked_list = LinkedList() #create new linked list

        #add elements from "my_linked_list" to "my_linked_list_new" in reverse order
        for j in range(my_linked_list.length()): 
            new_linked_list.add(my_linked_list.get(my_linked_list.length()-j-1))

        #print length of "my_linked_list_new" and show "my_linked_list_new"
        print("ii.) new_linked_list")
        print("Length of new_linked_list:", new_linked_list.length())
        print("Show new new_linked_list:")
        new_linked_list.show_list()

        print(30*"=") 
        print("iii). Testing")
        if my_linked_list.length() == new_linked_list.length():
                for i in range(my_linked_list.length()):
                        if my_linked_list.get(i) != new_linked_list.get(my_linked_list.length()-i-1):
                                print("New list has different elements than given list")
                        else:
                                print(my_linked_list.get(i),
                                      new_linked_list.get(my_linked_list.length()-i-1),
                                      "both elements match")
        else:
                print("The two lists have different amount of elements..")

if __name__ == "__main__":
        main()
