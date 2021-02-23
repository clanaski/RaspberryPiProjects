Question1 = input ("Who is the President of the United States?")
while Question1 != "Joe Biden":
    print("Wrong! Try again!")
    Question1 = input ("Who is the President of the United States?")
print ("Correct!")
Question2 = input ("How many times do you brush your teeth a day?")
while Question2 < "2":
    print ("Thats just nasty!")
    Question2 = input ("You might want to go brush them again then...how many times SHOULD you brush your teeth?")
print("White and Bright!!")