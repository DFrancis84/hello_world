def get_user_input():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")

    print(f'Hello {first_name} {last_name}! Welcome to Code Louisville - Monday Night Python Class')


def main():
    get_user_input()


if __name__ == "__main__":
    main()
