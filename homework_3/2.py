import json
import hashlib
def password_hash(passsword):
    h = json.dumps(hashlib.sha256(passsword.encode()).hexdigest())
    return h
p_hash = password_hash("qwerty")
with open('password_hash.json', 'r', encoding='utf-8') as f:
    for line in f:
        if p_hash in line:
            print('хеш паролей равен')
with open('password_hash.json', 'a', encoding='utf-8') as f:
    f.write(p_hash)
    f.write(',\n')
