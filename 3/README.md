# Submission 3

## Subject Area - Dota

## ER Diagram

![Alt text](./images/Dota%20ER%20Diagram.png?height=800 "Title")

Changes during Implementation Phase:
1. For the DUser table, changed the type of id from INT to BIGINT
2. Added wins, losses and total games played to DUser table
3. Added picks, wins to the Hero table
4. For the HeroUser table, changed the type of id from INT to BIGINT
5. For the Match table, added radTeamId, direTeamId and radVictory columns
6. For the Match table, changed the type of id from INT to BIGINT
7. For the UserHero table, changed the type of id from INT to BIGINT
8. For the UserHero table, modified the columns to be victory, kills, deaths, assists


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
### Sample Data
![Alt text](./images/Skill%20Sample%20Data.png?height=500 "Title")

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
### Sample Data
![Alt text](./images/Hero%20Skill%20Sample%20Data.png?height=500 "Title")

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
### Sample Data
![Alt text](./images/Team%20Sample%20Data.png?height=500 "Title")

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
### Sample Data
![Alt text](./images/Team%20User%20Sample%20Data.png?height=500 "Title")

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
### Sample Data
![Alt text](./images/Match%20Sample%20Data.png?height=500 "Title")

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

### Sample Data
![Alt text](./images/User%20Hero%20Sample%20Data.png?height=500 "Title")

## How we populated the database?
We first downloaded and created data from multiple APIs. And then loaded the data into db using `/copy` command.
I have also included all the scripts in the `scripts` folder which was used to get the data.

