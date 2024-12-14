from pprint import pprint
from dataclasses import dataclass
from collections import Counter
import math


@dataclass
class Vector2:
    x:int
    y:int
    def __add__(self, other):
        if not isinstance(other, Vector2):
            raise ValueError(f"Cannot add {other} to {self}")
        return Vector2(self.x + other.x, self.y + other.y)
    
@dataclass
class Robot:
    position:Vector2
    velocity:Vector2
    
    def move(self, space_dim:Vector2):
        self.position.x = (self.position.x + self.velocity.x) % space_dim.x
        self.position.y = (self.position.y + self.velocity.y) % space_dim.y

    def quadrant(self, space_dim:Vector2) -> tuple[int] | None:
        h, v = 0, 0
        if self.position.x == space_dim.x // 2 or self.position.y == space_dim.y // 2:
            return None
        
        if self.position.x < space_dim.x // 2:
            h = -1
        elif self.position.x > space_dim.x // 2:
            h = 1
            
        if self.position.y < space_dim.y // 2:
            v = -1
        elif self.position.y > space_dim.y // 2:
            v = 1
        return (h, v)

def main() -> None:    
    space_dim:Vector2 = Vector2(101, 103)
    
    robots:list[Robot] = list()
    with open("input.txt") as f:
        for line in f:
            pos = line.split(" ")[0]
            vel = line.split(" ")[1]
            posx = int(pos.split("=")[1].split(",")[0])
            posy = int(pos.split("=")[1].split(",")[1])
            velx = int(vel.split("=")[1].split(",")[0])
            vely = int(vel.split("=")[1].split(",")[1])
            robots.append(
                Robot(position=Vector2(posx, posy), velocity=Vector2(velx, vely))
            )

    # simulation 100 seconds
    for seconds in range(100):
        space = [[0] * space_dim.x for h in range(space_dim.y)]
        for robot in robots:
            space[robot.position.y][robot.position.x] += 1
            robot.move(space_dim=space_dim)
        
        # visual repr steps
        # print(f"Step: {seconds}")
        # for r in space:
        #     s = ""
        #     for c in r:
        #         s += str(c)
        #     print(s)

    # count quadrants
    cnt = Counter()
    for robot in robots:
        cnt[robot.quadrant(space_dim)] += 1
    
    # multiply quadrants count
    total = 1
    for key in cnt.keys():
        if key is not None:
            total *= cnt[key]
            
    print(cnt)
    print(total)
        
    
    
if __name__ == "__main__":
    main()