from Pygine.modules.Components.BaseComponent import BaseComponent


class SpriteRenderer(BaseComponent):
    def __init__(self, sprite):
        super().__init__()
        self.name = "SpriteRenderer"
        self.sprite = sprite
