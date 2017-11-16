print('this will execute outside of main')

def main():
    
    print ("Firstmodule's Name: {}".format(__name__))

if __name__ == '__main__':
    main()

