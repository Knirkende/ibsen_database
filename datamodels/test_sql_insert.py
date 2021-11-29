from .play import Play
from .unique_word import UniqueWord
from .sql_insert import play_insertion, unique_word_insertion

import unittest

"""
SQL code format for Play class:

INSERT INTO play (play_id, title, year, description)
  VALUES (Play.play_id, Play.title, Play.year, Play.description);

***

SQL code format for UniqueWord class:

INSERT INTO unique_word (word, word_length, play_id)
  VALUES (UniqueWord.word, UniqueWord.length, Play.play_id);

"""

class TestPlayInsert(unittest.TestCase):
    """Test the SQL code generated by the function play_insertion"""

    def SetUp(self):
        """Initialize instance of Play class"""
        self.gengangere = Play(1, 'Gengangere', 1882, 'Test description')

    def test_sql(self):
        query = play_insertion(self.gengangere)
        expected = "INSERT INTO play (play_id, title, year, description) VALUES (1, 'Gengangere', 1882, 'Test description);"
        self.assertEqual(query, expected)

class TestUniqueWordInsert(unittest.TestCase):
    """Test the SQL code generated by the function unique_word_insertion"""

    def SetUp(self):
        """Initialize instance of UniqueWord class"""
        self.skinkesteg = UniqueWord(word = 'Skinkesteg', play_id = 1)

    def test_sql(self):
        query = play_insertion(self.gengangere)
        expected = "INSERT INTO unique_word (word, word_length, play_id) VALUES ('Skinkesteg', 10, 1);"
        self.assertEqual(query, expected)

        