from manim import *

class Anima(Scene):
    def construct(self):
        
        t = Text('T',font_size=200,color=BLUE)
        
        t.move_to([5,0,0])
        self.play(Write(t))
        self.play(t.animate.move_to(LEFT*2))

        #star
        star = Star(color=RED,fill_opacity= 0.2)
        star.move_to([5,0,0])
        self.play(Create(star))
        self.wait()

        #square
        square= Square(fill_opacity= 0.2)
        square.move_to([5,0,0])
        


        self.play(star.animate.move_to(LEFT*4))
        self.play(Rotate(star,PI))

        t1= Text('RUMINDS')
        self.play(Write(t1))

        self.play(Create(square))
        self.play(square.animate.move_to([3,-1,-2]))
        self.play(square.animate.set_color(BLUE))
        self.play(Rotate(square,PI))

        #line

        line = Line(fill_opacity=4).set_color(ORANGE)
        line.move_to([-1.2,-0.5,-1])
        self.play(Create(line))

        self.play(line.animate.move_to([1.5,-0.5,1]))
        self.play(Uncreate(line))
        

        self.wait(2)

        self.play(Uncreate(t1))
        self.play(Uncreate(star)) 
        self.play(Uncreate(square))
        self.wait()
        self.play(Unwrite(t))
        