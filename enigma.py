import sys

#lexicon of actual rotors used in Army and Navy Enigmas 
lexicon_rotor_I    = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'] 
lexicon_rotor_II   = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
lexicon_rotor_III  = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
lexicon_rotor_IV   = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
lexicon_rotor_V    = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
lexicon_rotor_VI   = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W']
lexicon_rotor_VII  = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T']
lexicon_rotor_VIII = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']
lexicon_beta       = ['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M','D','R','T','A','K','Z','G','F','U','H','O','S']
lexicon_gamma      = ['F','S','O','K','A','N','U','E','R','H','M','B','T','I','Y','C','W','L','Q','P','Z','X','V','G','J','D']

#lexicon of actual reflectors
lexicon_reflector_A = ['E','N','K','Q','A','U','Y','W','J','I','C','O','P','B','L','M','D','X','Z','V','F','T','H','R','G','S']
lexicon_reflector_B = ['R','D','O','B','J','N','T','K','V','E','H','M','L','F','C','W','Z','A','X','G','Y','I','P','S','U','Q']
reflector_list = [lexicon_reflector_A, lexicon_reflector_B]#This is used when seting up the machine

#Setup machine
box_of_rotors = [lexicon_rotor_I, lexicon_rotor_II, lexicon_rotor_III, lexicon_rotor_IV, lexicon_rotor_V, lexicon_rotor_VI, lexicon_rotor_VII, lexicon_rotor_VIII,lexicon_beta, lexicon_gamma]


    
def use_plugboard(plugboard_setup, user_input):
    return plugboard_setup[char_to_index(user_input)]

def plugboard():# generates plugboard
    print("How many pairs of letters would you like to swap?")
    pairs = get_int()
    lexicon=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for count in range(0,pairs):
        lexicon=swap_pairs(lexicon)
    print(lexicon)
    return lexicon 

def swap_pairs(lexicon): #Transposition of alphabet
    print("First letter: ")
    letter1 = get_char()
    print("Second letter: ")
    letter2= get_char()
    p= char_to_index(letter1)
    q= char_to_index(letter2)
    temp=lexicon[p]
    lexicon[p] = lexicon[q]
    lexicon[q] = temp
    return lexicon

def char_to_index(letter): #For calculating the index based on the letter's character value  
    temp = ord(letter)-65
    return temp

def index_to_char(number): #for changing index in the lexicon of a character back to a character
    temp = chr(number + 65)
    return temp

def get_int():
    while True:
        input_int = input()
        input_int = int(input_int)
        if input_int <= 26:
            return (input_int)
        else:
            print("Error: Choose a number from the set")            

def get_char(): #user input for character
    while True:
        input_string = input().upper()
        if len(input_string) == 1:
           y = ord(input_string)
           if y <= 90 and y >= 65:
                return (input_string)
        else:
            print("ERROR: Type 1 letter") #in case the user types in the wrong value
    return(y)

def get_military(): #Germany had two different enigmas in military: Navy- 4 rotors and Army 3 rotors
    print("Are you the Navy?  Y/N")
    x = get_char()   
    if (x == 'Y' or  x == 'y' or x == 'yes' or x == 'Yes'):
        return 'navy'
    elif (x == 'N' or x =='n' or x =='no' or x == 'No'):
        print("Are you the Army?")
        y = get_char()
        if (y == 'Y' or y == 'y' or y == 'Yes' or y == 'yes'):
            return 'army'
        else: 
            print("You must be a Ally spy!")
            sys.exit(1)
        

