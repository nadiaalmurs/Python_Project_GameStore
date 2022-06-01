# Python_Project_GameStore

### What you can do
- See all games inventory and developers
- See a single game/ developer
- Create new game and developer
- Edit games and developers
- Filter by genre or developer
- Visually see stock levels by colour code (red: stock is low order more now, yellow: stock is almost low, thinking about ordering more, green: stock is high, black: out of stock)
- Visually see stock levels by number for accessibility (colour blindness, etc)
- Mark up is displayed on inventory
- Delevelopers can be active or deactive, deactived developers can not be choosen while creating a new game. 

### How to run
In terminal, at the highest root file, write the following:
- sqlite3 db/game_manager.db < db/game_manager.sql
- python3 console
- flask run

Then go to your local host in your main web browser and ta da... (http://localhost:5000/)
