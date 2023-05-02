
def line(deli):
    if deli:
        message = "The line is currently:"
        # for index, name in enumerate(deli, 1):
        #     message += (f' {index}. {name}')
        for i in range(len(deli)):
            message += f' {i + 1}. {deli[i]}'
        print(message)
    else:
        print('The line is currently empty.')

def take_a_number(line, name):
    line.append(name)
    print(f'Welcome, {name}. You are number {len(line)} in line.')

def now_serving(deli):
    if deli:
        print(f'Currently serving {deli[0]}.')
        deli.pop(0)
    else:
        print('There is nobody waiting to be served!')
