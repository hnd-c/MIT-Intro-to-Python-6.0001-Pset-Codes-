# Problem Set 4B
# Name: <Hem N Chaudhary>
# Collaborators:
# Time Spent: a couple of days
# Late Days Used: x

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_digit_shift(input_shift, decrypt):
    '''
    calculate the digit shift based on if decrypting or not
    decrypt: boolean, if decrypting or not
    Returns: digit_shift, the digit shift based on if decrypting or not
    '''
    if decrypt:
        digit_shift = 10 - (26-input_shift)%10
    else:
        digit_shift = input_shift
    return digit_shift

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=input_text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        copy_valid_word=self.valid_words[:]
        return copy_valid_word

    def make_shift_dict(self, input_shift, decrypt=False):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter and number.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift, as well as
        every number to one shifted down by the same amount. If 'a' is
        shifted down by 2, the result is 'c' and '0' shifted down by 2 is '2'.

        The dictionary should contain 62 keys of all the uppercase letters,
        all the lowercase letters, and all numbers mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet and every number (0 <= shift < 26)

        decrypt: if the shift dict will be used for decrypting. affects digit shift function

        Returns: a dictionary mapping letter/number (string) to
                 another letter/number (string).
        '''
        dictionary={}
        for i in range(len(string.ascii_lowercase)): #Generating dictionary of lower case letters shifted by input_shift
            dictionary[string.ascii_lowercase[i]]=string.ascii_lowercase[(i+input_shift)%26]
        
        for i in range(len(string.ascii_uppercase)): #Generating dictionary of higher case letters shifted by input_shift
            dictionary[string.ascii_uppercase[i]]=string.ascii_uppercase[(i+input_shift)%26]
        
        for i in range(len(string.digits)): #Generating dictionary of numbers shifted by input_shift
            dictionary[string.digits[i]]=string.digits[(i+get_digit_shift(input_shift, decrypt))%10]
        
        return dictionary

    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with the shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down by some number of characters, determined by the shift
        value that shift_dict was built with.

        shift_dict: a dictionary with 62 keys, mapping
            lowercase and uppercase letters and numbers to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter/number shifted using
            the input shift_dict

        '''
        message_text=''
        for char in self.message_text:  #shifting the message according to shift_dict
            if char in shift_dict.keys():
                message_text+=shift_dict[char]
            else:                      #special characters 
                message_text+=char
        
        
        return message_text

class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self, input_text)
        self.input_text=input_text
        self.input_shift=input_shift
        
            
            

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.input_shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict=self.make_shift_dict( self.input_shift)
        copy_encry_dict=encryption_dict.copy()
        
        return copy_encry_dict

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.apply_shift(self.get_encryption_dict())

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: an integer, the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        self.input_shift=input_shift
        


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, input_text)
        self.message_text=input_text

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (26 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt
        the message (a) and the decrypted message text using that shift value
        '''
        
        dicvalue={}
        for i in range(26):
            dicvalue[26-i]=0  #initializing dictionary
            decrip_message=self.apply_shift(self.make_shift_dict(26-i, decrypt=True)) #string of decripted message
            decrip_message1=decrip_message.split() #list of decripted messages
            for char in decrip_message1:
                 d=is_word(self.valid_words,char) #checking if the words in the decripted list matches witht he word in valid_word
                 if d:
                     dicvalue[26-i]+=1
                        
        greatest=max(dicvalue.values())
        for i in dicvalue.keys():
            if dicvalue[i]==greatest:
                decrip_message=self.apply_shift(self.make_shift_dict(i, decrypt=True)) #applying the shift with greates match with valid_word
                
                return (26-i,decrip_message)
            
                    
                
        
            
            
            


def test_plaintext_message():
    
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
    plaintext = PlaintextMessage('How,are you?', 2)
    print('Expected Output: Jqy,ctg aqw!')
    print('Actual Output:', plaintext.get_encrypted_message_text())
    
    
    plaintext = PlaintextMessage('Noo!!!', 5)
    print('Expected Output: Stt!!!')
    print('Actual Output:', plaintext.get_encrypted_message_text())
    
    
        
    

def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

  # This test is checking decoding a lowercase string with punctuation in it.
    encrypted = EncryptedMessage('Jqy,ctg aqw!')
    print('Expected Output:', (2, 'How,are you?'))
    print('Actual Output:', encrypted.decrypt_message())
    
    encrypted = EncryptedMessage("Qjy'x, Lt!")
    print('Expected Output:', (5, "Let's, Go!"))
    print('Actual Output:', encrypted.decrypt_message())



def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story=get_story_string()
    ans=EncryptedMessage(story).decrypt_message()
    
    return ans
 


if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_plaintext_message()
    test_encrypted_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)
    # pass

