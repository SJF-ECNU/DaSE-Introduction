def cubic_root(num, epsilon=1e-6, max_times=1000):
    guess = num
    for i in range(0, max_times):
        new_guess = guess - (guess ** 3 - num) / (3 * guess ** 2)
        if abs(guess - new_guess) < epsilon:
            return guess
        guess = new_guess
    return guess


if __name__ == "__main__":
    num_input = float(input("请输入要开三次根的数字："))
    cubic_root_result = cubic_root(num_input)
    print(f"开三次方根的近似值: {cubic_root_result}")
