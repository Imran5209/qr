import qrcode as qr

while True:
    print ('1. Link')
    print ('2. Text')
    choice = int(input('Choose 1 or 2: '))

    if choice == 1:
        Link = input('Enter Your Link: ')
        img = qr.make(Link)
    elif choice == 2:
        Text = input('Enter Your Text: ')
        img = qr.make(Text)
    else:
        print('Something Went Wrong')
    File_Name = input('Enter File Name: ')
    img.save(f'{File_Name}.png')
    print('Complete \n')