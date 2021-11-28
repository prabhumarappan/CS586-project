# Submission 2

## Subject Area - Dota

## ER Diagram

![Alt text](./Dota%20ER%20Diagram.png?height=800 "Title")

## Main Entities
1. User
   1. Id
   2. Username
   3. Email
   4. Created At
2. Hero
   1. Id
   2. Name
   3. AttackType -> Melee/Ranged
   4. Armor
   5. Complexity
   6. Type -> Strength/Intelligence/Agility (enum)
   7. HP
   8. Mana
3. Skill
   1. Id
   2. Name -> Mana Break/Blink/Counter Spell etc
   3. Description
4. Team
   1. id
   2. match_id
   3. date
   4. player_id
5. Match
   1. Id
   2. Start
   3. End
   4. Winner -> Radiant/Dire
   5. Score
6. Event
   1. Id
   2. Type -> Kill/BuyBack/Roshan (enum)
   3. Description
7. Tournament
   1. Id
   2. Name
   3. Teams
   4. Winner
   5. Time


## Tables
1. User
   1. id (PK)
   2. username
   3. email
   4. created_at
2. Hero
   1. id (PK)
   2. name
   3. attack_type -> Melee/Ranged
   4. armor
   5. complexity
   6. type -> Strength/Intelligence/Agility (enum)
   7. hP
   8. mana
3. Skill
   1. id (PK)
   2. name -> Mana Break/Blink/Counter Spell etc
   3. description
4. HeroSkill
   1. hero_id
   2. skill_id
5. Team
   1. id (PK)
   2. match_id (FK)
   3. date
   4. user_id (FK)
   5. type -> radiant/dire
   6. score
6. TeamUser
   1. team_id (FK)
   2. user_id (FK)
7. Match
   1. id (PK)
   2. start
   3. duration
   4. winner -> (FK)
8.  MatchTeam
   5. team_id (FK)
   6. match_id (FK)
9. UserHero
   1. user_id (FK)
   2. hero_id (FK)
   3. match_id (FK)
   4. result -> win/loss
10. Event 
   1. id (PK)
   2. type -> (kill, buyback, roshan) 
   3. description
11. MatchEvent
   1.  match_id (FK)
   2.  event_id (FK)
   3.  time
12. Tournament
   1.  id (PK)
   2.  name
   3.  start_date
   4.  prize_pool
   5.  winner (FK)
13. TournamentMatch
   1.  tournament_id (FK)
   2.  match_id (FK)
   3.  date
   4.  winner -> (FK)


SQL Statements
==============
`CREATE TABLE DUser (
   id int PRIMARY KEY, 
   username varchar(255) UNIQUE,
   email varchar(320) UNIQUE,
   created_at timestamp NOT NULL
);`

`CREATE TABLE Hero (
   id int PRIMARY KEY,
   name varchar(200) NOT NULL,
   attack_type varchar(6) NOT NULL,
   armor decimal NOT NULL,
   complexity int NOT NULL,
   type varchar(12) NOT NULL,
   hP decimal NOT NULL,
   mana decimal NOT NULL
);`

`CREATE TABLE Skill (
   id int PRIMARY KEY,
   name varchar(200) NOT NULL,
   description text NOT NULL
);`

`CREATE TABLE HeroSkill (
   hero_id int NOT NULL,
   skill_id int NOT NULL,
   CONSTRAINT fk_hero FOREIGN KEY (hero_id) REFERENCES Hero (id),
   CONSTRAINT fk_skill FOREIGN KEY (skill_id) REFERENCES Skill (id)
);`

`CREATE TABLE Team (
   id int PRIMARY KEY,
   date timestamp NOT NULL,
   user_id int NOT NULL,
   type varchar(7) NOT NULL,
   score int NULL,
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES DUser (id)
);`

`CREATE TABLE TeamUser (
   team_id int NOT NULL,
   user_id int NOT NULL,
   CONSTRAINT fk_team FOREIGN KEY (team_id) REFERENCES Team (id),
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES DUser (id)
);`

`CREATE TABLE Match (
   id int PRIMARY KEY,
   start timestamp NOT NULL,
   duration int NOT NULL,
   winner int,
   CONSTRAINT fk_winner FOREIGN KEY (winner) REFERENCES Team(id)
);`

`CREATE TABLE MatchTeam (
   match_id int NOT NULL,
   team_id int NOT NULL,
   CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Match (id),
   CONSTRAINT fk_team FOREIGN KEY (team_id) REFERENCES Team (id)
);`

`CREATE TABLE UserHero(
   user_id int NOT NULL,
   hero_id int NOT NULL,
   match_id int NOT NULL,
   result VARCHAR(4) NULL,
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES DUser(id),
   CONSTRAINT fk_hero FOREIGN KEY (hero_id) REFERENCES Hero(id),
   CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Match(id)
);`

`CREATE TABLE Event(
   id int PRIMARY KEY,
   type varchar(10) NOT NULL,
   description text
);`

`CREATE TABLE MatchEvent(
   match_id int NOT NULL,
   event_id int NOT NULL,
   time timestamp,
   CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Match(id),
   CONSTRAINT fk_event FOREIGN KEY (event_id) REFERENCES Event(id)
);`

`CREATE TABLE Tournament(
   id int PRIMARY KEY,
   name varchar(255),
   start_date timestamp NOT NULL,
   prize_pool int NOT NULL,
   winner int NULL,
   CONSTRAINT fk_winner FOREIGN KEY (winner) REFERENCES Team(id)
);`

`CREATE TABLE TournamentMatch(
   tournament_id int NOT NULL,
   match_id int NOT NULL,
   date timestamp NOT NULL,
   CONSTRAINT fk_tournament FOREIGN KEY (tournament_id) REFERENCES Tournament(id),
   CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Match(id)
);`