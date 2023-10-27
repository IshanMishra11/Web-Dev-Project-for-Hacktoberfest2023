import random

def generate_otp(length=6):
    # Generate a random OTP with the specified length
    otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return otp

if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
