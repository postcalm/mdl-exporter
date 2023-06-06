# Addition to the main README
Based on the last (for now) commit [443f9c5][1] from branch [2.8][2].

The plugin has been refined in Blender __3.2__. 

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

When exporting, the names of the textures used are extracted, as specified in the nodes, 
from all selected objects.

![truncate](<./images/Truncate Name.jpg>)

In the resulting file, the textures are written sequentially, ignoring the duplicates.
The very first texture has an index of __0__.

![textures](<./images/Exported Textures.jpg>)

After that, all the materials are written down. Each material is assigned an index of the texture used.

![textures](<./images/Exported Materials.jpg>)

The result of exporting to War3ModelEditor.

![textures](<./images/Export Result.jpg>)

---
[1]: https://github.com/khalv/mdl-exporter/commit/443f9c52ff0905cd0180fd7e5630f84707c07ba7
[2]: https://github.com/khalv/mdl-exporter/tree/2.8
