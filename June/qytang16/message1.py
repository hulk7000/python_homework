def letter(to,item,fromname):
    templite = (f"Dear {to},\n"
                f"Thank you for your recent purchase of {item}.\n"
                f"Remember, our support team is always here to assist you.\n"
                f"Best regards,\n"
                f"{fromname}")
    return templite
print(letter("bob","lego","jimmy"))