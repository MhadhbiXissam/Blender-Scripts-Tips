import bpy

# Create a custom toolbar
class CustomToolBar(bpy.types.Panel):
    """Custom Toolbar"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Tools"  # not visible
    bl_options = {'HIDE_HEADER','HEADER_LAYOUT_EXPAND'}

    
    def draw(self, context):
        layout = self.layout
        
        # Create a scrollable layout
        scrollable_layout = layout.column()
        
        scrollable_layout.template_ID(context.space_data, "pin_id", new="outliner.datablock_new", unlink="outliner.datablock_delete")
        scrollable_layout.emboss ='NORMAL'
        # Add buttons to the scrollable layout
        for i in range(50):
            box = scrollable_layout.column()
            box.scale_x = 2
            box.scale_y = 2
            box.ui_units_x = 2
            box.ui_units_y = 2
            box.operator("mesh.primitive_cube_add", text= "", icon='OUTLINER_DATA_META' , )



        print(dir(layout),file =open("/home/issam/Documents/blenders_apps/dir.txt","w"))

# Register the custom toolbar
def register():
    bpy.utils.register_class(CustomToolBar)

# Unregister the custom toolbar
def unregister():
    bpy.utils.unregister_class(CustomToolBar)

# Check if this script is being run as the main file
if __name__ == "__main__":
    register()

