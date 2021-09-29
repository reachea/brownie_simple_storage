from brownie import accounts, SimpleStorage

def test_deploy():
  # Arrange
  account = accounts[0]

  # Act
  simple_storage = SimpleStorage.deploy({ "from": account })
  initial_value = simple_storage.retrieve()
  expected = 0

  # Assert
  assert expected == initial_value

def test_update_store_simple_storage():
  # Arrange
  account = accounts[0]
  simple_storage = SimpleStorage.deploy({ "from": account })

  # Act
  update_simple_storage = simple_storage.store(15, { "from": account })
  update_simple_storage.wait(1)
  updated_simple_storage = simple_storage.retrieve()
  expected = 15

  # assert
  assert updated_simple_storage == expected