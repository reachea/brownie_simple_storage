from brownie import accounts, SimpleStorage

def read_simple_storage():
  simple_storage = SimpleStorage[0]

  stored_value = simple_storage.retrieve()
  print(stored_value)


def main():
  read_simple_storage()