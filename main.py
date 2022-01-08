#This is a simple morse code converter, all you need to do is enter a command line input and the result will be in morse code!,enjoy!

output = " "
def english_morse_converter (input,output):
    # Iterate over index
    for element in range(0, len(input)):
        if input[element] == ' ':
            output+= ' '
            continue
        character_in_english = input[element]
        character_in_morse = english_alphabet.index(character_in_english)
        output += morse_alphabet[character_in_morse]
    print(output)
    return


morse_alphabet = ["·−", "−···", "−·−·", "−··" ,"·",
"··−·","−−·", "····", "··", "·−−−", "−·−", "·−··", "−−", "−·",
"−−−", "·−−·", "−−·−" ,"·−·", '···', "−", "··−",
"···−", "·−−" ,"−··−" ,"−·−−", "−−··" ]

english_alphabet = ['a','b','c','d','e','f','g',
                    'h','i','j','k','l','m','n','o','p',
                    'q','r','s','t','u','v','w','x','y','z']

input = input("Please enter a string of characters: ").lower()

english_morse_converter(input,output)