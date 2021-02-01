import  random
pass_len = int(input("Enter the length of Password: "))
strength = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(strength,pass_len))
print(p)