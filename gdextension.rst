.. _gdextension:

GDExtension edition (high-performance core)
=============================================

Vertex Studio provides two cores:

- **GDScript**: pure script, the original.
- **GDExtension**: a native core written in C++. Both have exactly the same features and the same interface, and both read and write the same files, so you can switch between them at any time by replacing the addon folder. And you don't need to compile anything, pre-compiled libraries are included.

The difference is that the **GDExtension edition supports meshes with millions of vertices**, while **the GDScript edition is limited to tens of thousands** (more than enough for low-poly and retro-stylized games).

.. note::
    Both editions require **Godot 4.3 or higher**. The native core is built against the 4.3 API, so it works on 4.3, 4.4, 4.5, 4.6 and 4.7.

.. tip::
    If you want to change the GDExtension's C++ code and/or compile it yourself, the C++ source-code is also available when you get the Pro version.

.. _gdextension-installation:

Installing the GDExtension edition
----------------------------------

- Download ``vertex_studio_gdextension_free-<version>.zip`` or ``vertex_studio_gdextension_pro-<version>.zip``.
- Extract it and move ``addons/vertex_studio`` into your project's ``addons`` folder, exactly like the GDScript edition. The only difference is an extra ``addons/vertex_studio/bin`` folder holding the compiled library.
- **Restart Godot** after installing or updating it.
- Enable the plugin in "Project > Project Settings... > Plugins".

If you are upgrading from the GDScript edition, delete the old ``addons/vertex_studio`` folder first.

.. tip::
    Not sure which one is installed? If ``addons/vertex_studio/bin`` exists, you have the GDExtension edition.

If the library cannot be loaded (an unsupported platform, or a Godot older than 4.3), Vertex Studio falls back to the GDScript implementation automatically.

.. _gdextension-differences:

GDScript vs GDExtension
-----------------------

- Support to painting meshes with hundreds of thousands to millions of vertices, whereas in the GDScript version the interface starts stuttering at around 50k vertices.

  - Painting up to about **1M triangles is smooth**. From **2M to 4M** it is still usable in real time, but expect the occasional stutter.

- ``Show Vertices`` becomes usable on dense meshes, and the vertex cloud is hidden while you navigate the viewport so orbiting stays responsive. BEWARE: depending on the machine configuration, ``Show Vertices`` can also cause performance issues even with the GDExtension version.

  - In the settings you can configure the *Very Dense Mesh Vertex Count* to make ``Show Vertices`` disable itself automatically in case it causes performance issues (see :doc:`project-settings`).

- Better backface and occluded-vertex performance. You can also paint through the mesh (x-ray) by disabling ``Show Front Verts Only``.

  - How smooth this feels still depends on the mesh: a dense self-occluding shape (torus, capsules, characters) might need disabling ``Show Vertices``.

- Painting is always live with the GDExtension version (the GDScript version is not usable on high poly meshes).
- Undo of a brush stroke only stores the vertices you actually touched, instead of a copy of every colour in the mesh.

See :doc:`view-options` for the display toggles and :doc:`project-settings` for the thresholds mentioned below.

.. _gdextension-always-show-vertices:

A note on Always Show Vertices
------------------------------

``Always Show Vertices``: past a few tens of thousands of vertices it draws so many squares that the result is an unreadable clump: you cannot tell one vertex from another, so the option stops being useful.

Because of that:

- Above the ``Dense Mesh Vertex Count`` project setting, Vertex Studio turns it off automatically (see :doc:`project-settings`).
- On dense meshes the cloud is **subsampled**: you see a uniform sample spread across the whole mesh rather than every single vertex. Vertices under the brush, selected ones and those inside a marquee are always drawn.

``Show Vertices`` on its own (vertices only while a tool is active) is the setting you want on a dense mesh.

.. _gdextension-normals-performance:

Painting normals on dense meshes
--------------------------------

Paint Normals is the heaviest tool in Vertex Studio, in both editions:

- Making an edge **smooth** is a cheap per-vertex change.
- Making an edge **hard** can be heavy: hard edges need one vertex per face, where the mesh has to be split and the surface is rebuilt. On a dense mesh it can cause stuttering, and it makes the mesh bigger, and filling a million-vertex mesh hard can roughly triple the vertex count.

To keep the editor usable, ``Fill All Hard`` and ``Fill All Smooth`` run in the background once the mesh is larger than the ``Async Fill Normals Vertex Count`` project setting (100,000 vertices by default).

Saving, updating and applying :doc:`variations` of dense meshes is also handled in the background (off the main thread).

.. _gdextension-saving:

Save dense scenes as .scn
-------------------------

For meshes above roughly **50,000 vertices**, save the scene as **.scn** (binary) instead of **.tscn** (text). You can do this by choosing "Scene > Save As..." and picking ``.scn``.

A painted mesh stores a colour per vertex inside the scene file. In a text scene those numbers are written out as text, which makes saving and loading slow, and creates larger files.

.. _gdextension-limitations:

Limitations
-----------

- The compiled library is provided for desktop. On any other platform the addon falls back to GDScript.

  - If you have Vertex Studio Pro, you also get the C++ source-code, so you can compile the GDExtension yourself for other platforms.

- Painting normals can stutter on dense meshes, as described above.
