from utils.utils import *

def main():
    _saved_password1 = get_password()

def get_password(filename):
        fin = open(filename, 'r')
        old_password = fin.readline()[:-1]
        fin.close()
        return old_password

def change_password_value(filename):
        fout = open(filename, 'w')
        _new_password = get_random_uuid(9)
        fout.write(_new_password+'\n')
        fout.close()

if __name__ == "__main__":
    main()
