def say_hello():
    print("Hello from function!")

print("1.This line runs no matter what.")

if __name__ == "__main__":
    print("2.This line runs only if this file is executed directly.")
    say_hello()