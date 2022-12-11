from typing import Tuple, List
import itertools

Board = Tuple[Tuple[str]]
Path = List[Tuple[int, int]]


class WordHuntBoard:
    def __init__(self, letters: str):
        self.original_board = {
            (i, j): letters[j * 4 + i] for i, j in itertools.product(range(4), range(4))
        }

    def get_word_path(self, word: str, start: Tuple[int, int], board) -> Path:
        if word == "":
            return ()
        possibilites = self.get_neighboring_letters(start, board)
        for i in possibilites:
            if i[0] == word[0]:
                b = board.copy()
                del b[i[1]]
                call_output = self.get_word_path(word[1:], i[1], b)
                if call_output != None:
                    return (i[1],) + call_output
        return None

    def get_word_path_origin(self, word: str):
        for key, item in self.original_board.items():
            if item == word[0]:
                b = self.original_board.copy()
                del b[key]
                path = self.get_word_path(word[1:], key, b)
                if path != None:
                    return (key,) + path
        return None

    def get_neighboring_letters(
        self, position: Tuple[int, int], board: Board
    ) -> List[Tuple[str, Tuple[int, int]]]:
        outputs = []
        x, y = position
        positions = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]
        for position in positions:
            if position in board:
                outputs.append((board[position], position))
        return outputs


class WordHuntIterator:
    def __init__(self, words: List[str], letters: str, is_sorted: bool = False):
        self.board = WordHuntBoard(letters)
        if is_sorted:
            sorted_words = words
        else:
            sorted_words = sorted(words, key=len, reverse=True)
        self.words = iter(sorted_words)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            word = next(self.words)[:-1]
            output = self.board.get_word_path_origin(word)
            if output == None:
                continue
            return (output, word)


def main():
    file = open("letters10.txt", "r")
    words = iter(sorted(file.readlines(), key=len, reverse=True))
    iterator = WordHuntIterator(words, input("Give me letters: "))
    for i in iterator:
        input(i[1])


if __name__ == "__main__":
    main()
