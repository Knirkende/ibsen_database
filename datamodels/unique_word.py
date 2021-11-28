from dataclasses import dataclass

@dataclass
class UniqueWord:
    """
    Data model corresponding to the MySQL table 'unique_word'.
    """
    word: str

    @property
    def length(self):
        return len(self.word)

    def generate_sql(self) -> str:
        #TODO
        pass