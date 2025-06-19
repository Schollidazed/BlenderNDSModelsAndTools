#Script by Schollidazed for Blender 4.x.x

bl_info = {
    "name": "Texture Atlas Creator",
    "blender": (3, 0, 0),
    "category": "Image",
}

import bpy
import math
from bpy.props import IntProperty, CollectionProperty, PointerProperty, EnumProperty, StringProperty, BoolProperty
from bpy.types import Operator, Panel, PropertyGroup, UIList


# Property Group for each image
class AtlasImageItem(PropertyGroup):
    image: bpy.props.PointerProperty(type=bpy.types.Image)
    name: StringProperty(name="Entry Name")  # Display label
    mirror: BoolProperty(name="Mirror", description="Is this image mirrored?", default=False)


# Property group for all settings
class AtlasProperties(PropertyGroup):
    min_rows: IntProperty(name="Min Rows", default=1, min=1)
    min_columns: IntProperty(name="Min Columns", default=1, min=1)
    image_list: CollectionProperty(type=AtlasImageItem)
    active_index: IntProperty(name="Active Index", default=0)
    image_to_add: EnumProperty(
        name="Available Images",
        description="Select an image to add to the atlas",
        items=lambda self, context: [(img.name, img.name, "") for img in bpy.data.images]
    )


def update_grid_size(atlas_props):
    """Auto-update the grid size based on the list length."""
    count = len(atlas_props.image_list)
    atlas_props.min_columns = max(1, math.ceil(math.sqrt(count)))
    atlas_props.min_rows = max(1, math.ceil(count / atlas_props.min_columns))


# Operator to sort alphabetically
class TEXTURE_OT_SortImageList(Operator):
    bl_idname = "texture.sort_image_list"
    bl_label = "Sort Alphabetically"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        sorted_items = sorted(atlas_props.image_list, key=lambda item: item.name.lower())

        name_list = [item.name for item in sorted_items]
        mirror_list = [item.mirror for item in sorted_items]
        image_list = [item.image for item in sorted_items]

        atlas_props.image_list.clear()

        for i in range(len(sorted_items)):
            new_item = atlas_props.image_list.add()
            new_item.name = name_list[i]
            new_item.mirror = mirror_list[i]
            new_item.image = image_list[i]

        self.report({'INFO'}, "List Sorted Alphabetically.")
        return {'FINISHED'}
    
class TEXTURE_OT_MoveImageUp(Operator):
    bl_idname = "texture.move_image_up"
    bl_label = "Move Image Up"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        idx = atlas_props.active_index

        if idx > 0:
            atlas_props.image_list.move(idx, idx - 1)
            atlas_props.active_index -= 1

        return {'FINISHED'}

class TEXTURE_OT_MoveImageDown(Operator):
    bl_idname = "texture.move_image_down"
    bl_label = "Move Image Down"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        idx = atlas_props.active_index

        if idx < len(atlas_props.image_list) - 1:
            atlas_props.image_list.move(idx, idx + 1)
            atlas_props.active_index += 1

        return {'FINISHED'}


# Operator to add image from dropdown
class TEXTURE_OT_AddImage(Operator):
    bl_idname = "texture.add_image_to_atlas"
    bl_label = "Add Image to Atlas"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        image_name = atlas_props.image_to_add
        image = bpy.data.images.get(image_name)

        if image and not any(item.image == image for item in atlas_props.image_list):
            new_item = atlas_props.image_list.add()
            new_item.image = image
            new_item.name = image_name
            new_item.mirror = False
            update_grid_size(atlas_props)

        return {'FINISHED'}


# Operator to remove image
class TEXTURE_OT_RemoveImage(Operator):
    bl_idname = "texture.remove_image_from_atlas"
    bl_label = "Remove Image from Atlas"

    def execute(self, context):
        atlas_props = context.scene.atlas_props

        if len(atlas_props.image_list) > 0:
            atlas_props.image_list.remove(atlas_props.active_index)
            atlas_props.active_index = max(0, atlas_props.active_index - 1)
            update_grid_size(atlas_props)

        return {'FINISHED'}


# Operator to add mirrored image with prompt
class TEXTURE_OT_AddMirroredImage(Operator):
    bl_idname = "texture.add_mirrored_image_to_atlas"
    bl_label = "Add Mirrored Image"

    index: IntProperty()
    new_name: StringProperty(name="Mirror Entry Name")

    def invoke(self, context, event):
        source_item = context.scene.atlas_props.image_list[self.index]
        self.new_name = f"{source_item.name}_mirror"
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        source_item = atlas_props.image_list[self.index]

        new_item = atlas_props.image_list.add()
        new_item.image = source_item.image  # Store direct reference
        new_item.name = self.new_name
        new_item.mirror = True

        update_grid_size(atlas_props)

        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "new_name")


