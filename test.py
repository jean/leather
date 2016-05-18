#!/usr/bin/env python

import leather

# dot_data = [
#     (0, 3),
#     (4, 5),
#     (7, 9),
#     (8, 4)
# ]
#
# line_data = [
#     (0, 4),
#     (1, 3),
#     (2, 5),
#     (5, 6),
#     (9, 10)
# ]
#
# chart = leather.Chart()
# chart.set_x_scale(leather.LinearScale(0, 20))
# chart.add_dot(dot_data)
# chart.add_line(line_data)
# chart.to_svg('test.svg')

# dot_data = [
#     ('foo', 3),
#     ('bing', 5),
#     ('baz', 9),
#     ('blurg', 4)
# ]
#
# line_data = [
#     ('foo', 7),
#     ('bing', 2),
#     ('baz', 3),
#     ('blurg', 4)
# ]
#
# chart = leather.Chart()
# chart.add_column(line_data)
# chart.add_dot(dot_data)
# chart.to_svg('test.svg')

data = [[
    (0, 3),
    (4, 5),
    (7, 9),
    (8, 4)
], [
    (0, 4),
    (1, 3),
    (2, 5),
    (5, 6),
    (9, 10)
]]

grid = leather.Grid()

for series in data:
    chart = leather.Chart()
    chart.add_line(series)
    grid.add_chart(chart)

grid.to_svg('test.svg', 1200, 600)
