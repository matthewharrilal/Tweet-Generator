
class HashTable:
    def __init__(self, number_of_spots):

        # Initalizing the number of spots in the table going to be used in multiple functions
        self.number_of_spots = number_of_spots

    def create_hash_table(self):

        # Creating the table or the list with the number of spots the user passes in
        table = [None] * self.number_of_spots
        return table

    def generate_index_from_hash_code(self, hash_number):
        # Generates an index from the given hash number does not account for collisions
        index = hash_number % self.number_of_spots
        return index


    def insert_value(self, key, value):
        hash_table = self.create_hash_table()
        hash_table[self.generate_index_from_hash_code(key)] = value
        return hash_table


hash_instance = HashTable(10)
print(hash_instance.create_hash_table())
print(hash_instance.insert_value(115121212112111, "dog"))
