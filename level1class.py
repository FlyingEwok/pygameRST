import levelclass
import platformclass
import invisablehitmarkerclass
import enemyclass

# Create platforms for the level
class Level_01(levelclass.Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        levelclass.Level.__init__(self, player)
 
        self.level_limit = -1000
 
        # Array with width, height, x, and y of platform
        levelPlatform =[
                 [210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 [210, 70, 1120, 680]
                 ]

        levelHitMarker = [
                 [1, 140, 500, 360],
                 [1, 140, 709, 360]
                 ]

        enemyList = [
                [1, 1, 800, 520],
                [1, 1, 666, 550]
                ]
 
        # Go through the array above and add platforms
        for platform in levelPlatform:
            block = platformclass.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for hitmarker in levelHitMarker:
            marker = invisablehitmarkerclass.HitMarker(hitmarker[0], hitmarker[1])
            marker.rect.x = hitmarker[2]
            marker.rect.y = hitmarker[3]
            self.hitmarker_list.add(marker)

        for enemy in enemyList:
            enemy1 = enemyclass.Enemy()
            enemy1.level = self
            enemy1.rect.x = enemy[2]
            enemy1.rect.y = enemy[3]
            self.enemy_list.add(enemy1)
