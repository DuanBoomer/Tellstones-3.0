from ursina import *
from ursina import curve,camera
app=Ursina()
camera.z+=9
#Text(parent=camera.ui,text=u'\u00a9''2021 Orks', origin=(4.85,18), background=False)
class stone(Entity):
    def __init__(self,texture,position):
        super().__init__(
            model='plane',
            position=position,
            scale=(1,1,1),
            texture=texture,
            color=color.white,
            rotation_x=-90,
            collider='box',
        )

        self._texture_=texture
        self.swap_r_=False
        self.swap_l_=False

    def update(self):
        hit_info = raycast(origin=self.world_position ,direction=(0,0,0), ignore=(self,), distance=.25, debug=False)
        if hit_info.hit and self.swap_r_==True:
            hit_info.entity.x-=1
            self.swap_r_=False
        if hit_info.hit and self.swap_l_==True:
            hit_info.entity.x+=1
            self.swap_l_=False
        else:pass

    def swap_r(self):
        self.swap_r_=True
        self.animate_x(self.x+1,curve=curve.linear)
    def swap_l(self):
        self.swap_l_=True
        self.animate_x(self.x-1,curve=curve.linear)
    def hide(self):
            self.texture='hidden.png'
    def unhide(self):
            self.texture=self._texture_

    def input(self,key):
        if key=='left arrow' and self.hovered==True:
            self.swap_l()
        if key=='right arrow' and self.hovered==True:
            self.swap_r()
        if key=='a' and self.hovered==True:
            self.hide()
        if key=='s' and self.hovered==True:
            self.unhide()
        
scale=stone('scale.png',(0,0,0))
knight=stone('knight.png',(1,0,0))
flag=stone('flag.png',(2,0,0))
hammer=stone('hammer.png',(3,0,0))
sword=stone('sword.png',(-1,0,0))
shield=stone('shield.png',(-2,0,0))
crown=stone('crown.png',(-3,0,0))
line=Entity(
    model='plane',
    rotation_x=-90,
    position=(0,0,0.5),
    color=color.white,
    scale=(8,0,1.7),
    texture='line.jpg',
    )

Sky(texture='sky_sunset')
app.run()
