import unittest.mock
from puncpy.tagger import Tagger


class TaggerTestCase(unittest.TestCase):
    # Tests for `tagger.py`

    @unittest.mock.patch('puncpy.tagger.word_tokenize', return_value=['This', 'is', 'my', 'own', 'invention'])
    @unittest.mock.patch('puncpy.tagger.pos_tag', return_value=[('This', 'DT'), ('is', 'VBZ'), ('my', 'PRP$'), ('own', 'JJ'), ('invention', 'NN')])
    def test_tag_text(self, pos_tag_mock, word_tokenize_mock):
        # Arrange
        tagger = Tagger('This is my own invention')

        # Act
        result = tagger.tag_text()

        # Assert nltk.word_tokenize received correct input
        args, kwargs = word_tokenize_mock.call_args_list[0]
        assert args == ('This is my own invention',)

        # Assert nltk.pos_tag received correct input
        args, kwargs = pos_tag_mock.call_args_list[0]
        assert args == (['This', 'is', 'my', 'own', 'invention'],)

        # Assert tag_text output
        self.assertTrue(len(result) == 5)

