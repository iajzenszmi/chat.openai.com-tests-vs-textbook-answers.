import math

def natural_logarithm(number):
    return math.log(number)

def log_base(base, number):
    return math.log(number) / math.log(base)

if __name__ == "__main__":
    number = float(input("Enter the number to find the logarithm: "))
    ln_result = natural_logarithm(number)
    print(f"Natural logarithm of {number} is: {ln_result}")

    base = float(input("Enter the desired base for the logarithm: "))
    log_result = log_base(base, number)
    print(f"Logarithm base {base} of {number} is: {log_result}")

