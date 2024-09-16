import bcrypt

password = 'test_password'
hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print(hash_password)

password_check = 'test_password'
if bcrypt.checkpw(password_check.encode(), hash_password):
    print('OK')
else:
    print('NO')
