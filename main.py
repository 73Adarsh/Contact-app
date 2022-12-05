while True:
    q = input('Display = (d), Add = (a), Search = (s), Quit = (q) : ')
    if q == 'a':
        with open('contact.txt', 'a') as f:
            name = input('Name: ')
            phone = input('Phone: ')
            f.writelines((name,' : ',phone,'\n'))
    elif q == 's':
        with open('contact.txt', 'r') as f:
            search = input('Search: ')
            for i in f:
                if search in i:
                    print(i)
    elif q == 'd':
        with open('contact.txt', 'r') as f:
            for i in f:
                print(i)
    elif q == 'q':
        break
    else:
        print("Please inter a valid input")