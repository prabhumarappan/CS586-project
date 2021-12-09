# Submission 2

## Subject Area - Dota

## Old ER Diagram

![Alt text](./images/Dota%20ER%20Diagram%20(Old).png?height=800 "Title")

## New ER Diagram

![Alt text](./images/Dota%20ER%20Diagram.png?height=800 "Title")

## Main Entities
1. User
   1. id (PK)
   2. username
   3. email
   4. created_at
   5. wins 
   6. losses 
   7. total
2. Hero
   1. id (PK)
   2. name
   3. attack_type -> Melee/Ranged
   4. armor
   5. complexity
   6. type -> Strength/Intelligence/Agility (enum)
   7. hp
   8. mana
   9. picks
   10. wins
3. Skill
   1. Id
   2. Name -> Mana Break/Blink/Counter Spell etc
   3. Description
4. Team
   1. id
   2. name
   3. date
5. Match
   1. id (PK)
   2. start
   3. duration
   4. radTeamId (FK)
   5. direTeamId (FK)
   6. radVictory

## Tables

1. DUser
2. Hero
3. Skill
4. HeroSkill
5. Team
6. TeamUser
7. Match
8. UserHero

Schema and SQL Statements
==============
## DUser

   1. id (PK)
   2. username
   3. email
   4. created_at
   5. wins 
   6. losses 
   7. total
   
```SQL
CREATE TABLE DUser (
   id BIGINT PRIMARY KEY, 
   username varchar(255) UNIQUE,
   wins int DEFAULT 0,
   losses int DEFAULT 0,
   total int DEFAULT 0,
   email varchar(320) UNIQUE,
   created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Schema
![Alt text](./images/DUser%20Schema.png?height=500 "Title")

### Sample Data

![Alt text](./images/DUser%20Sample%20Data.png?height=500 "Title")

## Hero

   1. id (PK)
   2. name
   3. attack_type -> Melee/Ranged
   4. armor
   5. complexity
   6. type -> Strength/Intelligence/Agility (enum)
   7. hp
   8. mana
   9. picks
   10. wins

```SQL
CREATE TABLE Hero (
   id int PRIMARY KEY,
   name varchar(200) NOT NULL,
   attack_type varchar(6) NOT NULL,
   armor decimal NOT NULL,
   complexity int NOT NULL,   
   type varchar(12) NOT NULL,
   hp decimal NOT NULL,
   mana decimal NOT NULL,
   picks int DEFAULT 0,
   wins int DEFAULT 0
);
```

### Schema
![Alt text](./images/Hero%20Schema.png?height=500 "Title")

### Sample Data
![Alt text](./images/Hero%20Sample%20Data.png?height=500 "Title")


## Skill

   1. id (PK)
   1. name -> Mana Break/Blink/Counter Spell etc
   2. description
   
```SQL
CREATE TABLE Skill (
   id int PRIMARY KEY,
   name varchar(200) NOT NULL,
   description text NOT NULL
);
```
## HeroSkill

   1. hero_id
   2. skill_id

```SQL
CREATE TABLE HeroSkill (
   hero_id int NOT NULL,
   skill_id int NOT NULL,
   CONSTRAINT fk_hero FOREIGN KEY (hero_id) REFERENCES Hero (id),
   CONSTRAINT fk_skill FOREIGN KEY (skill_id) REFERENCES Skill (id)
);
```
## Team

   1. id (PK)
   2. date
   3. name
   
```SQL
CREATE TABLE DTeam (
   id int PRIMARY KEY,
   name varchar(200) NOT NULL,
   date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
## TeamUser

   1. team_id (FK)
   2. user_id (FK)
   3. date_joined

```SQL
CREATE TABLE TeamUser (
   team_id int NOT NULL,
   user_id BIGINT NOT NULL,
   date_joined timestamp DEFAULT CURRENT_TIMESTAMP,
   CONSTRAINT fk_team FOREIGN KEY (team_id) REFERENCES DTeam (id),
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES DUser (id)
);
```
## Match

   1. id (PK)
   2. start
   3. duration
   4. radTeamId (FK)
   5. direTeamId (FK)
   6. radVictory

```SQL
CREATE TABLE Match (
   id BIGINT PRIMARY KEY,
   start timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
   duration int NOT NULL,
   radTeamId int,
   direTeamId int,
   radVictory boolean,
   CONSTRAINT fk_radteamid FOREIGN KEY (radTeamId) REFERENCES DTeam(id),
   CONSTRAINT fk_direteamid FOREIGN KEY (direTeamId) REFERENCES DTeam(id)
);
```
## UserHero

   1. user_id (FK)
   2. hero_id (FK)
   3. match_id (FK)
   4. victory
   5. kills
   6. deaths
   7. assists

```SQL
CREATE TABLE UserHero(
   user_id BIGINT NOT NULL,
   hero_id int NOT NULL,
   match_id BIGINT NOT NULL,
   victory boolean DEFAULT FALSE,
   kills int DEFAULT 0,
   deaths int DEFAULT 0,
   assists int DEFAULT 0,
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES DUser(id),
   CONSTRAINT fk_hero FOREIGN KEY (hero_id) REFERENCES Hero(id),
   CONSTRAINT fk_match FOREIGN KEY (match_id) REFERENCES Match(id)
);
```