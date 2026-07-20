View and Debug Options
=========================================

View Options
------------

.. thumbnail:: _static/images/manual/view-modes.png
    :width: 50%

1. Toggle mesh's wireframe (it overlays on top of the mesh)
2. Toggle vertex colors
3. Toggle texture(s) (if the mesh has any textures)

.. note::
    Options 2 and 3 only work if you have Vertex Studio's "Setup Material" active. See :doc:`material-setup`.

4. Toggle display vertex overlay (display vertices as squares over the mesh, each square is colored with its vertex color)

    - Keep off if you are suffering from performance issues.

5. Always Show Vertices:

    - On: display all vertices, regardless of whether they are under the brush/cursor or selected.
    - Off: display only vertices under the brush/cursor or selected vertices.
    - Keep off if you are suffering from performance issues.

6. Show front vertices only: display only the vertices that are facing the camera. When off, works like a kind of "x-ray" view, showing all vertices, allowing to select and paint front and backface vertices.

7. Merge Shared Vertices: paint every vertex sharing a position together (smooth/soft-normal corners and smooth, soft-normal look).

    - Displayed as a "single square" per vertex.
    - Default vertex painting mode.
    - See :doc:`merge-and-split-shared-vertices`.
    .. image:: _static/images/manual/merge-split-merge.png

8. Split Shared Vertices: fan coincident hard-edge vertices apart so each face's corner can hold its own color.

    - Displayed as "multiple squares" fanning out from the "physical vertex" per vertex.
    - Requires hard edges / flat shading. You can create hard edges with the ``Paint Normals`` brush tool. See :doc:`merge-and-split-shared-vertices`.
    .. image:: _static/images/manual/merge-split-split.png

9. Vertex Size: how big the vertex overlay squares are.
10. Draw Distance: how far the vertex overlay squares are visible.

Debug and Performance Options
-----------------------------

.. thumbnail:: _static/images/manual/view-debug-channels.png
    :width: 50%

1. Debug RGBA channels:

    - Off: display all channels of the vertex colors.
    - R, G, B, A: toggle the display of only the red, green, blue, or alpha channels of the vertex colors.

.. note::
    Debugging views only work if you have Vertex Studio's "Setup Material" active. See :doc:`material-setup`.

.. tip::
    For more information about the RGBA channels, see :doc:`rgba-channels`. And for a real usage example, see :doc:`multi-texture-blending-tutorial`.

2. Real-time painting:

    - When active, the vertex colors are updated in real-time as you paint (just like any painting application like Krita, Photoshop, etc.).
    - When inactive, the vertex colors are updated only when you release the mouse.
    - Keep inactive if you are suffering from performance issues.

3. Hide Inspector while active: While a tool is active, switch the editor's Node to Signals or Groups so the Inspector doesn't repaint on every stroke (fixes slow or "jumping" painting).

    - Since Vertex Studio works by modifying the ``MeshInstance3D`` mesh data, Godot's Inspector keeps refreshing and repainting on every stroke, causing slow or "jumping" painting, that's why this option was added, which automatically make Godot switch to Signals or Groups while a tool is active.