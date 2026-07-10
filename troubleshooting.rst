Troubleshooting
=========================================

I have performance issues. It's slow to paint vertex colors with Vertex Studio.
----------------------------

Try the following settings and toggles under "View":

1. **Keep "Focus Node tab while active".** If nothing happens, close Vertex Studio and open it again (you can deselect your Mesh from the Scene Tree and re-select it). The important thing is that the Godot's Inspector must not be the active tab while painting (don't ask me why, but it removes most performance issues).
2. **Reduce "Draw Dist".**
3. **Disable "Show Front Verts Only"** (caveat: there's no occlusion now when drawing, so you might end up drawing and selecting backface vertices).
4. **Disable "Always Show Vertices"** (only vertices under the cursor or under selections will appear)/
5. **In extreme scenarios, disable "Real-time painting".** Notice that with this disabled, when you paint, your changes will appear only when you release the mouse button.

.. image:: _static/images/vertex_studio_godot_troubleshooting-1.jpeg

.. image:: _static/images/vertex_studio_godot_troubleshooting-2.jpeg


Lastly, **try zooming in the Godot 3D Viewport**, getting as close as you can to your mesh and to the vertices that you want to work with, specially in denser meshes.
Zoomed out, thousands of vertices being rendered under the brush:

.. image:: _static/images/vertex_studio_godot_troubleshooting-3.jpeg

Zoomed in, just local vertices being rendered, the interface responsiveness is felt immediately:

.. image:: _static/images/vertex_studio_godot_troubleshooting-4.jpeg

Vertex Colors do not appear in my model
---------------------------------------

- If you have Vertex Studio active, make sure your mesh has the "Setup Material" (either unlit or lit).

.. image:: _static/images/trouble-setupmaterial.png

- If you are outside Vertex Studio and your model still does not show vertex colors, the mesh's material is not using the vertex color information. You can use Godot's ``StandardMaterial3D``, then check ``Vertex Color``, ``Use as Albedo``.

.. image:: _static/images/vertex_studio_godot_troubleshooting-6.jpeg

- If you want Vertex Studio to place the ``StandardMaterial3D`` in your mesh automatically, choose ``StandardMaterial3D`` in "Material - On restore".

.. image:: _static/images/trouble-materialrestore.png
````
When I paint, nothing happens
---------------------------------------

- **No material:** make sure your mesh has a material.

.. image:: _static/images/vertex_studio_godot_troubleshooting-8.jpeg

- **No vertex color information in the material:** make sure the mesh's material uses the vertex color. If you are in Vertex Studio, you can also click "Setup Unlit" or "Setup Lit" to use a material designed specially for the studio.

.. image:: _static/images/trouble-setupmaterial.png


- **Wrong channel:** Make sure you are painting in the RGBA channel.

.. image:: _static/images/vertex_studio_godot_troubleshooting-9.jpeg

- **Incorrect vertex selection:** you might have a selection active and you are not painting in the selection. Either paint the selected vertices or deselect everything.

.. image:: _static/images/vertex_studio_godot_troubleshooting-10.jpeg

When I paint in one of the separate R/G/B/A channels, nothing happens
---------------------------------------------------------------------

- You can set the value of the channels directly by using the "Value" slider
- You can visualize the individual channels in the Debug view

.. image:: _static/images/vertex_studio_godot_troubleshooting-11.jpeg

I can't see all of the mesh's vertices. The vertex I want is not showing up or I cannot paint it.
---------------------------------------

- Make sure you have "Show Vertices" active under "View". Also make sure "Vertex Size" and "Draw Dist" are in a reasonable value, so you can see the vertices.

.. image:: _static/images/vertex_studio_godot_troubleshooting-12.jpeg

- Make sure you don't have a selection active with other vertices. If you have an active selection you can either:
	- Add more vertices to the selection (choose one of the selection tools, then hold ``Shift`` while making a new selection).
	- Or deselect everything or invert selection.

.. image:: _static/images/vertex_studio_godot_troubleshooting-13.jpeg

The Split Shared Verts view mode is active, but vertices still show up as a single, merged vertex
---------------------------------------

.. image:: _static/images/vertex_studio_godot_troubleshooting-14.jpeg

Split vertices work only on hard edges. You can either make flat and hard faces with the 3D software of your choice, like Blender or you can use Vertex Studio "Paint Normals" brush and paint individual faces and vertices as hard or smooth. By painting vertices hard, they are automatically split. By painting them smooth, they are welded as a merged vertex.

.. image:: _static/images/vertex_studio_godot_troubleshooting-15.jpeg

The scene file with the MeshInstance3D where I painted vertex colors is too big and/or is taking too long to load
---------------------------------------

Save the scene as a binary scene (``.scn``) instead of a text scene (``.tscn``).