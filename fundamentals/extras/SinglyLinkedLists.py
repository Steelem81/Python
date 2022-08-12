class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        self.head  = self.head.next

        return self

    def remove_from_back(self):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.remove_node()
        return self

    def remove_val(self, val):
        pass

    def instert_at(self, val, n):
        pass

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


    def __repr__(self):
        return (f'{self.value}')

    def remove_node(self):
        self.value = None
        

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values() 
my_list.remove_from_front().print_values()
my_node = SLNode('Testing')
my_node.remove_node()
my_list.remove_from_back().print_values()

