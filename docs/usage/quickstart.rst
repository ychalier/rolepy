Quickstart
==========

Settings
--------

Inside the root folder of the repository, create a file ``settings.txt``. You
may leave it blank for now, but you can specify settings with the following format:

.. code-block::

    # Window size in pixels
    # resolution=928*544
    resolution=928*544

    # FPS cap (leave empty for unlimited)
    # max_fps=144
    max_fps=

    # Time between two touchdown events
    # key_repeat_delay=10
    key_repeat_delay=10

Lines starting with a dash are ignored.

Start
-----

Start the main script ``role.py`` with the following command:

.. code-block:: bash

    python role.py
