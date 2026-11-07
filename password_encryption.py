class PasswordEncryption:

    def _init_(self, password):
    
        self.password = password

    def encrypt(self):
    
    new_password_list = []
    
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for character in self.password:
    
        located = False         
    
        for count in range(26):
        
                if character == lowercase_alphabet[count]:
                
                    new_index = (count + 13) % 26
                    
                    new_password_list.append(lowercase_alphabet[new_index])
                    
                    located = True
                    
                    break
                    
        if not located:
        
            for count in range(26):
        
                if character == uppercase_alphabet[count]:
                
                    new_index = (count + 13) % 26
                    
                    new_password_list.append(uppercase_alphabet[new_index])
                    
                    located = True
                    
                    break

        if not located:
        
            new_password_list.append(character)
                    
