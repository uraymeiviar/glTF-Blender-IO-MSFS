[![MSFS](misc/Logos/msfs_logo.png)](https://www.flightsimulator.com/)[![ASOBO](misc/Logos/asobo_logo.png)](https://www.asobostudio.com/) <img src="misc/Logos/glTF_logo.png" width="180" height="90">

# Microsoft Flight Simulator glTF 2.0 Importer and Exporter for Blender

This repository contains the current version of the official Microsoft Flight Simulator Blender Import/Export plugin. The flight sim community has already developed and forked the original project many times, and Asobo's intention is to fully support Blender with the help and contributions of all the developers that have already implemented features in the different unofficial Blender plugins.

>Asobo would especially like to thank the following people: <br>
>Vitus of [Wing42](https://wing42.com/), [tml1024](https://github.com/tml1024), [ronh991](https://github.com/ronh991), [pepperoni505](https://github.com/pepperoni505) of [FlyByWire](https://flybywiresim.com/)

:warning: This plugin cannot import glTF files that have been built into a Microsoft Flight Simulator package through the Sim's Package Builder.
<br>
:warning: This plugin is NOT compatible with the legacy exporter developed for FSX and P3D and MSFS.  Remove these plugin (Prefered) or disabled these plugins.
<br>
:warning: The version 1.3.x is only compatible with Blender 3.3.x LTS. Other versions are not supported.

*******

# Summary
- [How to Install the Add-on](#how-to-install-the-add-on)
  - [How to Install the ASOBO Blender MSFS Importer/Exporter using Blender:](#how-to-install-the-asobo-blender-msfs-importerexporter-using-blender)
  - [How to Install the ASOBO Blender msfs exporter by Copy/Paste to AppData](#how-to-install-the-asobo-blender-msfs-exporter-by-copypaste-to-appdata)
- [How to remove the Add-on](#how-to-remove-the-add-on)
- [Migration of Legacy Blend File Material Types/Modes](#migration-of-legacy-blend-file-material-typesmodes)
  - [Steps For Migration](#steps-for-migration)
- [Documentation](#documentation)
- [Notes On Shadertree](#notes-on-shadertree)

*******

# How to Install the Add-on

There are two ways to install the MSFS Blender exporter. Either using the Edit Preferences Menu and Install tab, or copy/paste the addon files to your %APPDATA% folder. Installation steps are explained down bellow :

## How to Install the ASOBO Blender MSFS Importer/Exporter using Blender:

1. Go to the Releases section of the https://github.com/AsoboStudio/glTF-Blender-IO-MSFS repository. Then download the zip file `io_scene_gltf2_msfs.zip`.

![Download Release](misc/Install/Download_rel.png)

2. Open Blender and go to : Edit > Preferences.

![Edit Preferences - Add](misc/Install/Edit_Pref.png)

3. Go to Add-ons and click on Install an add-on. This will bring up a file dialog, where you navigate to the folder where you have your `io_scene_gltf2_msfs.zip` downloaded file.

4. Select the `io_scene_gltf2_msfs.zip` file.  And click on the Install Add-on button.

![Edit Preferences - Install](misc/Install/Edit_Pref_install.png)

5. Enable the Add-on by clicking on the checkbox.

![Edit Preferences - Enable](misc/Install/Enable_checkbox_addon.png)

<br>

## How to Install the ASOBO Blender msfs exporter by Copy/Paste to AppData

1. Close Blender if you have it open.
2. Go to the Releases section of the https://github.com/AsoboStudio/glTF-Blender-IO-MSFS repository. Then download the zip file `io_scene_gltf2_msfs.zip`
3. Decompress the contents of the file to a temporary location.
4. Select the `io_scene_gltf2_msfs` folder then copy it to the clipboard (Ctrl + "C").
5. Now browse to the Blender `addons` folder, which - by default - can be found in the following locations:
   - **Windows**: This will usually be in `%AppData%\Blender Foundation\Blender\<blender-version>\scripts\addons\`.
   - **Mac OS X**: This will be in your Library (Press the *Option* key when in Finder's `Go` menu to open your Library folder): `\Users\<username>\Library\Application Support\Blender\<blender-version>\scripts\addons\`.
6. Paste the `io_scene_gltf2_msfs` into the Blender `addons` folder (Ctrl + V).

After completing the process outlined above, you will need to start Blender and then activate the plugin. Activation is done from Edit > Preferences, as shown in the image below:

**NOTE** : You may need to restart Blender again after activating the plugin for all the options to be visible in the IDE.

![Edit Preferences - Enable](misc/Install/Enable_checkbox_addon.png)

# How to remove the Add-on

1. If you previously installed the Microsoft Flight Simulator glTF Extensions Add-on, Remove/Delete the older version using the Blender Edit > Preferences Menu. 

![Edit Preferences](misc/Install/Edit_Pref.png)


2. Select the Add-ons tab. Search for the `Microsoft Flight Simulator glTF Extension` Importer/Exporter add-on in the search box. Delete the `Import-Export: Microsoft Flight Simulator gltf Extension` using the `Remove` button.<br>  
:warning: DO NOT DELETE THE `Import-Export: gltf 2.0 format` Add-on.

![Search Remove](misc/Install/Edit_Pref_search_rem.png)

3. You should now have only the `Import-Export: gltf 2.0 format` addon left.
4. Close the Blender program.


# Migration of Legacy Blend File Material Types/Modes

This Blender addon is now the officially supported addon for Microsoft Flight Simulator, and as such, blend files that were made using any other version/iteration of the addon are now considred *legacy* blend files. Basically, legacy blend files had the extensions that are used to create glTF 2.0 files for use in the Microsoft Flight Simulator hard-coded into them. However, the ASOBO version of the exporter uses the Khronos default code and adds hooks to this code for the ASOBO extensions used in the glTF files.

The ASOBO exporter also has a much more complex and versitile material node structure that can be seen in the Shader Tab/Window in Blender. Your legacy Flight Simulator Material mode/types should be migrated to the new ASOBO Microsoft Flight SImulator material mode/types with the click of the "**`Migrate Material Data`**" button
in the MSFS Material Parameters panel (under the Blender Material Properties). 

We have made every effort possible to ensure that legacy blend files can be easily and fully migrated to use this addon and exporter, and we recommend the migration to use this addon as soon as possible to ensure future compatibility as this addon evolves and is updated. 

Once you have performed a migration, you should look at the shader nodes in your *original* blend file and make sure the BSDF node paramerters are the same as the panel values.  This is an important check to make as these can get out of sync when you modify the parameters in the `Surface` section of the `Material Properties` panel instead of modifying them in the `MSFS Material Parameters` section. In particular, pay attention to the *Metallic* and *Roughness* Scale and Factor values.

<br>

## Steps For Migration

1. Open your blend file.
2. Select a node/mesh
3. Open the `MSFS Material Params` Panel in the Material Properties
    - You will see a `Migrate Material Data` button above the MSFS Material Params type drop down list.
    - **DO NOT Select a MSFS Material from the drop down**, this will erase the existing legacy data and you will lose all your material settings.
4. Click on the "Migrate Material Data" button
    - Your existing legacy material type/mode will be conoverted to the new ASOBO MSFS material type shader node structure.

Figure 1 Before migration

![Before](misc/MaterialMigration/BeforeMigration.png)

Figure 2 After Migration

![After](misc/MaterialMigration/AfterMigration.png)

All the settings from the legacy node structure are copied to the ASOBO exporter shader node structure. As you can see from the images above, the ASOBO node structure is more complex and there are a lot more nodes. Sometimes some model developers have made changes to the legacy BSDF node that are *not* reflected in the `MSFS Material Params` panel data - the variables that are migrated come instead from the *legacy* panel data, so there may be situations where your material will not look correct. This means that you will need to compare your legacy blend file materials to the new blend file Materials after migration to see if there are any issues like this one. You can do this by openeing another Blender instance and opening the legacy file in that, then comparing the MSFS Material Params panel values with the legacy parameter values and adjusting them accordingly.

Note that each Microsoft Flight Simulator material will need to be migrated, but any mesh/nodes associated to that material will also have it's MSFS Material Parameters migrated. 

Finally, you may also notice that some MSFS Material Parameters show data but *cannot* be adjusted. This is in keeping with the ASOBO 3DS Max exporter material parameters.  Please raise an issue if this is not to your requirements.

## WARNING
After migration SAVE YOUR FILE AS A NEW FILE and keep your legacy blend file for future reference.

# Documentation
If you want to learn how to use this add-on you can refer to the documentation page here :
[Documentation for Microsoft Flight Simulator glTF 2.0 Importer and Exporter for Blender](./Documentation/Documentation.md)

You can also have a look at the SDK documentation of the plugin here : https://docs.flightsimulator.com/html/Asset_Creation/Blender_Plugin/The_Blender_Plugin.htm

# Notes On Shadertree

Shadertree modification directly impacts the result of the exporter. 
The properties of your material must only be modified through the `MSFS Material Panel` section.

:warning: If you work with an MSFS Material you should never modify the shader tree manually.



