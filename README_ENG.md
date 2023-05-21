# Addition to the main README
Based on the last (for now) commit [443f9c5][1] from branch [2.8][2].

The version of Blender on which the plugin was refined and used is __3.2__.

The modification is intended only for work with __WMO objects__.
Workability with other formats is not guaranteed!

---
## Changes to export settings:
- Exporting "selected objects" is enabled by default

## Added features:
- The option to specify the path to textures (textures by default) and their extension (.blp by default)
- Texture names from WMO objects are exported.

---
## How does it work?

When exporting an object, its name is read, for example, _ICECROWN_DOOR_01_.
This name is truncated to _ICECROWN_DOOR_ (all numeric values with an underscore are truncated).

:warning: For this reason it is important that the name of the texture on your disk coincides with the name of the object in the editor!

![truncate](<./images/Truncate Name.jpg>)

---
[1]: https://github.com/khalv/mdl-exporter/commit/443f9c52ff0905cd0180fd7e5630f84707c07ba7
[2]: https://github.com/khalv/mdl-exporter/tree/2.8
