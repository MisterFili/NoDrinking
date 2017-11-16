
def main():
    name = get_name()
    print('hello, {}'.format(name))

def get_name():
    return (input('please enter your name:'))

if __name__ == '__main__':
    main()
