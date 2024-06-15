import turtle

def draw_image(coordinates, fill_color):
    turtle.speed(0) 
    turtle.pu()  
    turtle.title("Luna the Moon")

    if coordinates:
        turtle.goto(coordinates[0]) 
        turtle.pd()  
        turtle.ht()
        turtle.fillcolor(fill_color)  
        turtle.begin_fill()  
        for coordinate in coordinates:
            x, y = coordinate
            turtle.goto(x, y)
        turtle.end_fill()  

    turtle.pu()  
    turtle.home()    
    turtle.pd() 

def draw_images_from_files(file_colors):
    for fname, fill_color in file_colors.items():
        with open(fname, 'r') as file:
            fill_color = file.readline().strip()
            fcoordinates = [tuple(map(float, line.strip().split(','))) for line in file]
            draw_image(fcoordinates, fill_color)
    turtle.done()

file_colors = {
    'coordinates/d1': '#fff8e7',
    'coordinates/d2': '#ffa700',   
    'coordinates/d3': '#ffa700',
    'coordinates/d4': 'blue',
    'coordinates/d5': '#fffdd0',
    'coordinates/d6': '#fffdd0',
    'coordinates/d7': '#black',
    'coordinates/d8': 'black',
    'coordinates/d9': 'black',
    'coordinates/o1': 'black',
    'coordinates/o2': 'black',
    'coordinates/o3': 'black',
    'coordinates/o4': 'black',
    'coordinates/o5': 'black',
    'coordinates/o6': 'black',
    'coordinates/o7': 'black',
    'coordinates/o8': '#ffbcd9',
    'coordinates/o9': '#b31b1b',
    'coordinates/g1': 'white',
    'coordinates/g2': '#ff7f50',
    'coordinates/g3': '#ffa6c9',
    'coordinates/g4': "#ff7f50",
    'coordinates/g5': "#ff7f50",
    'coordinates/g6': "#cd5b45",
    'coordinates/g7': "#ff7f50",
    'coordinates/g8': "#cd5b45",
    'coordinates/g9': "#9fa91f",
    'coordinates/y1': "#9fa91f",
    'coordinates/y2': "#9fa91f",
    'coordinates/y3': "#9fa91f",
    'coordinates/y4': "#9fa91f",
    'coordinates/y5': "#ffa500",
    'coordinates/y6': "#ffa500",
    'coordinates/y7': "#ffa500",
}
draw_images_from_files(file_colors)