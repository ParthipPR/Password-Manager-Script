OWLimport string #need to add data encription


def password_finder():
    userid = input('Enter the user id :')
    with open('data.txt') as data:
        dataPresent = data.readlines()
        Data_lines = list(dataPresent)
        for i in dataPresent:
            entry =list(i.split())
            if entry[0] == userid:
                print(entry[1])
            else:
                pass

def password_writer():
    userid = input('Enter the User Id :')
    password = input('Enter the Password :')
    entry =  userid+' '+password
    with open('data.txt') as data:
        dataPresent = data.read()
    with open('data.txt','wt') as data:
        data.writelines(dataPresent+entry+'\n')

def password_manager():
    print('*'*50)
    print('PASSWORD MANAGER')
    print('Enter 1 to enter new userid and password')
    print('Enter 2 to veiw existing password')
    print('Enter 3 to veiw all the password')
    print('*'*50)

    response = int(input('enter the option:'))

    if response == 1:
        password_writer()
    elif response == 2:
        password_finder()
    elif response == 3:
        with open('data.txt') as file:
            data =  file.read()
            print(data)
    else:
        print('Please enter the valid option')
wantToContinue = 'y'
while wantToContinue == 'y':
    master_password = input('Enter the password:')
    if master_password == 'owlboy':
        password_manager()
    else:
        print('wrong password')
    wantToContinue = input('do you want to continue?(y/n):')

