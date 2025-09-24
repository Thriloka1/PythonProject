
class CustomerNode:
    def __init__(self,name, location):
        self.name=name
        self.location=location
        self.next=None

class CustomerList:
    def __init__(self):
        self.head=None
    def add_customer(self,name,location):
        new_node=CustomerNode(name,location)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def get_customer_by_name(self,name):
        current=self.head
        while current:
            if current.name.lower()==name.lower():
                return current
            current=current.next
        return None

    def display_customers(self):
        current=self.head
        if not current:
            print("no customers yet")
            return
        while current:
            print(f"{current.name} at {current.location}")
            current=current.next

customers=CustomerList()