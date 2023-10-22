-- User stories:
-- As a Maker
-- So that I can let people know what I am doing
-- I want to post a message (peep) to chitter

-- So that I can see what others are saying
-- I want to see all peeps in reverse chronological order

-- So that I can better appreciate the context of a peep
-- I want to see the time at which it was made

-- So that I can post messages on Chitter as me
-- I want to sign up for Chitter

-- Nouns: peep, time, date, 

-- Table peeps [content, datetime, user_id]
-- Table users [email, username, name, password]

-- Decide on the tables relationship
-- 1. Can one user have many POSTS? <- foregin key

DROP TABLE IF EXISTS peeps CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Table 
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content text,
  date_time text,
  user_id int
);

-- sequence of args (content, user_id, date_time)
INSERT INTO peeps (content, date_time, user_id) VALUES ('I learned SQL today, it was fun!', '2022-10-10 12:24:55', 1);
INSERT INTO peeps (content, date_time, user_id) VALUES ('What a day, 5k run done! @xAmiBa', '2022-10-17 12:24:55', 2);
INSERT INTO peeps (content, date_time, user_id) VALUES ('Boris Johnson is crazy...', '2022-10-11 18:24:55', 3);
INSERT INTO peeps (content, date_time, user_id) VALUES ('Anyone knows good restaurants in Central London?', '2022-10-14 16:24:55', 1);
INSERT INTO peeps (content, date_time, user_id) VALUES ('#partytime Happy bDay to me!', '2022-10-12 13:24:55', 2);

-- Table 2
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  username text,
  name text,
  password text
);

INSERT INTO users (email, username, name, password) VALUES ('aminaba666@gmail.com', 'xAmiBa', 'Amina Ba', 'ccb3be5cb5df7ba694a3896b09f26d7adb0cee5ffaa9ab680094d05c3fd9da8e');
INSERT INTO users (email, username, name, password) VALUES ('davidQQQ@gmail.com', 'Davido999', 'David', 'password_david777');
INSERT INTO users (email, username, name, password) VALUES ('joe_python@gmail.com', 'Crazy_Joe', 'Joe Smith', 'password_joe8!');


-- Write file into database in terminal
-- psql -h 127.0.0.1 chitter < seeds/chitter.sql