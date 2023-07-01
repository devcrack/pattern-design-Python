# SRP 
For example if you have a class, the class should have its primary responsibility
whatever it's meant to be doing, and it not should on take on other responsibilities
Let's take a look to the following code:

```python
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
```
So far so good because the main responsibility is storing
and removing entries of the Journal class. Everything is fine for now. 

Now if we add more functionality to the class
```python
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

    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


```
The problem here is that we have added a secondary responsibility to the 
journal class. Now not only does the journal just store entries and allow 
us to manipulate the entries, but it's now taking on the responsibility 
of data persistence by providing functionality for saving and loading the 
journal from particular resources. So you want to take the responsibility 
of persistence, and you want to stick it to a separate class. 
```python
class PersistenceManager:
    
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
```

In resume, you don't want to overload your objects with too many 
responsibilities

[Full coded example](./single_responsability.py)
