import unittest.mock
from puncpy.apostrophe import Apostrophe


class ApostropheTestCase(unittest.TestCase):
    # Tests for `apostrophe.py`

    @unittest.mock.patch('puncpy.tagger.Tagger.tag_text', return_value=[('It', 'PRP'), ("'s", 'VBZ'), ('getting', 'VBG'), ('harder', 'RBR')])
    def test_execute(self, tag_text_mock):
        # Arrange
        apostrophe = Apostrophe()

        # Act
        result = apostrophe.execute('It\'s getting harder')

        # Assert Tagger.tag_text() was called once
        assert tag_text_mock.called and tag_text_mock.call_count == 1

        # Assert expected output is ApostropheItemCollection with one ApostropheItem...
        # TODO


# def test_execute_throws(self, tag_text_mock):
# Assert exception thrown
# self.assertRaises(ValueException, apostrophe.execute, 'It is getting harder')

