from drunk import Drunk
from field import Field
from coords import Coords
from bokeh.plotting import figure, show

def walk(field, drunk, distance):
    start = field.get_coord(drunk)

    for _ in range(distance):
        field.move(drunk)

    return start.distance(field.get_coord(drunk))

def run_simulation(distance, trys, drunk):
    person = drunk(name='Martin')
    origin = Coords(0,0)
    distances = []

    for _ in range(trys):
        field = Field()
        field.add_coord(person, origin)
        simulation = walk(field, person, distance)
        distances.append(simulation)

    return distances

def draw(x,y):
    graphic = figure(title='Path', x_axis_label='Steps', y_axis_label='Distance')
    graphic.line(x,y,legend_label='Average Distance')
    show(graphic)

def main(distances, trys, drunk):
    average_distances = []
    for i in distances:
        results = run_simulation(i, trys, drunk)
        average = round(sum(results) / len(results), 4)
        maxd = max(results)
        mind = min(results)
        average_distances.append(average)
        print(f'{drunk.__name__} walked {i} steps')
        print(f'Average: {average}')
        print(f'Max: {maxd}')
        print(f'Min: {mind}')
    draw(distances, average_distances)


if __name__ == '__main__':
    distances = [10, 100, 1000, 10000]
    trys = 100

    main(distances, trys, Drunk)