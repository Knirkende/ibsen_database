from dataclasses import dataclass

@dataclass
class Play:
    """
    Data model corresponding to the MySQL table 'play'.
    """
    play_id: int
    title: str
    year: int
    description: str

    def generate_sql(self) -> str:
        #TODO
        pass