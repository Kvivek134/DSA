class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new_node

	def delete(self, data):
		if self.head is None:
			print("List is empty.")
			return

		if self.head.data == data:
			self.head = self.head.next
			print(f"{data} deleted.")
			return

		current = self.head
		while current.next is not None and current.next.data != data:
			current = current.next

		if current.next is None:
			print(f"{data} not found.")
			return

		current.next = current.next.next
		print(f"{data} deleted.")

	def display(self):
		if self.head is None:
			print("List is empty.")
			return

		current = self.head
		while current is not None:
			print(current.data, end=" -> ")
			current = current.next
		print("None")


linked_list = SinglyLinkedList()

while True:
	print("\n1. Insert")
	print("2. Delete")
	print("3. Display")
	print("4. Exit")

	try:
		choice = int(input("Enter your choice: "))
	except ValueError:
		print("Please enter a number from 1 to 4.")
		continue

	match choice:
		case 1:
			try:
				value = int(input("Enter value to insert: "))
			except ValueError:
				print("Please enter a valid integer.")
				continue
			linked_list.insert(value)
			print(f"{value} inserted.")
		case 2:
			try:
				value = int(input("Enter value to delete: "))
			except ValueError:
				print("Please enter a valid integer.")
				continue
			linked_list.delete(value)
		case 3:
			linked_list.display()
		case 4:
			print("Program ended.")
			break
		case _:
			print("Invalid choice. Please select 1 to 4.")
 