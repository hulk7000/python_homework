from DB_database import User_record, Money_record


def get_money():

    player_name = input("Enter your name: ")


    pre_balance = User_record.get_latest_balance(player_name)


    print(f"\nBefore Balance: {pre_balance}")


    while True:

        try:

            amount = int(
                input("Enter money amount to add: ")
            )


            if amount <= 0:

                print("Amount must be greater than 0.")

                continue


            break


        except ValueError:

            print("Enter a valid number.")



    new_balance = pre_balance + amount



    User_record(
        player_name,
        amount
    ).update_balance()



    Money_record(

        player_name,

        amount,

        pre_balance,

        new_balance,

        "Deposit"

    ).add_info()



    print("\n💰 Money added successfully!")

    print(f"New Balance: ${new_balance}")