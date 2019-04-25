
with open('keys.txt', 'r') as f:
    keys = f.read().splitlines()

infura_key = keys[0]
private_key = keys[1]