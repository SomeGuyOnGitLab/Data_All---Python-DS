class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        new_plate = ''.join([char.lower() for char in licensePlate if char.isalpha()])
        plate_dict = self.dict_ret(new_plate)
        min_word = None
        for word in words:
            word_dict = self.dict_ret(word)
            if self.is_completing_word(plate_dict, word_dict):
                if min_word is None or len(word) < len(min_word):
                    min_word = word
        return min_word

    def dict_ret(self, word):
        plate_details = {}
        for char in word:
            plate_details[char] = plate_details.get(char, 0) + 1
        return plate_details

    def is_completing_word(self, plate_dict, word_dict):
        for char, count in plate_dict.items():
            if word_dict.get(char, 0) < count:
                return False
        return True
