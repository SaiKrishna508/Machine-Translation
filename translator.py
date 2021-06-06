from translate import Translator


class Translation:

    def __init__(self, text):
        self.text = text

    def translate_word(self):
        translator = Translator(from_lang='en', to_lang='te')
        translation = translator.translate(self.text)
        return translation

# trans = translation("I am going to beach today!")
# result = trans.translate_word()
# print(result)
