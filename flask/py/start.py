import datasend


def Start():

    # Give the user some context.
    print("\nWelcome to the nature center. What would you like to do?")

    # Set an initial value for choice other than the value for 'quit'.
    choice = ''

    # Start a loop that runs until the user enters the value for 'quit'.
    while choice != 'q':
        # Give all the choices in a series of print statements.
        print("\n[1] Start Bot")

        print("[q] Enter q to quit.")

        # Ask for the user's choice.
        choice = input("\nWhat would you like to do? ")

        # Respond to the user's choice.
        if choice == '1':
            datasend.dbconnection()
            datasend.dbquestion()
            while choice != 'q':
                # Give all the choices in a series of print statements.
                print("\n[1] Anything else?")

                print("[q] Enter q to quit.")

                # Ask for the user's choice.
                choice = input("\nWhat would you like to do? ")
                if choice == '1':
                    datasend.dbquestion()
        elif choice == 'q' or 'Q':
            print("\nThanks for playing. See you later.\n")
        else:
            print("\nI don't understand that choice, please try again.\n")

    # Print a message that we are all finished.
    print("Thanks again, bye now.")


