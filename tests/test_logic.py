import pytest

from api.logic import skip_splits, extract_word, get_words


class BaseCase:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'test_{self.name}'


class SkipSplitsCase(BaseCase):

    def __init__(self, name, text, start_index, answer):
        super().__init__(name)
        
        self.text = text
        self.start_index = start_index
        self.answer = answer

        
SKIP_SPLITS_CASES = [
    SkipSplitsCase('all spaces', ' \t ', 0, 3),
    SkipSplitsCase('symbols', ';.,,?!(', 0, 7),
    SkipSplitsCase('two words', 'abgt \t! \t word2', 4, 10),
    SkipSplitsCase('empty line', '', 0, 0),
]


@pytest.mark.parametrize('case', SKIP_SPLITS_CASES, ids=str)
def test_skip_splits(case):
    answer = skip_splits(case.text, case.start_index)
    assert answer == case.answer


class ExtractWordCase(BaseCase):

    def __init__(self, name, text, start_index, finish_index, word):
        super().__init__(name)
        
        self.text = text
        self.start_index = start_index
        self.finish_index = finish_index
        self.word = word


EXTRACT_WORD_CASES = [
    ExtractWordCase('one word', 'aword', 0, 5, 'aword'),
    ExtractWordCase('first word', 'a word', 0, 1, 'a'),
    ExtractWordCase('second word', 'a word', 2, 6, 'word'),
    ExtractWordCase('split char first', '\t test', 0, 6, 'test'),
]


@pytest.mark.parametrize('case', EXTRACT_WORD_CASES, ids=str)
def test_extract_words(case):
    index, word = extract_word(case.text, case.start_index)
    assert index == case.finish_index
    assert word == case.word


class GetWordsCase(BaseCase):

    def __init__(self, name, text, words):
        super().__init__(name)

        self.text = text
        self.words = words


GET_WORD_CASES = [
    GetWordsCase('empty', '', []),
    GetWordsCase('one word', 'oneword', ['oneword']),
    GetWordsCase('two words', 'one word', ['one', 'word']),
    GetWordsCase('split characters', '\t one ??? word! yahoo)', ['one', 'word', 'yahoo']),
]


@pytest.mark.parametrize('case', GET_WORD_CASES, ids=str)
def test_get_text(case):
    words = get_words(case.text)
    for word, case_word in zip(words, case.words):
        assert word == case_word
