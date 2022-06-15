import os

env_variable = input("Variable:")
env_value = input("Value:")

os.environ[env_variable] = env_value
print(f"{env_variable} was set to {env_value}")