# CodeSkulptor executa programas Python em seu navegador.
# Clique no botão superior esquerdo para executar esta demonstração simples.

# CodeSkulptor é testado para rodar em versões recentes do
# Chrome, Firefox, Safari e Edge.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Manipulador para desenhar na tela

def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

#Crie um quadro e atribua retornos de chamada a manipuladores de eventos
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
