import string
import random
a=string.ascii_letters+string.digits+string.punctuation
le=int(input("enter length of password : "))
def gen_pwd(le):
    return random.choices(a,k=le)
b=gen_pwd(le)
print("your password is","".join(b))