# Operator to add next image alphabetically
class TEXTURE_OT_AddNextAlphabeticalImage(Operator):
    bl_idname = "texture.add_next_alphabetical_image"
    bl_label = "Add, Go Down One"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        current_image_name = atlas_props.image_to_add

        # Build sorted image list
        sorted_images = sorted([img.name for img in bpy.data.images])
        try:
            current_index = sorted_images.index(current_image_name)
        except ValueError:
            self.report({'ERROR'}, "Current image not found in image list.")
            return {'CANCELLED'}

        # Add the currently selected image
        if not any(item.image and item.image.name == current_image_name for item in atlas_props.image_list):
            image = bpy.data.images.get(current_image_name)
            if image:
                new_item = atlas_props.image_list.add()
                new_item.image = image
                new_item.name = current_image_name
                new_item.mirror = False
                update_grid_size(atlas_props)

        # Advance dropdown to the next image in list
        if current_index + 1 < len(sorted_images):
            atlas_props.image_to_add = sorted_images[current_index + 1]
        else:
            self.report({'INFO'}, "Reached end of image list!")

        return {'FINISHED'}


# Operator to create the atlas
class TEXTURE_OT_CreateAtlas(Operator):
    bl_idname = "texture.create_atlas"
    bl_label = "Create Texture Atlas"
    bl_description = "Creates a texture atlas from selected images"

    def execute(self, context):
        atlas_props = context.scene.atlas_props
        images = []

        for item in atlas_props.image_list:
            if item.image:
                images.append((item.image, item.mirror))

        if len(images) == 0:
            self.report({'ERROR'}, "No images selected for atlas.")
            return {'CANCELLED'}

        img_width, img_height = images[0][0].size
        columns = max(atlas_props.min_columns, math.ceil(math.sqrt(len(images))))
        rows = max(atlas_props.min_rows, math.ceil(len(images) / columns))

        atlas_width = columns * img_width
        atlas_height = rows * img_height

        atlas_image = bpy.data.images.new("TextureAtlas", width=atlas_width, height=atlas_height)
        pixels = [0.0] * (4 * atlas_width * atlas_height)

        for idx, (img, mirror) in enumerate(images):
            img.pixels[:]  # Ensure image is loaded
            x_offset = (idx % columns) * img_width
            y_offset = atlas_height - ((idx // columns) + 1) * img_height

            for y in range(img_height):
                for x in range(img_width):
                    src_x = img_width - 1 - x if mirror else x
                    src_idx = 4 * (y * img_width + src_x)

                    dst_x = x_offset + x
                    dst_y = y_offset + y
                    dst_idx = 4 * (dst_y * atlas_width + dst_x)

                    pixels[dst_idx:dst_idx + 4] = img.pixels[src_idx:src_idx + 4]

        atlas_image.pixels = pixels
        atlas_image.update()

        for area in context.screen.areas:
            if area.type == 'IMAGE_EDITOR':
                area.spaces.active.image = atlas_image
                break

        self.report({'INFO'}, "Texture Atlas Created Successfully!")
        return {'FINISHED'}


# UIList to display the image list (supports drag and drop)
class TEXTURE_UL_ImageList(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row(align=True)
        row.label(text=item.name, icon='IMAGE_DATA')

        if not item.mirror:
            op = row.operator("texture.add_mirrored_image_to_atlas", text="Mirror", icon='ARROW_LEFTRIGHT')
            op.index = index


# UI Panel
class TEXTURE_PT_AtlasPanel(Panel):
    bl_label = "Texture Atlas Creator"
    bl_idname = "TEXTURE_PT_atlas_panel"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Texture Atlas'

    def draw(self, context):
        layout = self.layout
        atlas_props = context.scene.atlas_props

        layout.prop(atlas_props, "min_rows")
        layout.prop(atlas_props, "min_columns")

        layout.prop(atlas_props, "image_to_add")
        row = layout.row(align=True)
        row.operator("texture.add_image_to_atlas", icon='ADD')
        row.operator("texture.add_next_alphabetical_image", icon='SORTALPHA')

        layout.label(text="Images in Atlas:")

        row = layout.row()
        row.template_list("TEXTURE_UL_ImageList", "", atlas_props, "image_list", atlas_props, "active_index", rows=6)

        col = row.column(align=True)
        col.operator("texture.remove_image_from_atlas", icon='X', text="")
        col.separator()
        col.operator("texture.move_image_up", icon='TRIA_UP', text="")
        col.operator("texture.move_image_down", icon='TRIA_DOWN', text="")

        layout.operator("texture.sort_image_list", icon='SORTALPHA')

        layout.separator()
        layout.operator("texture.create_atlas", icon='IMAGE_DATA')



# Register
classes = [
    AtlasImageItem,
    AtlasProperties,
    TEXTURE_OT_AddImage,
    TEXTURE_OT_RemoveImage,
    TEXTURE_OT_AddMirroredImage,
    TEXTURE_OT_AddNextAlphabeticalImage,
    TEXTURE_OT_SortImageList,
    TEXTURE_OT_MoveImageUp,
    TEXTURE_OT_MoveImageDown,
    TEXTURE_OT_CreateAtlas,
    TEXTURE_UL_ImageList,
    TEXTURE_PT_AtlasPanel
]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.atlas_props = PointerProperty(type=AtlasProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.atlas_props


if __name__ == "__main__":
    register()
