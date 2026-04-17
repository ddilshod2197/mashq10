while True:
    print("1. Qo'shish | 2. Ayirish | 3. Ko'paytirish | 4. Bo'lish | 5. Chiqish")
    tanlov = input("Tanlang: ")
    
    if tanlov == "5":
        break
    
    a = float(input("1-son: "))
    b = float(input("2-son: "))
    
    if tanlov == "1":
        print(f"Natija: {a + b}")
    elif tanlov == "2":
        print(f"Natija: {a - b}")
    elif tanlov == "3":
        print(f"Natija: {a * b}")
    elif tanlov == "4":
        if b != 0:
            print(f"Natija: {a / b}")
        else:
            print("0 ga bo'lish mumkin emas!")
