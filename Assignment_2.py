class Order:
    def __init__ (self, meals, table_num):
        self.meals = meals
        self.table_num = table_num
        self.next = None
        
class Kitchen:
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def add_order(self, order):
        if self.tail == None:
            self.head = order
            self.tail = order
        else:
            self.tail.next = order
            self.tail = order
        # print(order)
            
    def cook_order(self):
        if self.head == None:
            print('No orders.')
            return None
        else:
            cooked = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return cooked
        
    def delete_order(self, table):
        current = self.head
        prev = None
        while current:
            if current.table_num == table:
                if prev:
                    prev.next = current.next
                if current == self.tail:
                        self.tail = prev  
                else:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None 
                return
            prev = current
            current = current.next
        print(f"Order for {table} was sucessfully deleted.")
        
        
    def view_orders(self):
        if self.head == None:
            print('No orders.')
        else:
            current = self.head
            while current:
                print(f"Table {current.table_num} ordered {', '.join(current.meals)}")
                current = current.next
                
                
kitchen = Kitchen()

# Add orders 
order1 = Order(['Chicken Soup', 'Greek Salad'], 1)
order2 = Order(['Blackened Salmon', 'Baked Potato'], 2)
order3 = Order(['Grilled Calamari', 'Marinara Pizza'], 3)

kitchen.add_order(order1)
kitchen.add_order(order2)
kitchen.add_order(order3)

# View current orders 
print("Current orders:")
kitchen.view_orders()

# Cooked order
cooked = kitchen.cook_order()
if cooked:
    print(f"\nCooked order for Table {cooked.table_num}: {', '.join(cooked.meals)}\n")

# Delete an order 
kitchen.delete_order(1)

# View still uncooked orders
print("\nOrders in the kitchen:")
kitchen.view_orders()

                
        