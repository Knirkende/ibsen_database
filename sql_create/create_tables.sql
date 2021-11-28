CREATE TABLE unique_word (
    word_id INT NOT NULL AUTO INCREMENT,
    word VARCHAR(20),
    word_length INT,
    play_id INT,
    PRIMARY KEY(word_id),
    FOREIGN KEY(play_id) REFERENCES play(play_id)
);

CREATE TABLE play (
    play_id INT NOT NULL AUTO INCREMENT,
    title VARCHAR(40),
    year SMALLINT,
    description TEXT,
    PRIMARY KEY(play_id)
);