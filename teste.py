import hashlib

encoded = '12345'.encode()
result = hashlib.sha256(encoded)
print(result.hexdigest())