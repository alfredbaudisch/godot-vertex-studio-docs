FAQ
=========================================

What is the minimum version of Godot required?
---------------------------------------

Godot 4.3 or higher.

Is there undo and redo support?
----------------------------------

Yes, undo history is implemented, you can undo and redo normally in Godot.

.. _faq-max-triangles:

What is the maximum amount of triangles per mesh that Vertex Studio can handle?
---------------------------------------------------------------------

From my tests, up until 20k triangles per mesh (plus children meshes) there's barely any noticeable performance impact.

If you have a scene with multiple separate meshes, there's no performance impact at all even if the scene has hundreds of thousands of triangles, since Vertex Studio processes only the currently selected mesh (and its children).

From 20k to 80k triangles in a single mesh, it's still possible to paint and select vertices, but the brush starts to get sluggish.

I even tested painting a mesh with 2.5 million triangles, and Godot nor the addon crashed, but each brush stroke took a few seconds to complete.

When dealing with denser meshes, be sure to disable ``Show Wireframe``, ``Show Vertices`` and ``Always Show Vertices`` under ``View``.

.. image:: _static/images/faq-disable-performance.png
