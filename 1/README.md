# Submission 1

## Subject Area - Dota

## General Description
Dota[https://www.dota2.com/home] know as Defence of The Ancient is a online multiplayer game. There are two teams of 5 players each, Dire and Radiant. Every player chooses their own hero (who have a combination of skill in agility, strength and intelligence).

The game can go more comprehensive than what I have decided to implement. The game can have coaches, players can build items, upgrade items, leveling up heros and also can give other players items. But for the purpose of this project, this is just restricted to

1. Matches a player has played
2. Kills made in a match
3. Roshans killed in a match
4. Hero Skills
5. Players in a team during a match

### Abbrevations
1. KDA - Kill Death Assist
2. KD - Kill Death

## Questions
1. Name the player with maximum number of matches?
2. Name the player who has played highest number of hours in game?
3. Name the player with maximum number of kills in total
4. Name the player with maximum number of deaths in total
5. Name the player with the lowest number of assists in total
6. List the 5 heroes which are picked the most. Order them by their picking rate.
7. List the last 5 picked heroes. Order them by their picking rate.
8. List the hero who is picked the most?
9.  For every player, list down their top picked heroes
10. List the longest running match
11. For each player, list their longest running match
12. For each player, list one player they have played the most with
13. For player Ana (or any other player) list down their top 5 successful matches and their KD rate(won game and highest KD)
14. For player Ana (or any other player) list down their top 5 unsuccessful matches and their KD rate
15. List down all the players and the number of times they have played the hero "Anti Mage"
16. List down all the players and the number of times they have played the heros "Troll Warlord" and "Bristeback"
17. For each hero, list down their main type (agility, strength and intelligence)
18. Name the user with the highest number of victories
19. Name the user with the highest win rate
20. Name the user with the lowest number of victories


## Data Source
1. https://www.opendota.com/
2. https://www.opendota.com/api-keys
3. https://www.opendota.com/heroes
4. https://www.opendota.com/teams
5. https://www.kaggle.com/devinanzelmo/dota-2-matches

### What is the plan to ingest data into DB?
I plan to convert the data form different sources into a csv and then plan to load them into the database using the `copy` command.
The data will be combed from the above opendota API and then aggregated into multiple CSVs.