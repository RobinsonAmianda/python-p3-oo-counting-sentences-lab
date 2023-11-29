#!/usr/bin/env python3

class MyString:
  def __init__(self,value = []):
    self.value = value
  def get(self):
    return self.value
  def set(self,string_value):
    self.string_value = string_value
    if self.value == str:
      self.value = self.string_value
    else:
        print("The value must be a string.")
  property(get,set)

  def is_sentence(self):
    return self.value(".")
  def is_question(self):
    return self.value("?")
  def is_exclamation(self):
    return self.value("!")
  def count_sentences(self):
    return  self.value == self.string_value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)
     
