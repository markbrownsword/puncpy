import unittest.mock
from puncpy.common import process_tagged_text


class CommonTestCase(unittest.TestCase):
    # Tests for `common.py`

    @unittest.mock.patch('sys.stdout')
    def test_process_tagged_text(self, mock_stdout):
        # Arrange
        text = [('This', 'DT'), ('is', 'VBZ'), ('my', 'PRP$'), ('own', 'JJ'), ('invention', 'NN')]

        # Act
        process_tagged_text(text)

        # Assert
        self.assertEqual(10, mock_stdout.write.call_count)