from passlib.hash import argon2

class argon2hash:
    def __init__(self,password,type=None,salt=None):
        self.password = password
        self.type = None
        self.salt = None

    def gen_hash(self):
        h = argon2
        if self.type:
            try:
                h.type = self.type
            except:
                pass
            
        if self.salt:
            try:
                h.salt = self.salt
            except:
                pass

        rval = {
            "hash"      : h.hash(self.password),
            "type"      : h.type,
            "salt"      : h.salt
        }

        return rval

if __name__ == "__main__":
    Argon2hash = argon2hash("T35tP@55w0rD",type="id",salt="c29tZXNhbHQ")
    print(Argon2hash.gen_hash())
