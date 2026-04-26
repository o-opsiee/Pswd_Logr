def otw_logger() :

    try:
        level = int(input("Level: "))
        pswd = input("Pass.: ")
        
        with open("bandit.txt", "a") as f:
            f.write(f"#{level}     {pswd}\n")
    except ValueError:
        print("Value Error, duh!")

otw_logger()