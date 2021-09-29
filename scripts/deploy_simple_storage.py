from brownie import accounts, SimpleStorage, network, config

def deploy_simple_storage():
  account = get_account()

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


def get_account():
  if (network.show_active == 'development'):
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])


def main():
  deploy_simple_storage()