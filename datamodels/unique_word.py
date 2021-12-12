from dataclasses import dataclass

@dataclass
class UniqueWord:
    """
    Data model corresponding to the MySQL table 'unique_word'.
    """
    word: str
    play_id: int

    @property
    def length(self):
        return len(self.word)

    def generate_sql(self) -> str:
        insert = "INSERT INTO unique_word VALUES "

#"INSERT INTO unique_word (word, word_length, play_id) VALUES (UniqueWord.word, UniqueWord.length, Play.play_id);"
        pass