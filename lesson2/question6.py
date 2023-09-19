def square_root(num_input, epsilon=1e-6):
    guess = num_input / 4
    while True:
        if abs(num_input - guess ** 2) <= epsilon:
            return guess
        next_guess = guess - (guess ** 2 - num_input) / (2 * guess)
        guess = next_guess


if __name__ == "__main__":
    print(square_root(2))
# g=c/2 1.4142135623746899
# g=c 1.4142135623746899
# g=c/4 1.4142135625249321
# 有影响
