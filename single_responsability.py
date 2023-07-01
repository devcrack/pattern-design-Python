class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

if __name__ == '__main__':
    j = Journal()
    j.add_entry("I have passed for my amazon package")
    j.add_entry("I was with my mom today in the morning")
    print(f'Journal entries:\n{j}')

    # Using the PersitenceManager class
    print("\n========================================================\n")
    PersistenceManager.save_to_file(j, r'./temp.txt')

    with open(r"./temp.txt") as fh:
        print(fh.read())

