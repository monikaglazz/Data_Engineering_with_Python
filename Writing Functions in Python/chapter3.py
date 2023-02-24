import pandas as pd
import random

# 1


def mean(data):
    print(data.mean())


def std(data):
    print(data.std())


def minimum(data):
    print(data.min())


def maximum(data):
    print(data.max())


def load_data():
    df = pd.DataFrame()
    df['height'] = [72.1, 69.8, 63.2, 64.7]
    df['weight'] = [198, 204, 164, 238]
    return df


def get_user_input(prompt='Type a command: '):
    command = random.choice(['mean', 'std', 'minimum', 'maximum'])
    print(prompt)
    print('> {}'.format(command))
    return command


# Add the missing function references to the function map
function_map = {
    'mean': mean,
    'std': std,
    'minimum': minimum,
    'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

# 2


def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b
        return subtract
    else:
        print("I don't know that one")


add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

# 3

call_count = 0


def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(
        call_count
    ))


for _ in range(20):
    my_function()


def read_files():
    file_contents = None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents = []
        with open(filename) as fin:
            file_contents.append(fin.read())

    for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
        save_contents(filename)

    return file_contents


print('\n'.join(read_files()))


def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print('Work done? {}'.format(done))

# 4


def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))
    return new_func


my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
    my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

# 5


def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(5, 10)
