CREATE TABLE olympic_games (
    id integer,
    calendar_year integer,
    season text,
    city text
);

CREATE TABLE athletes (
    id integer,
    given_name text,
    country text,
    noc text
);

CREATE TABLE medals (
    id integer,
    noc text,
    medal text
);