class Solution(object):
    def uniqueMorseRepresentations(self, words):
        data = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformed_words = {}
        for word in words:
            transformed = ''
            for char in word:
                transformed = transformed + data[ord(char)-ord('a')]
            if transformed not in transformed_words.keys():
                transformed_words[transformed] = 1
            else:
                temp = transformed_words[transformed]
                transformed_words[transformed] = temp+1
        return len(transformed_words.keys())
        
