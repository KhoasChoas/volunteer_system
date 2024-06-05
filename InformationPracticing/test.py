import uuid
from werkzeug.security import generate_password_hash,check_password_hash


if __name__ == '__main__':
    print(uuid.uuid4())

    pwd = '12345678910'
    _pwd = generate_password_hash(pwd)
    print(_pwd)
    print(check_password_hash(_pwd, pwd))

