def find_last_alphabetical_word():
 
    wr1 = input("Enter a word: ")
    wr2 = input("Enter a 2nd word: ")
    wr3 = input("Enter a 3rd word: ")


    words = [wr1.lower(), wr2.lower(), wr3.lower()]


    last_word = max(words)


    print(f"The word that comes last alphabetically is: {last_word}")



find_last_alphabetical_word()
