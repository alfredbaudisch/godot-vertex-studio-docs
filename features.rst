Features
=========================================

Vertex Studio is a Godot plugin for **editing, managing and painting vertex colors and vertex normals** of 3D meshes. A complete solution for vertex painting inside the Godot editor. Vertex Studio is a must-have tool for making games inspired by PS1, N64 or early PC games aesthetics, but it's useful even in modern workflows, since vertex coloring can also be used for texture blending and masking.

.. video:: _static/videos/vertexstudio-features-overview-captioned.mp4
  :width: 100%


.. _features-details:

Vertex Studio features in details
---------------------------------

.. note::
    Features marked with ⭐ are only available in the Pro edition.

Vertex Studio brushers and selections work in both **perspective and orthographic** viewports, so you can freely move the camera in the 3D Viewport while painting and selecting.

* **Vertex color painting**

  * **Paint Vertex Colors brush** (:kbd:`B`): a screen-space brush (consistent size in pixels regardless of zoom) for coloring vertices straight onto the mesh in the viewport.

    * Supports painting both on **static** and **skeletal/skinned animated meshes** (even if the mesh is in the middle of an animation). See the :ref:`FAQ <faq-skeletal-mesh>`.

  * **Adjustable opacity, applied stroke-relative**: like Blender and Photoshop, holding and dragging over the same vertices applies the opacity **once per stroke** instead of stacking up and darkening as you pass over them again.
  * **Eraser** (:kbd:`Shift+E`): the eraser is also a brush, so its opacity controls how **hard or soft** it erases, restoring vertices back toward white.
  * **Bucket Fill**: fill (:kbd:`G`) **every vertex** (``Fill All``) or just the **active selection** (``Fill Selection``), plus the reverse, ``Erase All`` / ``Erase from Selection``. Fill respects opacity, so filling repeatedly builds the color up.
  * **Blur**: a smoothing brush that nudges each vertex's color toward the average of its **1-ring neighbours** (crossing hard-edge seams too), creating soft gradients.
  * **Replace Colors by threshold** ⭐: swap one color for another in a selection or the whole mesh, within an adjustable tolerance.
  * Full **RGBA** painting (default) or **single-channel painting (R / G / B / A)** ⭐: paint into **just one channel** or **add multiple channel combinations** (by holding :kbd:`Shift`) or set a channel's grayscale value from 0.0 to 1.0 with a dedicated ``Value`` slider while leaving the others untouched, ideal for **packing masks** (for example, ambient occlusion in one channel or `multi-texture blending <https://alfredbaudisch.github.io/godot-vertex-studio-docs/multi-texture-blending-tutorial.html>`_).
  * **Brush falloff curves** ⭐: shape the brush's strength profile with Godot's **curve editor**. Different falloff graphs effectively become **different brushes and "stamps"**.
  * **Paint Precision tool** ⭐: a point-and-click tool with **no brush size** that locks onto the exact vertex/point under the cursor, so you can paint **individual vertices** accurately (and individual split corners of hard edges).