class rotor: #Creates object: Rotor which can be manipulated by its given wiring, rotor number, position for starting position, and iteration
    def __init__(self, lexicon, rotor_number, starting_position):
        self.wiring = lexicon 
        self.position = starting_position
        self.iteration = 0
        self.rotor_number = rotor_number
    def set_position(self, init_int):
        self.position = init_int
    def encrypt(self, init_char, rotated, reflected = 0): #the actual encryption
        if rotated == 1: #a particular rotor rotates until it does a full rotation,
                         #when the full rotation is accomplished that rotor no longer rotates and the next rotor rotates 
            self.position = self.position + 1
        if reflected != 0: 
            for i,c in  enumerate(self.wiring): #iterate through each letter but 
                if c in init_char:              #then give a pair of the letter and it's number in order
                    i = (i - self.position)%26
                    encrypt_char = index_to_char(i)
                    break
        else:
            index = (char_to_index(init_char) + self.position)%26
            encrypt_char = self.wiring[index]
        
        if self.position > 25:
            rotate_next = 1 #dictates when a rotor rotates
        else:
            rotate_next = 0 #dictates when a rotor does not rotate
        self.position = ((self.position)%26) #use of modular arthimetics
     
        return (encrypt_char, rotate_next)#returns a tuple so that the next letter in the
                                          #string can be takenin and the appropriate rotor knows if it should rotate
    
def get_rotors(): #User input to get the rotors and set up the machine
    military_branch = get_military()
    if military_branch == 'army':
        print("Choose 3 rotors from the set of I to X")
        number_of_rotors = 3
    else:
        print("Choose 4 rotors from the set of I to X")
        number_of_rotors = 4
        
    print("Which rotors would you like (1-10)? Order from fastest to slowest ")
    rotor_choice_list = []
    for i in range(0, number_of_rotors):
        print("Choose rotor for slot " , i + 1)
        rotor_choice = get_int()    
        print("Choose starting position of rotor (a number 1 to 26) ")
        start_position = get_int()
        if (start_position in range(1,26)):
            #print( rotor_choice, start_position )
            tmp = rotor(box_of_rotors[rotor_choice - 1], rotor_choice, start_position)
            rotor_choice_list.append(tmp) 

    print("These are the rotors you chose ") #just a statement to remind the user which rotors they chose
    for r in rotor_choice_list:
        print (r.rotor_number, end=' ')
    return rotor_choice_list

def get_reflector(): #user input to chose which reflector
    while True:
        reflector_choice = input("\nChoose Reflector A or B: ").upper()
        try:
            if reflector_choice == 'A':
                return rotor(reflector_list[0], reflector_choice, 0)
        
            if reflector_choice == 'B':
                return rotor(reflector_list[1], reflector_choice, 0)
        except:
            print("Error: Please type A or B")

def get_string(): #User input to encrypt
    return (input("Enter a message to encrypt: ").upper())

def message_to_encrypt(): #sending string to encrypt function in rotor class
        return (get_string().replace(" ",""))
       
def main():
    print("Thank you for using the Engima Machine today. You will set up your plugboard,")
    print("choose rotors, and choose a reflector before you encrypt or decrypt your message. Good Luck!")
    plugboard_setup = plugboard()
    rotor_list = get_rotors()
    reflector = get_reflector() 
    cipher_choice= message_to_encrypt()
    
    for s in cipher_choice: #for some character in the message i want to encrypt
        temp = use_plugboard(plugboard_setup, s)
        rotatenext = 1
        
        for r in rotor_list:
            (temp, rotatenext) = r.encrypt(temp,rotatenext) #encrypt the temp variable through the plugboard and the assigned rotors  
        (temp, rotatenext) = reflector.encrypt(temp,0) #this sends the letter through the reflector
       
        for r in reversed(range(len(rotor_list))): #This goes through the rotors in reversed order 
            (temp, rotatenext) = rotor_list[r].encrypt(temp, 0, 1)
           
        temp = use_plugboard(plugboard_setup,temp) #back through the plugboard 
        print(temp, end = ' ') #the lampboard
        

if __name__ == "__main__":
    print("Would you like to set up your Enigma Machine? ")
    answer = get_char()
    while(answer == "Yes" or answer == "Y" or answer == "Y"):
        main()
        print("\nWould you like to set up another Enigma Machine? ")
        answer = get_char()
    else:
        print("OK")
        sys.exit(1)

    
