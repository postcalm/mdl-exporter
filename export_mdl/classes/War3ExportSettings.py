from mathutils import Matrix


class War3ExportSettings:
    def __init__(self):
        self.global_matrix = Matrix()
        self.use_selection = False
        self.optimize_animation = False
        self.optimize_tolerance = 0.05
        self.texture_path = ""
        self.texture_extension = ""
