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

-- Table peeps [content, date, time]
-- Table users [email, username, name, password, user_id]
-- peeps_users [user_id, peep_id] -- connecting table

-- Decide on the tables relationship
-- 1. Can one user have many POSTS? <- foregin key

-- Table 
CREATE TABLE <table_name> (
  id SERIAL PRIMARY KEY,
  <column> text,
  <column> int
);

-- Table 2
CREATE TABLE <table_name> (
  id SERIAL PRIMARY KEY,
  <column> text,
  <column> int
);
INSERT INTO <table_name> (<columns>) VALUES (<values>);


-- Table 3 (connecting table)
CREATE TABLE posts_tags (
  post_id int,
  tag_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (post_id, tag_id)
);

-- Write file into database in terminal
-- psql -h 127.0.0.1 database_name < table_name.sql