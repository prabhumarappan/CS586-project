# Submission 3

## Subject Area - Dota

## ER Diagram

![Alt text](./images/Dota%20ER%20Diagram.png?height=800 "Title")

### Changes in ER during Implementation Phase:
1. For the DUser table, changed the type of id from INT to BIGINT
2. Added wins, losses and total games played to DUser table
3. Added picks, wins to the Hero table
4. For the HeroUser table, changed the type of id from INT to BIGINT
5. For the Match table, added radTeamId, direTeamId and radVictory columns
6. For the Match table, changed the type of id from INT to BIGINT
7. For the UserHero table, changed the type of id from INT to BIGINT
8. For the UserHero table, modified the columns to be victory, kills, deaths, assists

### Reason for the above changes:
1. Majorly because the data for events and tournaments were not readily available. Had to move them out of the schema. This lead to removing few of the tables. 
2. Apart from that, to complete the queries I seemed to miss a few columns, so for those I have added extra rows to the existing tables.

### Changes in Question during Implemenation Phase:
1. List down the tournaments happening now
2. List top 5 hero skills that are picked
3. Maximum number of roshan kills
4. Maximum number of buybacks
5. Removed the query to fetch each players top heor by win rate

### Reason for the above changes:
1. Tournmanets was removed from ER diagram, so no relation to query
2. Events were removed, so no relation to query
3. Same as 2
4. Same as 2
5. The query for this was becoming way too complicated to run

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

## Questions - and their respective queries
1. Name the player with maximum number of matches?
   ```SQL
   select username, email from duser where id in (select user_id from userhero group by user_id having count(*) = (select count(*) from userhero group by user_id order by count(*) desc limit 1));
   ```

   ![Alt text](./images/Query1.png?height=500 "Query")

2. Name the player who has played highest number of hours in game?
   ```SQL
   select user_id, duser.username, total_duration from (select u.user_id, sum(m.duration) as total_duration from userhero u, match m where u.match_id = m.id group by user_id order by total_duration desc limit 1) as f, duser where f.user_id = duser.id;
   ```

   ![Alt text](./images/Query2.png?height=500 "Query")

3. Name the player with maximum number of kills in total
   ```SQL
   select username, email from duser where id in (select user_id from userhero group by user_id having sum(kills)=(select sum(kills) total_kills from userhero group by user_id order by total_kills desc limit 1)); 
   ```

   ![Alt text](./images/Query3.png?height=500 "Query")

4. Name the player with maximum number of deaths in total
   ```SQL
   select username, email from duser where id in (select user_id from userhero group by user_id having sum(deaths)=(select sum(deaths) total_deaths from userhero group by user_id order by total_deaths desc limit 1));
   ```

   ![Alt text](./images/Query4.png?height=500 "Query")

5. Name the player with the lowest number of assists in total
   ```SQL
   select username, email from duser where id in (select user_id from userhero group by user_id having sum(assists)=(select sum(assists) total_assists from userhero group by user_id order by total_assists asc limit 1));  
   ```

   ![Alt text](./images/Query5.png?height=500 "Query")

6. List the 5 heroes which are picked the most. Order them by their picking rate.
   ```SQL
   select f.hero_id, hero.name, f.total_picks from hero, (select hero_id, count(*) total_picks from userhero group by hero_id order by total_picks desc limit 5) as f where hero.id = f.hero_id order by f.total_picks desc;
   ```

   ![Alt text](./images/Query6.png?height=500 "Query")

7. List the last 5 picked heroes. Order them by their picking rate.
   ```SQL
   select f.hero_id, hero.name, f.total_picks from hero, (select hero_id, count(*) total_picks from userhero group by hero_id order by total_picks asc limit 5) as f where hero.id = f.hero_id order by f.total_picks asc;
   ```

   ![Alt text](./images/Query7.png?height=500 "Query")

8. List the hero who is picked the most?
   ```SQL
   select id, name from hero where id = (select hero_id from userhero group by hero_id having count(*) = (select count(*) total_picks from userhero group by hero_id order by total_picks desc limit 1));
   ```

   ![Alt text](./images/Query8.png?height=500 "Query")

9.  For every player, list down their top picked heroes 
   ```SQL
   select b.user_id, duser.username, c.hero_id, hero.name, b.games from (select f.user_id, max(hero_count) as games from (select user_id, hero_id, count(*) as hero_count from userhero group by user_id, hero_id order by hero_count desc) as f group by f.user_id) as b, (select user_id, hero_id, games from (select f.user_id, f.hero_id, max(hero_count) as games from (select user_id, hero_id, count(*) as hero_count from userhero group by user_id, hero_id order by hero_count desc) as f group by f.user_id, hero_id) as f) as c, duser, hero where duser.id =b.user_id and c.hero_id = hero.id and b.user_id = c.user_id and b.games = c.games order by b.games desc;
   ```

   ![Alt text](./images/Query9.png?height=500 "Query")
   
