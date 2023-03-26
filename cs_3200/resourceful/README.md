# s23-resourceful-TekoXVI

## Games Collection

**Games**

Attributes:

* name (string)
* console (string)
* max players (integer)
* splitscreen (string)
* price (integer)

## Schema

```sql
CREATE TABLE games (
id INTEGER PRIMARY KEY,
name TEXT,
console TEXT,
max_players INTEGER,
splitscreen TEXT,
price INTEGER);
```

## REST Endpoints

Name                     | Method | Path
-------------------------|--------|------------------
Retrieve game collection | GET    | /games
Retrieve game member     | GET    | /games/*\<id\>*
Create game member       | POST   | /games
Update game member       | PUT    | /games/*\<id\>*
Delete game member       | DELETE | /games/*\<id\>*