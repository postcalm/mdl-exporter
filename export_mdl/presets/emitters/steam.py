import bpy
psys = bpy.context.object.particle_systems.active.settings.mdl_particle_sys

psys.emitter_type = 'ParticleEmitter2'
psys.model_path = ''
psys.texture_path = 'Textures\\Clouds8x8Mod.blp'
psys.filter_mode = 'Blend'
psys.emission_rate = 10
psys.life_span = 4.0
psys.speed = 80
psys.gravity = 20.0
psys.longitude = 0.0
psys.latitude = 20
psys.ribbon_material = None
psys.ribbon_color = (1.0, 1.0, 1.0)
psys.variation = 0.20000000298023224
psys.head = True
psys.tail = False
psys.tail_length = 0.0
psys.start_color = (1.0, 1.0, 1.0)
psys.start_alpha = 0
psys.start_scale = 20
psys.mid_color = (1.0, 1.0, 1.0)
psys.mid_alpha = 150
psys.mid_scale = 30
psys.end_color = (1.0, 1.0, 1.0)
psys.end_alpha = 0
psys.end_scale = 40
psys.time = 0.4000000059604645
psys.rows = 8
psys.cols = 8
psys.head_life_start = 0
psys.head_life_end = 32
psys.head_life_repeat = 1
psys.head_decay_start = 32
psys.head_decay_end = 64
psys.head_decay_repeat = 1
psys.tail_life_start = 0
psys.tail_life_end = 0
psys.tail_life_repeat = 1
psys.tail_decay_start = 0
psys.tail_decay_end = 0
psys.tail_decay_repeat = 1
psys.unshaded = True
psys.unfogged = False
psys.line_emitter = False
psys.sort_far_z = False
psys.model_space = False
psys.xy_quad = False