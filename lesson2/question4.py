def square_root(num_input, epsilon=1e-6):
    guess = num_input
    while True:
        if abs(num_input - guess ** 2) <= epsilon:
            return guess
        next_guess = guess - (guess ** 2 - num_input) / (2 * guess)
        guess = next_guess


if __name__ == "__main__":
    print(square_root(2))
