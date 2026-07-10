Quickstart Guide (How to Use)
=========================================

Vertext Studio is complete solution for editing vertex colors and vertex normals of 3D meshes in Godot. See all the features in the :doc:`features` page.

This is a how to use / quickstart guide / tutorial to get you started with Vertex Studio.

!! TODO: this is the scene before and after !!

Project and addon setup
-----

If you want to follow along with the tutorial, you can download the sample project here. Extract the zip file and open the project in Godot.

Then, download and activate the addon in your Godot project (the sample project does not come with the addon). See the :doc:`installation` page for more details.

Part 1: Material setup and basic vertex painting with the brush and the eraser
---------------------------------------------------------------------------

Let's start by painting the archway base mesh.

.. video:: _static/videos/vertexstudio-tutorial01.mp4
  :width: 100%

1. Open the "Scenario" scene and click the "Archway" node in the SceneTree.
2. Activate Vertex Studio.
3. Setup the :doc:`Vertex Studio material <materials>` by clicking the ``Setup Unlit`` under the ``Material`` secton. We are choosing the unlit material because we do not want lighting or shadows affecting the viewport and the mesh.

.. image:: _static/images/tut-setupmaterial.png

.. note::	
    What happens with the material originally assigned to the mesh? Vertex Studio will automatically restore the material once the interface is closed. You can also restore it immediately by clicking the ``Restore Material`` button (the one with the counterclockwise arrow icon).
    
    You can alternate between the original material and the setup materials any time by clicking the buttons as needed. This workflow is actually encouraged to visualize between the Studio and the final result.

4. Select the ``Paint Vertex Colors`` (aka "Brush") tool by clicking its icon, pressing :kbd:`B`, or by opening the tools popup in the viewport with :kbd:`Ctrl+F` and clicking the Brush icon.

.. image:: _static/images/tut-brushicon.png

5. Select a color, reduce the opacity, and paint the inner part of the archway.

.. image:: _static/images/tut-pickcolor-andopacity.png

6. In the viewport, you can increase and decrease the brush size by holding :kbd:`]` and :kbd:`[` respectively. You can also cycle through colors from the palette (Swatches) by pressing :kbd:`X` (or also open the tools popup with :kbd:`Ctrl+F`, but from now on, I'm not going to repeat this information).

7. If you make a mistake, you can undo normally or use the ``Eraser`` tool by clicking its icon or by pressing :kbd:`Shift+E`. The eraser is also a brush, thus opacity also affects how hard or soft the eraser is.

.. image:: _static/images/tut-eraser.png

Part 2: Vertex selection and bucket fill
---------------------------------------------------------------------------

.. video:: _static/videos/vertexstudio-tutorial02.mp4
  :width: 100%

I want to make the base of the archway darker. Let's select the base vertices and fill them with a darker color.

1. In order to make it easier to view vertices that are on the back, disable ``Show Front Verts Only`` under ``View`` (1).

You can also toggle the texture with ``Show Textured`` (2) in order to make it easier to see just the vertex colors.

.. image:: _static/images/tut-showfrontverts.png

2. To paint only a few selected vertices without affecting unwanted vertices, you can use the ``Single Selection`` tool. Click individual vertices to select them. To **add to the selection**, you can hold :kbd:`Shift` while clicking. To **remove from the selection**, you can hold :kbd:`Alt` while clicking previously selected vertices.

.. image:: _static/images/tut-singleselection.png

3. You can fill the selected vertices with the ``Fill Selection`` (aka "Bucket Fill", also activated with :kbd:`G` key) (1) tool or you can paint the selected vertices with the brush (since now there's an active selection, the other vertices will be masked out). The bucket fill also uses the opacity setting, so filling repeteadly will add the color to the selection.

If you want, you can first ``Erase from Selection`` (2) to clear the colors from the selected vertices, and then fill again.

.. image:: _static/images/tut-fill.png

.. note::	
    When there is no active selection, the bucket fill tool is shown as ``Fill All`` and the clear tool is shown as ``Erase All``, and both affect all vertices (i.e. fill all vertices with the current color or erase color from all vertices).
 
4. To clear the selection, you can click ``Deselect`` or press :kbd:`Shift+L` or click an empty space in the viewport.

.. image:: _static/images/tut-deselect.png

5. PRO ONLY: You can also use the ``Lasso Selection`` (activated with :kbd:`L` key), ``Rectangle Selection`` or ``Ellipse Selection`` tools to select vertices in an easier and more efficient way than the ``Single Selection`` tool. :kbd:`Shift` and :kbd:`Alt` also work to add to or remove from the selection with these tools.

.. image:: _static/images/tut-lasso.png

.. note::	
    DEVELOPER NOTE: The lasso tool is one of my favorite tools in the addon, even though it's not the main selling point (which is "painting vertices"), but it's one of the most useful tools when dealing with complex scenes and models (alongside ``Vertex Groups``), since it saves so much time by allowing for complex and weirdly shaped selections.

- Paint a simple rock
- Paint base instance vs world instance
- Show banjo kazooie scene before and after
- Paint banjo scene vertex by vertex and start introducing selection tools, select linked, vertex groups, snapshopts, and custom material, paint alpha

Material setup
--------------

Changing view modes
--------------------

Painting vertices
-----------------

Creating and managing color palettes
-----------------------------------

Making selections
-----------------

Painting and changing normals
----------------

Grouping vertices
-----------------

Creating and managing snapshots
-------------------------------

Shortcuts
----------

.. note::
    The majority of actions and tools in Vertex Studio DO NOT HAVE A SHORTCUT. They are available through the main panel or the "Tools and Tool Settings popup" (activated with :kbd:`Ctrl+F` in the 3D viewport).

These are the shortcuts available:

.. list-table::
   :widths: 65 35
   :header-rows: 1

   * - Action
     - Keybinding
   * - **Brush**
     - :kbd:`B`
   * - **Increase brush size**
     - :kbd:`]`
   * - **Decrease brush size**
     - :kbd:`[`
   * - **Cycle swatches and colors**
     - :kbd:`X` (also cycles between Hard and Normal when in "Paint Normals")
   * - **Eraser**
     - :kbd:`Shift+E`
   * - **Tools and Tool Settings popup** (open at the mouse position in the 3D viewport)
     - :kbd:`Ctrl+F`
   * - **Fill** (bucket fill everything or the current selection)
     - :kbd:`G`
   * - **Lasso selection**
     - :kbd:`L`
   * - **Deselect all**
     - :kbd:`Shift+L`