* **Vertex selection & masking**

  * **Single Selection (Point)**: click individual vertices (it's possible to add to the selection while holding :kbd:`Shift` and remove from selection while holding :kbd:`Alt`).
  * **Lasso, Rectangle and Ellipse selection** ⭐: marquee tools for fast, complex, **arbitrary/weirdly shaped selections** that would be painful to do vertex by vertex.
  * **Select All**, **Deselect** (:kbd:`Shift+L`), and **Invert Selection** ⭐.
  * **Select Linked (by material)** ⭐: select **whole surfaces at once** by their material, picked from a list of the mesh's materials (like Blender).
  * **Add / remove modifiers**: hold :kbd:`Shift` to **add** to a selection and :kbd:`Alt` to **remove**, with any selection tool.
  * **Selections mask your painting**: while a selection is active, the brush, eraser and fill only affect the selected vertices.

* **Colors, swatches & palettes**

  * **Color picker** with reusable **swatches**: click ``+`` to add the current color, **right-click** a swatch to remove it, and cycle through them while painting with :kbd:`X`.
  * **Eyedropper**: sample a vertex's color back into the brush.
  * **Import PNG palettes**: pull colors straight out of a PNG image (for example, palettes from **Lospec**).
  * **Save / Load palettes** as **Godot Resource files**, so your palettes are reusable across scenes and projects.

* **Vertex & face normals (hard / smooth)**

  * **Paint Normals brush** ⭐: brush vertices between **hard and smooth** shading. It's **topological** (it welds and splits vertices per face) and **regenerates tangents**.
  * **Fill Normals** ⭐: set the **whole mesh or the current selection** to hard or smooth in one click.

* **Shared & split vertices** (the stacked corners of hard edges)

  * **Merge mode**: coincident vertices at a hard edge paint **together** and read as one smooth vertex.
  * **Split mode** ⭐: stacked corner vertices **fan apart on screen** so you can paint **each face's corner its own color**, then collapse back. It allows you to get multiple colors per "physical vertex".

* **Vertex Groups** ⭐ (like Blender)

  * Save and manage **named selections of vertices** onto the mesh.

* **Variations** ⭐: non-destructive variations of a single mesh

  * A Variation captures a **full snapshot** of the mesh: **vertex colors**,  **active selection**, **vertex groups**, AND the **normal / surface topology** (hard and smooth splits).
  * Saved as **Godot Resource files**: create, overwrite, load and delete them from the ``Variations`` panel.
  * Great for **seasons, day/night, damage or dirt states**, and anything else where the same mesh needs to look differently. Or just to create non-destructive workflows.

* **Runtime switching & blending** ⭐: the ``VSRuntime`` node

  * Add a **VSRuntime child** to any ``MeshInstance3D`` to switch Variations from the **Inspector** and/or **in-game at runtime** via an API.
  * **Restore base instance**: re-link a painted world instance back to its **source scene** (dropping the local mesh override) non-destructively, even after you've already overridden it locally.
  * **Blend / tween between two Variations** (EXPERIMENTAL): smoothly interpolate a mesh from one Variation to another over time; **vertex colors all blend at once**, allowing for mesh morphing: day ↔ night, healthy ↔ damaged, cold ↔ hot, etc.

    * **GPU blending**: the entire tween is a **single shader uniform**. Uses Vertex Studio's bundled **lit / unlit blend shaders**. Faster than CPU blending, but no custom material support.
    * **CPU blending**: slower than GPU blending, but it **keeps your mesh's own custom material / shader**.

* **Materials & view modes** (non-destructive)

  * **One-click paint material** (``Setup Lit`` / ``Setup Unlit``) applied as a per-surface **override**, so your mesh's real materials are **never touched** and are **automatically restored** when you close Vertex Studio (or immediately via ``Restore Material``).
  * **Debug channel view**: isolate and inspect the **R, G, B or A** channel on its own.
  * **View toggles** useful for debugging, readability and performance: ``Show Textured``, ``Show Vertex Colors``, ``Show Front Verts Only`` (aka "X-Ray" view) and ``Always Show Vertices`` .

* **Base mesh & world instances workflow**

  * Paint a **base scene** once and every instance usage **updates automatically**.
  * Paint **specific world instances** for per-instance details (baked into that scene) or keep them fully non-destructive with **Variations + VSRuntime** ⭐.
  * Full Godot's **Editable Children** support, so you can paint a single instance and override it without affecting the base mesh.

* **Editor integration & workflow**

  * **Tools & Tool Settings popup**: press :kbd:`Ctrl+F` over the viewport for a floating tool popup like Photoshop and Blender.
  * Full **Undo / Redo** integration with Godot's editor history, including the topology-changing normal edits.
  * **Keyboard shortcuts** (see :doc:`shortcuts`).
  * **Settings persist** between sessions, and each mesh's Variation history is saved **with the scene** (and can be alternated in the scene with **Variations**).

* **Performance considerations**

  * A per-mesh **occlusion BVH** alongside a camera memoized visibility helps hide occluded vertices and tries to keep the workflow fast even on higher poly, self-occluding meshes (NOTICE: it's not a silver bullet).
  * On denser meshes realtime rebuilds try to automatically defer to the end of the stroke.
  * See the FAQ: :ref:`What is the maximum amount of triangles per mesh that Vertex Studio can handle? <faq-max-triangles>`

* **Free versus Pro ⭐**

  * **Free** includes the core, essential features for vertex painting: brush, eraser, bucket fill, opacity, point selection, select all / deselect, swatches & palettes (including PNG import), blur, debug views, view modes and the non-destructive material setup.
  * **Pro** ⭐: everything from Free plus lasso / rectangle / ellipse & linked selection tools, invert selection, split-vertex painting, paint precision, paint normals, vertex groups, replace colors, single-channel R/G/B/A painting, falloff curve editing, and Variations + the VSRuntime node (Inspector/runtime switching and snapshot blending).
