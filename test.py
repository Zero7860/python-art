import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Cristiano Ronaldo Pixel Art")
screen.bgcolor("white")

# Define color mappings
colors = {
    'K': '#000000',  # Black outline
    'B': '#663300',  # Brown hair
    'S': '#FFCC99',  # Skin tone
    'W': '#FFFFFF',  # White eyes
    'R': '#FF0000',  # Red jersey
    'L': '#0000FF',  # Blue collar
    'Y': '#FFFF00'   # Yellow details
}

# Pixel grid (15x15)
pixels = [
    "KKKKKKKKKKKKKKK",
    "KBBBBBBBBBBBBBBK",
    "KBBBBBBBBBBBBBBK",
    "KBBBBBBBBBBBBBBK",
    "KSSSSSSSSSSSSSSK",
    "KSSSWWKKKWWSSSSK",
    "KSSSKSSSSSKSSSSK",
    "KSSSKSSSSSKSSSSK",
    "KSSSSSSSSSSSSSSK",
    "KSSSSKKKKKSSSSSK",
    "KSSSSSSSSSSSSSSK",
    "KRRRRRRRRRRRRRRK",
    "KRRRRRRRRRRRRRRK",
    "KRRRRLLLRRRRRRRK",
    "KKKKKKKKKKKKKKKK"
]

# Set up turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Calculate starting position (top-left corner)
start_x = -150
start_y = 150

# Draw pixel art
for y in range(len(pixels)):
    row = pixels[y]
    for x in range(len(row)):
        color_char = row[x]
        color = colors.get(color_char, '#FFFFFF')  # Default to white
        
        # Calculate position
        x_pos = start_x + x * 20
        y_pos = start_y - y * 20
        
        # Draw square
        pen.goto(x_pos, y_pos)
        pen.pendown()
        pen.begin_fill()
        pen.color(color)
        for _ in range(4):
            pen.forward(20)
            pen.right(90)
        pen.end_fill()
        pen.penup()

# Finish up
turtle.done()