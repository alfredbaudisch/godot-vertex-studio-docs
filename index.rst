.. Vertex Studio Documentation documentation master file, created by
   sphinx-quickstart on Thu Jul  9 16:12:13 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Vertex Studio Documentation
=========================================

Vertex Studio is a **complete solution for editing, painting and managing vertex colors and vertex normals** of 3D meshes inside Godot. It has tools for:

- Painting and filling vertices (brush, eraser, opacity adjustment, brush falloff, color palettes, bucket fill, blur, color replacement by threshold, RGBA channel selection).
- Selecting vertices (lasso, rectangle and ellipse selection); linked by material selection (like Blender).
- Changing vertex and face normals between hard and smooth.
- Painting individual vertices or split vertices (shared vertices of hard edges, allowing for multipler colors in a single "physical vertex").
- Grouping vertices into vertex groups like Blender.
- Creating and managing variations/snapshots of vertex colors, selections and vertex smoothness topology, creating non-destructive variations of a single mesh.
- Switching between mesh variations at runtime and blending between variations.

See the :doc:`features` page for every feature in detail.
 
.. video:: _static/videos/vertexstudio-features-overview-captioned.mp4
  :width: 100%

Where to get it
----------------

See the :doc:`installation` page.

How to use it
--------------

See the :doc:`quickstart-guide` page.

.. image:: _static/videos/vertexstudio-final-result.gif


.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Quickstart
   
   features
   installation
   quickstart-guide
   shortcuts
   advanced-tutorial

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Manual

   interface
   material-setup
   view-modes
   brushes
   selection-tools
   vertex-groups
   variations
   runtime-and-api
   settings-and-preferences

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Support
   
   faq
   troubleshooting