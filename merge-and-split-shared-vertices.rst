Merge and Split Shared Vertices
=========================================

What shared vertices are
------------------------

On a smooth surface, the faces around a corner share one single vertex. On a hard edge they can't: each face needs its own normal at that corner, so the mesh stacks several vertices in the exact same position, one per face. They are shared in the sense that they sit at the same place, and each one carries its own normal and its own color.

That detail matters for vertex painting, because a "physical vertex" you see in the viewport can actually be two, three or more vertices on top of each other, and each one can hold a different color.

Vertex Studio gives you both behaviours, and you switch between them in the ``View`` section (see :doc:`view-options`).

.. image:: _static/images/manual/merge-split-toggle.png

Merge Shared Vertices
---------------------

The default mode: vertices stacked in the same position are painted together and drawn as a single square, so a corner reads as one vertex and gets one color ("one physical vertex, one color").

.. image:: _static/images/manual/merge-split-merge.png

Split Shared Vertices
---------------------

.. note::
    This mode requires Vertex Studio Pro ⭐.

The stacked vertices fan apart on screen around their real position, each square drawn in its own color with a thin line back to the point they belong to. Now you can paint each face's corner with a different color, which is how you get a sharp color change across an edge instead of a gradient, the classic N64 and PS1 look.

.. image:: _static/images/manual/merge-split-split.png

The fan is only for picking, the vertices never move: as soon as you go back to Merge, the squares collapse back into one.

.. tip::
    The ``Precision Paint Brush`` is the comfortable way to paint a fan, it locks onto the individual vertex under the cursor with no brush size involved. See :doc:`brushes-painting-tools`. If you want to paint all vertices on the fan at once, just use the brush, normally.

.. tip::
    Selection tools can select individual vertices on the split fan.

.. note::
    Split only has something to fan out where the mesh actually has hard edges. On a fully smooth model every corner is a single vertex, so both modes look the same. To create the hard edges, use the ``Paint Normals`` brush below.

Paint Normals
-------------

.. note::
    This feature requires Vertex Studio Pro ⭐.

``Paint Normals`` is a brush that edits vertex normals instead of colors, so you can make edges hard or smooth directly in Godot, without going back to Blender.

.. image:: _static/images/manual/painting-normals.png

With the tool active, ``Paint Settings`` shows a ``Mode`` row:

- ``Hard``: the brushed corners become faceted, each face keeps its own normal.
- ``Smooth``: the brushed corners are averaged, so the edge shades smoothly.

Brush size still applies, opacity and falloff do not: a normal is either hard or smooth, there is nothing in between.

While the tool is active, the vertex squares are colored by their current state instead of their color:

- Light **red** for *hard*.
- Light **blue** for *smooth*.

.. image:: _static/images/manual/paint-normals-red-blue.png

.. important::
    Painting normals is topological, it changes the mesh: making an edge hard splits the corner into one vertex per face, and making it smooth welds those vertices back into one. Tangents are regenerated afterwards.

    Since a welded vertex can only hold one color and one UV, corners painted with different colors don't fully weld: they keep their separate vertices but shade smoothly.

Fill Normals
^^^^^^^^^^^^

With the tool active, the panel also shows a ``Fill Normals`` section to set the whole mesh at once:

.. image:: _static/images/manual/normals-fill.png

.. image:: _static/images/manual/normals-fill-selection.png

- ``Fill All Hard`` / ``Fill All Smooth``: apply to every vertex.
- With an active selection the buttons become ``Fill Selection Hard`` / ``Fill Selection Smooth`` and apply only to the selected vertices.

.. video:: _static/videos/paint-normals-smooth-hard.mp4
    :width: 100%

.. tip::
    Use the ``Setup Lit`` material while editing normals (see :doc:`material-setup`). The unlit material shades everything flat, so you won't see the difference between a hard and a smooth edge.

Workflow: from a smooth model to painted hard corners
-----------------------------------------------------

1. With ``Paint Normals`` in ``Hard`` mode, brush the edges you want faceted (or use ``Fill All Hard`` for a fully faceted look).
2. Switch to ``Split Shared Vertices`` in ``View``. The corners you made hard now fan apart.
3. Pick the ``Precision Paint Brush`` and paint each corner of the fan with its own color.
4. Go back to ``Merge Shared Vertices`` when you are done, so normal painting behaves as usual again.

.. tip::
    Both the merge and split toggle and the normals tool can be bound to a key, see :doc:`shortcuts`.
