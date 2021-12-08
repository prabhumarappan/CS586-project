# Submission 3

# Subject Area - Dota

# Table of Contents
- [Submission 3](#submission-3)
- [Subject Area - Dota](#subject-area---dota)
- [Table of Contents](#table-of-contents)
- [ER Diagram](#er-diagram)
- [Changes in Implementation Phase](#changes-in-implementation-phase)
    - [Changes in ER during Implementation Phase:](#changes-in-er-during-implementation-phase)
    - [Reason for the above ER changes:](#reason-for-the-above-er-changes)
    - [Changes in Question during Implemenation Phase:](#changes-in-question-during-implemenation-phase)
    - [Reason for the above Question changes:](#reason-for-the-above-question-changes)
- [Schema and SQL Statements](#schema-and-sql-statements)
  - [DUser](#duser)
    - [Schema](#schema)
    - [Sample Data](#sample-data)
  - [Hero](#hero)
    - [Schema](#schema-1)
    - [Sample Data](#sample-data-1)
  - [Skill](#skill)
    - [Sample Data](#sample-data-2)
  - [HeroSkill](#heroskill)
    - [Sample Data](#sample-data-3)
  - [Team](#team)
    - [Sample Data](#sample-data-4)
  - [TeamUser](#teamuser)
    - [Sample Data](#sample-data-5)
  - [Match](#match)
    - [Sample Data](#sample-data-6)
  - [UserHero](#userhero)
    - [Sample Data](#sample-data-7)
- [How we populated the database?](#how-we-populated-the-database)
- [Questions - and their respective queries](#questions---and-their-respective-queries)

# ER Diagram

![Alt text](./images/Dota%20ER%20Diagram.png?height=800 "Title")

# Changes in Implementation Phase

### Changes in ER during Implementation Phase:
1. For the DUser table, changed the type of id from INT to BIGINT
2. Added wins, losses and total games played to DUser table
3. Added picks, wins to the Hero table
4. For the HeroUser table, changed the type of id from INT to BIGINT
5. For the Match table, added radTeamId, direTeamId and radVictory columns
6. For the Match table, changed the type of id from INT to BIGINT
7. For the UserHero table, changed the type of id from INT to BIGINT
8. For the UserHero table, modified the columns to be victory, kills, deaths, assists

### Reason for the above ER changes:
1. Majorly because the data for events and tournaments were not readily available. Had to move them out of the schema. This lead to removing few of the tables. 
2. Apart from that, to complete the queries I seemed to miss a few columns, so for those I have added extra rows to the existing tables.

### Changes in Question during Implemenation Phase:
1. List down the tournaments happening now
2. List top 5 hero skills that are picked
3. Maximum number of roshan kills
4. Maximum number of buybacks
5. Removed the query to fetch each players top heor by win rate

### Reason for the above Question changes:
1. Tournmanets was removed from ER diagram, so no relation to query
2. Events were removed, so no relation to query
3. Same as 2
4. Same as 2
5. The query for this was becoming way too complicated to run

# Schema and SQL Statements

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

# How we populated the database?
We first downloaded and created data from multiple APIs. And then loaded the data into db using `/copy` command.
I have also included all the scripts in the `scripts` folder which was used to get the data.

# Questions - and their respective queries
1. Name the player with maximum number of matches?
   ```SQL
   SELECT username,
       email
   FROM duser
   WHERE id in
      (SELECT user_id
      FROM userhero
      GROUP BY user_id
      HAVING count(*) =
         (SELECT count(*)
         FROM userhero
         GROUP BY user_id
         ORDER BY count(*) DESC
         LIMIT 1));
   ```

   ![Alt text](./images/Query1.png?height=500 "Query")

2. Name the player who has played highest number of hours in game?
   ```SQL
   SELECT user_id, 
       duser.username, 
       total_duration 
   FROM   (SELECT u.user_id, 
                  Sum(m.duration) AS total_duration 
         FROM   userhero u, 
                  MATCH m 
         WHERE  u.match_id = m.id 
         GROUP  BY user_id 
         ORDER  BY total_duration DESC 
         LIMIT  1) AS f, 
         duser 
   WHERE  f.user_id = duser.id; 
   ```

   ![Alt text](./images/Query2.png?height=500 "Query")

3. Name the player with maximum number of kills in total
   ```SQL
   SELECT username, 
       email 
   FROM   duser 
   WHERE  id IN (SELECT user_id 
               FROM   userhero 
               GROUP  BY user_id 
               HAVING Sum(kills) = (SELECT Sum(kills) total_kills 
                                    FROM   userhero 
                                    GROUP  BY user_id 
                                    ORDER  BY total_kills DESC 
                                    LIMIT  1)); 
   ```

   ![Alt text](./images/Query3.png?height=500 "Query")

4. Name the player with maximum number of deaths in total
   ```SQL
   SELECT username, 
         email 
   FROM   duser 
   WHERE  id IN (SELECT user_id 
               FROM   userhero 
               GROUP  BY user_id 
               HAVING Sum(deaths) = (SELECT Sum(deaths) total_deaths 
                                       FROM   userhero 
                                       GROUP  BY user_id 
                                       ORDER  BY total_deaths DESC 
                                       LIMIT  1)); 
   ```

   ![Alt text](./images/Query4.png?height=500 "Query")

5. Name the player with the lowest number of assists in total
   ```SQL
   SELECT username, 
       email 
   FROM   duser 
   WHERE  id IN (SELECT user_id 
               FROM   userhero 
               GROUP  BY user_id 
               HAVING Sum(assists) = (SELECT Sum(assists) total_assists 
                                       FROM   userhero 
                                       GROUP  BY user_id 
                                       ORDER  BY total_assists ASC 
                                       LIMIT  1)); 
   ```

   ![Alt text](./images/Query5.png?height=500 "Query")

6. List the 5 heroes which are picked the most. Order them by their picking rate.
   ```SQL
   SELECT f.hero_id, 
       hero.name, 
       f.total_picks 
   FROM   hero, 
         (SELECT hero_id, 
                  Count(*) total_picks 
         FROM   userhero 
         GROUP  BY hero_id 
         ORDER  BY total_picks DESC 
         LIMIT  5) AS f 
   WHERE  hero.id = f.hero_id 
   ORDER  BY f.total_picks DESC; 
   ```

   ![Alt text](./images/Query6.png?height=500 "Query")

7. List the last 5 picked heroes. Order them by their picking rate.
   ```SQL
   SELECT f.hero_id, 
       hero.name, 
       f.total_picks 
   FROM   hero, 
         (SELECT hero_id, 
                  Count(*) total_picks 
         FROM   userhero 
         GROUP  BY hero_id 
         ORDER  BY total_picks ASC 
         LIMIT  5) AS f 
   WHERE  hero.id = f.hero_id 
   ORDER  BY f.total_picks ASC; 
   ```

   ![Alt text](./images/Query7.png?height=500 "Query")

8. List the hero who is picked the most?
   ```SQL
   SELECT id, 
         name 
   FROM   hero 
   WHERE  id = (SELECT hero_id 
               FROM   userhero 
               GROUP  BY hero_id 
               HAVING Count(*) = (SELECT Count(*) total_picks 
                                 FROM   userhero 
                                 GROUP  BY hero_id 
                                 ORDER  BY total_picks DESC 
                                 LIMIT  1)); 
   ```

   ![Alt text](./images/Query8.png?height=500 "Query")

9.  For every player, list down their top picked heroes 
   ```SQL
   SELECT b.user_id, 
       duser.username, 
       c.hero_id, 
       hero.name, 
       b.games 
   FROM   (SELECT f.user_id, 
                  Max(hero_count) AS games 
         FROM   (SELECT user_id, 
                        hero_id, 
                        Count(*) AS hero_count 
                  FROM   userhero 
                  GROUP  BY user_id, 
                           hero_id 
                  ORDER  BY hero_count DESC) AS f 
         GROUP  BY f.user_id) AS b, 
         (SELECT user_id, 
                  hero_id, 
                  games 
         FROM   (SELECT f.user_id, 
                        f.hero_id, 
                        Max(hero_count) AS games 
                  FROM   (SELECT user_id, 
                                 hero_id, 
                                 Count(*) AS hero_count 
                           FROM   userhero 
                           GROUP  BY user_id, 
                                    hero_id 
                           ORDER  BY hero_count DESC) AS f 
                  GROUP  BY f.user_id, 
                           hero_id) AS f) AS c, 
         duser, 
         hero 
   WHERE  duser.id = b.user_id 
         AND c.hero_id = hero.id 
         AND b.user_id = c.user_id 
         AND b.games = c.games 
   ORDER  BY b.games DESC; 
   ```

   ![Alt text](./images/Query9.png?height=500 "Query")
   
10. List the longest running match
   ```SQL
   SELECT * 
   FROM   MATCH 
   WHERE  duration = (SELECT duration 
                     FROM   MATCH 
                     ORDER  BY duration DESC 
                     LIMIT  1); 
   ```

   ![Alt text](./images/Query10.png?height=500 "Query")

11. For each player, list their longest running match
   ```SQL
   SELECT a.user_id, 
       duser.username, 
       a.longest_match 
   FROM   (SELECT user_id, 
                  Max(m.duration) longest_match 
         FROM   userhero, 
                  MATCH m, 
                  duser 
         WHERE  m.id = match_id 
         GROUP  BY user_id) AS a, 
         duser 
   WHERE  a.user_id = duser.id 
   ORDER  BY a.longest_match DESC; 
   ```

   ![Alt text](./images/Query11.png?height=500 "Query")

12. For each player, list one player they have played the most with
   ```SQL
   SELECT a.first_user, 
       duser.username, 
       b.second_user, 
       a.total_played 
   FROM   (SELECT f.first_user, 
                  Max(played_count) AS total_played 
         FROM   (SELECT u1.user_id first_user, 
                        u2.user_id second_user, 
                        Count(*)   AS played_count 
                  FROM   userhero u1, 
                        userhero u2 
                  WHERE  u1.match_id = u2.match_id 
                        AND u1.user_id != u2.user_id 
                  GROUP  BY u1.user_id, 
                           u2.user_id) AS f 
         GROUP  BY f.first_user) AS a, 
         (SELECT f.first_user, 
                  f.second_user, 
                  Max(played_count) AS total_played 
         FROM   (SELECT u1.user_id first_user, 
                        u2.user_id second_user, 
                        Count(*)   AS played_count 
                  FROM   userhero u1, 
                        userhero u2 
                  WHERE  u1.match_id = u2.match_id 
                        AND u1.user_id != u2.user_id 
                  GROUP  BY u1.user_id, 
                           u2.user_id) AS f 
         GROUP  BY f.first_user, 
                     second_user) AS b, 
         duser 
   WHERE  duser.id = a.first_user 
         AND a.first_user = b.first_user 
         AND a.total_played = b.total_played 
   ORDER  BY a.total_played DESC; 
   ```

   ![Alt text](./images/Query12.png?height=500 "Query")

13. For player Ana (or any other player) list down their top 5 successful matches and their KD rate(won game and highest KD)
   ```SQL
   SELECT a.user_id, 
       duser.username, 
       a.match_id, 
       b.kills, 
       b.deaths, 
       Coalesce(b.kills / Nullif(b.deaths, 0), b.kills) kd_rate 
   FROM   (SELECT user_id, 
                  match_id 
         FROM   userhero 
         WHERE  victory = true 
         GROUP  BY user_id, 
                     match_id) a, 
         userhero b, 
         duser 
   WHERE  duser.id = a.user_id 
         AND duser.username = 'Ana' 
         AND a.user_id = b.user_id 
         AND a.match_id = b.match_id 
   ORDER  BY kd_rate DESC 
   LIMIT  5; 
   ```

   ![Alt text](./images/Query13.png?height=500 "Query")

14. For player Ana (or any other player) list down their top 5 unsuccessful matches and their KD rate
   ```SQL
   SELECT a.user_id, 
       duser.username, 
       a.match_id, 
       b.kills, 
       b.deaths, 
       Coalesce(b.kills / Nullif(b.deaths, 0), b.kills) kd_rate 
   FROM   (SELECT user_id, 
                  match_id 
         FROM   userhero 
         WHERE  victory = false 
         GROUP  BY user_id, 
                     match_id) a, 
         userhero b, 
         duser 
   WHERE  duser.id = a.user_id 
         AND duser.username = 'Ana' 
         AND a.user_id = b.user_id 
         AND a.match_id = b.match_id 
   ORDER  BY kd_rate ASC 
   LIMIT  5; 
   ```

   ![Alt text](./images/Query14.png?height=500 "Query")

15. List down all the players and the number of times they have played the hero "Anti Mage"
   ```SQL
   SELECT d.username, 
       Count(*) 
   FROM   userhero u, 
         hero h, 
         duser d 
   WHERE  u.hero_id = h.id 
         AND h.name = 'Anti-Mage' 
         AND d.id = u.user_id 
   GROUP  BY d.username; 
   ```

   ![Alt text](./images/Query15.png?height=500 "Query")

16. List down all the players and the number of times they have played the heros "Troll Warlord" and "Bristeback"
   ```SQL
   SELECT d.username, 
       Count(*) 
   FROM   userhero u, 
         hero h, 
         duser d 
   WHERE  u.hero_id = h.id 
         AND ( h.name = 'Troll Warlord' 
               OR h.name = 'Bristleback' ) 
         AND d.id = u.user_id 
   GROUP  BY d.username, 
            d.id; 
   ```

   ![Alt text](./images/Query16.png?height=500 "Query")

17. For each hero, list down their main type (agility, strength and intelligence)
   ```SQL
   SELECT id, 
       name, 
       type 
   FROM   hero; 
   ```

   ![Alt text](./images/Query17.png?height=500 "Query")

18. Name the user with the highest number of victories
   ```SQL
   SELECT username, 
       email 
   FROM   duser 
   WHERE  id IN (SELECT user_id 
               FROM   userhero 
               WHERE  victory = true 
               GROUP  BY user_id 
               HAVING Count(*) = (SELECT Count(*) win_count 
                                    FROM   userhero 
                                    WHERE  victory = true 
                                    GROUP  BY user_id 
                                    ORDER  BY win_count DESC 
                                    LIMIT  1)); 
   ```

   ![Alt text](./images/Query18.png?height=500 "Query")

19. Name the user with the highest win rate
   ```SQL
   SELECT d.username, 
       win_count * 100 / ( win_count + loss_count ) AS win_prct 
   FROM   duser d, 
         (SELECT user_id, 
                  Count(*) AS win_count 
         FROM   userhero 
         WHERE  victory = true 
         GROUP  BY user_id) AS a, 
         (SELECT user_id, 
                  Count(*) AS loss_count 
         FROM   userhero 
         WHERE  victory = false 
         GROUP  BY user_id) AS b 
   WHERE  d.id = a.user_id 
         AND a.user_id = b.user_id 
   ORDER  BY win_prct DESC 
   LIMIT  1; 
   ```

   ![Alt text](./images/Query19.png?height=500 "Query")

20. Name the user with the lowest number of victories
   ```SQL
   SELECT username, 
       email 
   FROM   duser 
   WHERE  id IN (SELECT user_id 
               FROM   userhero 
               WHERE  victory = true 
               GROUP  BY user_id 
               HAVING Count(*) = (SELECT Count(*) win_count 
                                    FROM   userhero 
                                    WHERE  victory = true 
                                    GROUP  BY user_id 
                                    ORDER  BY win_count ASC 
                                    LIMIT  1)); 
   ```

   ![Alt text](./images/Query20.png?height=500 "Query")