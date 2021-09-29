from brownie import accounts, SimpleStorage

def deploy_simple_storage():
  account = accounts[0]

  simple_storage_contract = SimpleStorage.deploy({ "from": account })
  
  # retrieve
  stored_value = simple_storage_contract.retrieve()
  print(stored_value)

  # update stored value
  tx = simple_storage_contract.store(15, { "from": account })
  tx.wait(1)

  # retrieve updated value
  updated_stored_value = simple_storage_contract.retrieve()
  print(updated_stored_value)

def main():
  deploy_simple_storage()