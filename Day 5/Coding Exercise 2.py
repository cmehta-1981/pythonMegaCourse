


ips = ['100.122.133.105', '100.122.133.111']

while True:
    user_action = input("Enter the index of the IP you want: ")

    match user_action:
        case '0':
            print("you chose ", ips[0])
        case "1":
            print("you chose ", ips[1])