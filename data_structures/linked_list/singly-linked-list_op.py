class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a new node
def create_new_node(new_data):
    return Node(new_data)

# Insert a node at the beginning
def insert_node_infront(head, new_data):
    new_node = create_new_node(new_data)
    new_node.next = head
    return new_node

# Insert a node at a specific position
def insert_node_at_position(head, new_data, position):
    new_node = create_new_node(new_data)

    if position == 1:
        new_node.next = head
        return new_node

    current = head
    for i in range(1, position - 1):
        if current is None:
            print("Position not available.")
            return head
        current = current.next

    if current is None:
        print("Position not available.")
        return head

    new_node.next = current.next
    current.next = new_node
    return head

# Insert a node at the end
def insert_node_at_last(head, new_data):
    new_node = create_new_node(new_data)

    if head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next

    current.next = new_node
    return head

# Delete the first node
def delete_node_infront(head):
    if head is None:
        return None

    temp = head
    head = head.next
    del temp
    return head

# Delete a node at a specific position
def delete_node_at_position(head, position):
    if head is None:
        return None

    if position == 1:
        return delete_node_infront(head)

    current = head
    prev = None
    for i in range(1, position):
        if current is None:
            print("Position not available.")
            return head
        prev = current
        current = current.next

    if current is None:
        print("Position not available.")
        return head

    prev.next = current.next
    del current
    return head

# Delete the last node
def delete_node_last(head):
    if head is None:
        return None

    if head.next is None:
        del head
        return None

    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    del second_last.next
    second_last.next = None
    return head

# Print the linked list
def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

# Main function
def main():
    head = create_new_node(2)
    head.next = create_new_node(3)
    head.next.next = create_new_node(4)
    head.next.next.next = create_new_node(5)
    #initial linked list is 2->3->4->5

    while True:
        print("\nMenu:")
        print("1. Display linked list")
        print("2. Insert an element")
        print("3. Delete an element")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nThe list is:", end=" ")
            print_list(head)
            #should print  #initial linked list is 2->3->4->5

        elif choice == 2:
            print("\nInsert Options:")
            print("1. Insert node at the beginning")
            print("2. Insert node at the end")
            print("3. Insert node at a specific position")
            print("4. Exit")
            var1 = int(input("Enter your choice: "))

            if var1 == 1:
                new_data = int(input("Enter the new data to be inserted: "))
                head = insert_node_infront(head, new_data)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                 #linked list is 1->2->3->4->5 if 1 is new data

            elif var1 == 2:
                new_data = int(input("Enter the new data to be inserted: "))
                head = insert_node_at_last(head, new_data)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                #linked list is 2->3->4->5->1 if 1 is new data

            elif var1 == 3:
                new_data = int(input("Enter the new data to be inserted: "))
                position = int(input("Enter the position where new data is to be inserted: "))
                head = insert_node_at_position(head, new_data, position)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                #linked list is 2->3->4->8->5 if 8 is new data and position if 4

            elif var1 == 4:
                print("\nExiting insert options.")
                continue

            else:
                print("Invalid choice")

        elif choice == 3:
            print("\nDelete Options:")
            print("1. Delete node at the beginning")
            print("2. Delete node at the end")
            print("3. Delete node at a specific position")
            print("4. Exit")
            var2 = int(input("Enter your choice: "))

            if var2 == 1:
                head = delete_node_infront(head)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                #linked list is 3->4->5->1 

            elif var2 == 2:
                head = delete_node_last(head)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                #linked list is 2->3->4->5

            elif var2 == 3:
                position = int(input("Enter the position to delete: "))
                head = delete_node_at_position(head, position)
                print("\nThe updated list is:", end=" ")
                print_list(head)
                #linked list is 2->4->5 if position is 2

            elif var2 == 4:
                print("\nExiting delete options.")
                continue

            else:
                print("Invalid choice")

        elif choice == 4:
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
