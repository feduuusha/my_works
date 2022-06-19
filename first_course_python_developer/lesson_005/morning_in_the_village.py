from draw_function.rainbow import rainbow_curve_simple as rainbow
from draw_function.rainbow import list_of_colors
from draw_function.wall import house
from draw_function.smile import smile
from draw_function.snowdrift import snowdrift
from draw_function.tree import tree
from draw_function.sun import sun

smile(0, 320, 'yellow')
rainbow(350, 300, list_of_colors, 'blue')
snowdrift(-400, -300)
tree(350)
house(200, 200)
sun(-350, 300)
