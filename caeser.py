from caeser_art import logo
print(logo)
def ceaser(original_text,shift_amount,encode_or_decode):
    info=""
    if encode_or_decode=="decode":
            shift_amount*=-1 
    for letter in original_text:
        position = alphabet.index(letter) + shift_amount
        position %=  len(alphabet)
        info += alphabet[position]
    print(f"Here is the encoded result:{info}")    

should_continue=True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("Type 'yes' to continue and Type 'no'to exit:\n").lower()
    if restart=="no":
         should_continue=False
         

