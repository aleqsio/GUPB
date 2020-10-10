from queue import SimpleQueue

import pygame
import sys      
from gupb.model import arenas
from gupb.model import characters
from gupb.model import coordinates
# noinspection PyUnusedLocal
# noinspection PyMethodMayBeStatic

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
MIST_TTH: int = 5
# top left of map is 0 0


class MyAwesomeController:
    def __init__(self):
        self.action_queue: SimpleQueue[characters.Action] = SimpleQueue()
        self.memory = dict()
        self.time = 0
        self.menhir_heading_map = dict()
        
    def computeMenhirMap(self):
        queue = []
        queue.append(
            (self.menhir_position, 0, None))
        while(queue):
            vPos, vDist, vSourceDir = queue.pop(0)
            if(vPos not in self.arena.terrain):
                continue
            if(vPos in self.menhir_heading_map and vDist >= self.menhir_heading_map[vPos]["distance"]):
                continue
            if(not self.arena.terrain[vPos].terrain_passable()):
                continue
            self.menhir_heading_map[vPos] = {
                "distance": vDist, "sourceDir": vSourceDir}
            for dir in dirs:
                queue.append((
                    vPos + coordinates.Coords(*dir), vDist + 1, dir if vDist > 0 else None))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MyAwesomeController):
            return True
        return False

    def __hash__(self) -> int:
        return 42

    def reset(self, arena_description: arenas.ArenaDescription) -> None:
        self.menhir_position = arena_description.menhir_position
        self.arena = arenas.Arena.load(arena_description.name) # we're just using the static method to avoid repeating parsing files
        self.computeMenhirMap()
        pass

    def invertCoords(self, coords):
        if coords is None:
            return None
        return coordinates.Coords(coords[0]*-1, coords[1]*-1)

    def getMistDistance(self, knowledge: characters.ChampionKnowledge):
        currentRadius = self.arena.mist_radius - (self.time // MIST_TTH) 
        playerMenhirDist = self.menhir_heading_map[knowledge.position]["distance"]
        return currentRadius - playerMenhirDist

    def decide(self,  knowledge: characters.ChampionKnowledge) -> characters.Action:
        decision = None
        self.updateTiles(knowledge)
        self.updateFacing(knowledge)
        print(self.getMistDistance(knowledge))
        preferedDir = self.invertCoords(
            self.menhir_heading_map[knowledge.position]["sourceDir"])
        if(preferedDir == self.facing):
            decision = characters.Action.STEP_FORWARD
        else:
            decision = characters.Action.TURN_LEFT
        # if(self.knowledge.)
       
       
        self.time+=1
        return decision

   
    @property
    def name(self) -> str:
        return 'MyAwesomeController'

    def updateFacing(self, knowledge: characters.ChampionKnowledge):
        for dir in dirs:
            if(knowledge.position + dir in knowledge.visible_tiles):
                self.facing = dir
                return

    def updateTiles(self,  knowledge: characters.ChampionKnowledge):
        for coords in knowledge.visible_tiles:
            self.memory[coords] = (self.time, knowledge.visible_tiles[coords])

POTENTIAL_CONTROLLERS = [
    MyAwesomeController(),
]

