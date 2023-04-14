from argon2 import PasswordHasher
from argon2 import exceptions as argon2Exceptions
try:
    from app.helpers.rndpwd import randpwd
except:
    from rndpwd import randpwd

class argon2hash:
    def __init__(self,password=None):
        self.password = password if password else randpwd().generate()
        self.ph = PasswordHasher()
    def generate(self):
        self.ph = PasswordHasher()
        self.hash = self.ph.hash(self.password)
        rval = {
            "password"  : self.password,
            "hash"      : self.hash
        }
        return rval
class argon2verify:
    def __init__(self,argon_hash,password):
        self.hash = argon_hash
        print(self.hash)
        self.password=password
        print(self.password)

        self.ph = PasswordHasher()
        print("Initialized PasswordHasher()")

    def verify(self):
        output = None
        try: 
            self.ph.verify(self.hash,self.password)
            output = True
        except (argon2Exceptions.VerifyMismatchError, argon2Exceptions.VerificationError):
            output = False
        return output

if __name__ == "__main__":

    print("\n###############################\n Random Password & Verify\n###############################")
    password = randpwd.generate()
    badpassword = "NotThePassword"
    print(password)
    hash = argon2hash(password=password).generate()["hash"]
    print(hash)
    print(f"{password}: {PasswordHasher().verify(hash,password)}")
    print(f"{badpassword}: {argon2verify(hash,badpassword).verify()}")
    print("###############################\n\n")
    print("###############################\n  Password='P@5Sw0Rd' & Verify\n###############################")
    password="P@5Sw0Rd"
    hash=argon2hash(password=password).generate()["hash"]
    print(hash)
    print(PasswordHasher().verify(hash,"P@5Sw0Rd"))
    print(f"{password}: {PasswordHasher().verify(hash,password)}")
    print(f"{badpassword}: {argon2verify(hash,badpassword).verify()}")