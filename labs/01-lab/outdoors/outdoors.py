from .lake import draw_lake
from .park import draw_park

def draw_outdoors():
    print("@ Outdoor attractions:")
    draw_lake()
    draw_park()
    return
