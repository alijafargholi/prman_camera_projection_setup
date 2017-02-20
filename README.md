# PrMan Projection Setup Tool - v2.0

The use of this tool is to setup the connection between the projection nodes
in Maya.

![ScreenShot](http://alijafargholi.com/wp-content/uploads/2015/11/prman_projection_setup_ui.png)


Setting up a camera projection in RfM has more complications, or at least
more steps than usual workflow. It may cause some frustration for artists
trying to get this to work, so I decided to make a small gui to do make this
connections.

Tested for in Maya 2016 | RenderMan 20 and Maya 2017 RenderMan 21

For more information please [CLICK HERE.](http://alijafargholi.com/2015/11/prman-camera-projection-setup-for-maya/)


Installation
============

1. [Download the Package](https://github.com/alijafargholi/prman_camera_projection_setup/archive/master.zip)
2. Unzip the downloaded file and rename it to **prmanProjectionSetup**.
3. Then move the entire *prmanProjectionSetup*  folder to the specified path:
    * Mac OS X
        * ~/Library/Preferences/Autodesk/maya/scripts
    * Linux
        * /maya/\<version>/scripts
    * Windows
        * \<drive>:\Documents and Settings\\\<username>\\My Documents\\maya\\scripts

4. Then in a new instance of Maya, open the script editor and run the following
 in a *Python* tab:

    ```python
    from prmanProjectionSetup import cam_proj_setup_ui
    reload(cam_proj_setup_ui)
    cam_proj_setup_ui.create_ui()
    ```

> Note:
>> Probably you don't want to run the script from the python tab
every time you wan to open the tool, you could drag and drop the code from the *python* tab to a *shell*