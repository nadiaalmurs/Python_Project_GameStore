import pdb
from models.game import Game
from models.developer import Developer

import repositories.game_repository as game_repository
import repositories.developer_repository as developer_repository

developer_repository.delete_all()
game_repository.delete_all()

developer1 = Developer("CapCom", 5, 3)
developer_repository.save(developer1)

developer2 = Developer("Rockstar Games", 10, 2)
developer_repository.save(developer2)

developer3 = Developer("Frogwares", 8, 5)
developer_repository.save(developer3)

game1 = Game("Resident Evil Village", "Horror", "Ethan Winters searches for his kidnapped daughter in a village filled with mutant creatures.", 25, 30, 50, developer1)
game_repository.save(game1)

game2 = Game("Grand Theft Auto 5", "Adventure", "The story is centred on the heist sequences, and many missions involve shooting and driving gameplay.", 10, 10, 20, developer2)
game_repository.save(game2)

game3 = Game("Red Dead Redemption 2", "Adventure", "After a failed bank robbery in 1899 in the western town of Blackwater, Arthur Morgan and his gang are forced to go on the run.", 4, 50, 70, developer2)
game_repository.save(game3)


game4 = Game("Sherlock Holmes: The Devil's Daughter", "Detective", "Holmes and Watson are unexpectedly thrust into a new case when they witness a massive traffic accident in central London. The case soon takes on a sinister caste of murder, and Holmes must unravel the motives behind the targeted killing that set off the deadly chain of events.", 50, 30, 40, developer3)
game_repository.save(game4)

pdb.set_trace()