10. List the longest running match
   ```SQL
   select * from match where duration = ( select duration from match order by duration desc limit 1);
   ```

   ![Alt text](./images/Query10.png?height=500 "Query")

11. For each player, list their longest running match
   ```SQL
   select a.user_id, duser.username, a.longest_match from (select user_id, max(m.duration) longest_match from userhero, match m, duser  where m.id = match_id group by user_id) as a, duser where a.user_id = duser.id order by a.longest_match desc;
   ```

   ![Alt text](./images/Query11.png?height=500 "Query")

12. For each player, list one player they have played the most with
   ```SQL
   select a.first_user, duser.username, b.second_user, a.total_played from (select f.first_user, max(played_count) as total_played from (select u1.user_id first_user, u2.user_id second_user, count(*) as played_count from userhero u1, userhero u2 where u1.match_id = u2.match_id and u1.user_id != u2.user_id group by u1.user_id, u2.user_id) as f group by f.first_user) as a, (select f.first_user, f.second_user, max(played_count) as total_played from (select u1.user_id first_user, u2.user_id second_user, count(*) as played_count from userhero u1, userhero u2 where u1.match_id = u2.match_id and u1.user_id != u2.user_id group by u1.user_id, u2.user_id) as f group by f.first_user, second_user) as b, duser where duser.id = a.first_user and a.first_user = b.first_user and a.total_played = b.total_played order by a.total_played desc;
   ```

   ![Alt text](./images/Query12.png?height=500 "Query")

13. For player Ana (or any other player) list down their top 5 successful matches and their KD rate(won game and highest KD)
   ```SQL
   select a.user_id, duser.username, a.match_id, b.kills, b.deaths, COALESCE(b.kills / NULLIF(b.deaths,0), b.kills) kd_rate  from (select user_id, match_id from userhero where victory=True group by user_id, match_id) a, userhero b, duser where duser.id = a.user_id and duser.username='Ana' and a.user_id = b.user_id and a.match_id=b.match_id order by kd_rate desc limit 5;
   ```

   ![Alt text](./images/Query13.png?height=500 "Query")

14. For player Ana (or any other player) list down their top 5 unsuccessful matches and their KD rate
   ```SQL
   select a.user_id, duser.username, a.match_id, b.kills, b.deaths, COALESCE(b.kills / NULLIF(b.deaths,0), b.kills) kd_rate  from (select user_id, match_id from userhero where victory=False group by user_id, match_id) a, userhero b, duser where duser.id = a.user_id and duser.username='Ana' and a.user_id = b.user_id and a.match_id=b.match_id order by kd_rate asc limit 5;
   ```

   ![Alt text](./images/Query14.png?height=500 "Query")

15. List down all the players and the number of times they have played the hero "Anti Mage"
   ```SQL
   select d.username, count(*) from userhero u,hero h, duser d where u.hero_id = h.id and h.name= 'Anti-Mage' and d.id = u.user_id group by d.username;
   ```

   ![Alt text](./images/Query15.png?height=500 "Query")

16. List down all the players and the number of times they have played the heros "Troll Warlord" and "Bristeback"
   ```SQL
   select d.username, count(*) from userhero u,hero h, duser d where u.hero_id = h.id and (h.name= 'Troll Warlord' or h.name='Bristleback') and d.id = u.user_id group by d.username, d.id;
   ```

   ![Alt text](./images/Query16.png?height=500 "Query")

17. For each hero, list down their main type (agility, strength and intelligence)
   ```SQL
   select id, name, type from hero;
   ```

   ![Alt text](./images/Query17.png?height=500 "Query")

18. Name the user with the highest number of victories
   ```SQL
   select username, email from duser where id in (select user_id from userhero where victory = True group by user_id having count(*) = (select count(*) win_count from userhero where victory=True group by user_id order by win_count desc limit 1));
   ```

   ![Alt text](./images/Query18.png?height=500 "Query")

19. Name the user with the highest win rate
   ```SQL
   select d.username, win_count*100/(win_count+loss_count) as win_prct from duser d, (select user_id,count(*) as win_count from userhero where victory=True group by user_id) as a, (select user_id,count(*) as loss_count from userhero where victory=False group by user_id) as b where d.id = a.user_id and a.user_id = b.user_id order by win_prct desc limit 1;
   ```

   ![Alt text](./images/Query19.png?height=500 "Query")

20. Name the user with the lowest number of victories
   ```SQL
   select username, email from duser where id in (select user_id from userhero where victory = True group by user_id having count(*) = (select count(*) win_count from userhero where victory=True group by user_id order by win_count asc limit 1));
   ```

   ![Alt text](./images/Query20.png?height=500 "Query")