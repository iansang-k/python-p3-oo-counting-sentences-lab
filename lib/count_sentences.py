#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value  # This uses the setter below
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        if not self.value:
            return 0
        
        
        temp = self.value.replace('?', '.').replace('!', '.')
        
        sentences = [s for s in temp.split('.') if s.strip()]
        return len(sentences)
