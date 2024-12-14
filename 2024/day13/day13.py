from pprint import pprint
from dataclasses import dataclass
from functools import cache
import math

# @dataclass
# class Config:
#     price_x:int
#     price_y:int
#     a_cost:int
#     b_cost:int
#     a_times:int
#     b_times:int
#     a_disp_x:int
#     a_disp_y:int
#     b_disp_x:int
#     b_disp_y:int

#     def cost(self) -> int:
#         return self.a_times * self.a_cost + self.b_times * self.b_cost

#     def calculate_times(self):
#         self.b_times = self.price_y * self.a_disp_x - self.a_disp_y * self.price_x
#         self.b_times /= self.b_disp_y * self.a_disp_x - self.b_disp_y * self.a_disp_y
        
#         self.a_times = self.price_x - self.b_disp_x * self.b_times
#         self.a_times /= self.a_disp_x
        
#     def get_calculated_claw_position(self) -> tuple[int]:
#         return (self.a_disp_x * self.a_times + self.b_disp_x * self.b_times,
#                 self.a_disp_y * self.a_times + self.b_disp_y * self.b_times)

@dataclass(frozen=True)
class Position:
    x:int
    y:int
    def __add__(self, other):
        if not isinstance(other, Position):
            raise ValueError(f"Cannot add {other} to {self}")
        return Position(self.x + other.x, self.y + other.y)

@cache
def search(position:Position, cost:int, goal:Position, depth:int) -> int:
    # print(depth)
    print(position)
    disp_a = Position(94, 34)
    disp_b = Position(22, 67)
    
    if depth > 100:
        return math.inf
    
    if position == goal:
        print("found")
        return cost
    
    cost_a, cost_b = math.inf, math.inf
    
    position_a = position + disp_a
    if position_a.x <= goal.x and position_a.y <= goal.y:
        cost_a = search(position_a, cost + 3, goal, depth + 1)
        
    position_b = position + disp_b
    if position_b.x <= goal.x and position_b.y <= goal.y:
        cost_b = search(position_b, cost + 1, goal, depth + 1)
    
    return min(cost_a, cost_b)
    
    
    

def main() -> None:    
    # garden = list()
    # with open("test.txt") as f:
    #     for line in f:
    #         garden.append(list(line.strip()))
    # c = Config(price_x=8400, price_y=5400, a_cost=3, b_cost=1,
    #            a_times=0, b_times=0, a_disp_x=94, a_disp_y=34, b_disp_x=22, b_disp_y=67)
    # c.calculate_times()
    # print(c)
    # print(c.get_calculated_claw_position())
    # print(c.cost())
    print(search(Position(0, 0), 0, Position(8400, 5400), 0))
    
if __name__ == "__main__":
    main()