class Contact:
    '''
    Contact class to represent a contact with a name and number.
    '''

    def __init__(self, name: str, number: str):
        # -------------
        # Attributes:
        # -------------
        self.name = name           # Contact name
        self.number = number       # Contact phone number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.

    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value: Contact):
        # -------------
        # Attributes:
        # -------------
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.

    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size  # Array to hold linked lists

    def hash_function(self, key: str) -> int:
        """
        Convert a string key into an integer index.
        The hash value is based on summing the ASCII values of the key's characters.
        """
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key: str, number: str):
        """
        Insert a new contact into the hash table.
        If the contact name already exists, update the phone number.
        """
        index = self.hash_function(key)
        contact = Contact(key, number)

        if self.data[index] is None:
            self.data[index] = Node(key, contact)
        else:
            # Collision occurred; traverse the linked list
            current = self.data[index]
            while current is not None:
                if current.key == key:
                    current.value.number = number  # Update existing number
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, contact)

    def search(self, key: str):
        """
        Search for a contact by name.
        Returns the Contact object if found, otherwise None.
        """
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        """
        Print the contents of the hash table, showing all contacts at each index.
        """
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                chain = ""
                while current is not None:
                    chain += f"- {current.value} "
                    current = current.next
                print(f"Index {i}: {chain.strip()}")


# ----------------------------
# Testing Section
# ----------------------------
if __name__ == "__main__":
    # Create a hash table with 10 slots
    table = HashTable(10)

    # Initial table (all empty)
    print("Initial Table:")
    table.print_table()

    # Add contacts
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    print("\nAfter Adding John and Rebecca:")
    table.print_table()

    # Add more to test collisions
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # May may collide with Amy
    print("\nAfter Adding Amy and May (Collision Test):")
    table.print_table()

    # Update Rebecca’s number
    table.insert("Rebecca", "999-444-9999")
    print("\nAfter Updating Rebecca's Number:")
    table.print_table()

    # Search for existing contact
    contact = table.search("John")
    print("\nSearch result:", contact)

    # Search for non-existing contact
    print("\nSearch for missing contact (Chris):", table.search("Chris"))

# ------------------------
# Design Memo
# ------------------------
# Why is a hash table the right structure for fast lookups?
# A hash table is ideal for fast lookups because it uses a hash function to convert a key directly into an index, allowing data to be accessed in
# constant time O(1). This makes it much faster than a list, which requires searching each element, or a tree, which requires multiple comparisons
# to locate a node.

# How did you handle collisions?
# In this implementation, collisions are handled through separate chaining. Each position in the hash table contains a linked list  of Node objects.
# If two names hash to the same index, the new contact is added to the end of the chain. If a contact with the same name already exists, its phone 
# number is updated instead of creating a duplicate. Ensuring data consistency while maintaining efficient insertion and retrieval.

# When might an engineer choose a hash table over a list or tree?
# Engineers could choose a hash table over lists or trees when quick access, insertion, and updates are required without caring about maintaining order. 
# For example, a contact management system benefits from this structure since users frequently search and modify entries by name. Hash tables provide a 
# simple and efficient solution for managing large sets of key-value pairs.