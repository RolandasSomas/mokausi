"""
Sukurti klasę, kurioje atributas butu "text".

Sukurti metodus, kurie:
1. Suskaičiuotų kiek yra žodžių tekste;
2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame.
Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;

Prasau pagalvoti ar Jūsų sprendime nėra kodo dubliavimo ir pagalvokite kaip jo išvengti.
"""


class Issrinkimas:
    def __init__(self, text=str):
        self.text = text

    # def split_text(self):
    #     return self.text.split()
    def how_many_words(self, text=str):
        return len(text.split())

    def find_words(self, text, letters="ao"):
        result = []
        for word in text.split():
            if all(letter in word for letter in letters):
                result.append(word)
        return result

    def find_words_with_length(self, length=8):
        result = []
        words = text.split()
        for i in words:
            if len(i) >= length:
                result.append(i)
        return result


text = "Metoda, example, games, examskuris , as, baba, gražintų visus žodžius, kurie būtų nurodyti metodo, koda kintamajame."
isrinkimas = Issrinkimas()
print(isrinkimas.how_many_words(text))
print(isrinkimas.find_words(text))
print(isrinkimas.find_words_with_length(3))
