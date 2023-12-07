[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ECKgeadS)
# COMP-1510-202330-Term-Project

# Survive CST
by: Alice Huang (A01372753), Yang Guo (A00968177)


#### GitHub usernames:
Alice: orangeepop  
Yang: YangGuo57 

## About this game:
Survive CST is a SUD simulation game where the player is a new student entering first year, first term of the CST 
program. The player needs to balance schoolwork, social life, work life, and sleep in order to succeed in this program. 

## Required elements
| Element                  | Package/module name                           | Line              |
|--------------------------|-----------------------------------------------|-------------------|
| immutable data structure | game_system                                   | 2, 3              |
| mutable data structure   | game_system.character.py                      | 23-30             |
| exceptions               | game_system.save.py                           | 60-66             |
| dictionary comprehension | game_system.map.py                            | 29-30             |
| if statements            | game_system.save.py                           | 18,22,28          |
| while loop               | game_system.weekend.py                        | 134               |
| in operator              | game_system.weekend.py                        | 174               |
| range function           | game_system.weekend.py<br/>game_system.map.py | 439-445<br/>29-30 |
| itertools                | game_system.character.py                      | 183               |
| random module            | game_system.weekend.py                        | 211               |
| function annotations     | game_system.weekend.py                        | 60                |
| 10x10 map                | game.py                                       | 41-42             |
|character| game_system.character.py                      | 6-42              |
|movement in 4 directions| game_system.move.py                           | 92-99             |
|movement restriction| game_system.move.py                           | 4-38              |
|gameplay ending| game.py | 52-53, 58-59, 79  |
|challenges| game_system.exam.py| 128-134           |




## functions that we did not doctest/unit test:
weekday.weekday  
weekday.end_of_week_action  
weekday.random_weekday_event   
event_trigger.move_during_office_hours  
event_trigger.move_on_weekends  
weekend.weekend  
weekend.function_dispatcher