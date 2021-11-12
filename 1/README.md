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
3. Name the player with maximum number of kills in a match?
4. List the 5 heroes which are picked the most. Order them by their picking rate.
5. List the last 5 picked heroes. Order them by their picking rate.
6. List the hero with the highest 
7. For every player, list down their top hero by their winning percentage
8. For every player, list down their top picked heroes
9. List the longest running match
10. For each player, list one player they have played the most with
11. List all the tournaments happening now
12. List top 5 hero skills that are picked
13. Which player got killed in a match the most?
14. Find the match with the maximum number of roshan kills
15. Find the match with the maximum number of buybacks
16. For player Ana (or any other player) list down their top 5 successful matches and their KD rate(won game and highest KDA)
17. For player Notail (or any other player) list down their top 5 unsuccessful matches and their KD rate
18. List down all the players and the number of times they have played the hero "Anti Mage"
19. List down all the players and the number of times they have played the heros "Troll Warlord" and "Bristeback"
20. For each hero, list down their characteristics (agility, strength and intelligence) in one row.


## Data Source
1. https://www.opendota.com/
2. https://www.kaggle.com/devinanzelmo/dota-2-matches

### What is the plan to ingest data into DB?
I plan to convert the data form different sources into a csv and then plan to load them into the database using the `copy` command.