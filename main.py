while True:
    name = input("Enter name: ")
    if name == "stop":
        break
    lastname = input("Enter username: ")
    age = int(input("Enter age: "))
    if age < 0:
        print("Yoshingiz qabul qilindi✅")
    elif age != int(age):
        print("Yosh butun son bolishi lozim")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if phone.startswith("+998"):
        print("Ma'lumotlaringiz qabul qilindi✅")
    else:
        print("Telefon nomerni xato kiritdingiz iltimos ma'lumotlarni qaytadan kiriting")

def generate_user_id():
    global user_id
    user_id += 1
    return user_id

if __name__ == "__main__":
    user_id = 1000
    new_user_id = generate_user_id()


with open("users_info.txt", "w") as file:
    file.write(f"ID--> {new_user_id}\n")
    file.write(f"Ism--> {name}\n")
    file.write(f"Familiya--> {lastname}\n")
    file.write(f"Yosh--> {age}\n")
    file.write(f"Telefon--> {phone}\n")
    file.write(f"Email--> {email}\n")
    file.write(f"Manzil--> {address}\n")

print("Ma'lumotlar faylga yozildi.")