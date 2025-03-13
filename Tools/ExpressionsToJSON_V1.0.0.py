#Script by Schollidazed for Blender 4.x.x

import bpy 
import json
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, PointerProperty
from bpy.types import Operator

class VIEW3D_PT_ExpressionsToJSON(bpy.types.Panel):
    
    #Decorating the Editor...
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    bl_label = "Batch Convert to JSON"
    bl_category = "ExpressionsToJSON"
    bl_idname = 'PT_ExpressionsToJSON'

    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        
        layout.prop_search(scene, "target", scene, "objects", text="Armature")
        if context.scene.target is not None:
            layout.prop(scene.boneSelection, "EyeBone")
            layout.prop(scene.boneSelection, "MouthBone")
            layout.prop(scene.boneSelection, "MouthSide")
            layout.prop(scene.boneSelection, "LeftBone")
            layout.prop(scene.boneSelection, "RightBone")
            layout.operator("export.some_data")
        elif len(bpy.types.Scene.boneList) != 0:
            bpy.types.Scene.boneList = []

##------BONE ENUMS-----##             
def PickBoneCallback(self, context):
    ob = context.scene.target
    if ob is not None and len(bpy.types.Scene.boneList) == 0:
        i = 0
        for bone in ob.bones:
            print(bone.name)
            bpy.types.Scene.boneList.append( (str(i), bone.name, "", 'BONE_DATA', i) )
            i+=1
    return bpy.types.Scene.boneList
                        
class PickBone(bpy.types.PropertyGroup):
    EyeBone: EnumProperty(
        name= "Eye Expression Bone",
        description= "Find the Eye Expression Bone in the Selected Armature",
        items= PickBoneCallback,
    )

    MouthBone: EnumProperty(
        name="Mouth Expression Bone",
        description="Find the Mouth Expression Bone in the Selected Armature",
        items=PickBoneCallback
    )
    
    LeftBone: EnumProperty(
        name="Left Hand Expression Bone",
        description="Find the Left Hand Expression Bone in the Selected Armature",
        items=PickBoneCallback
    )
    
    RightBone: EnumProperty(
        name="Right Hand Expression Bone",
        description="Find the Right Hand Expression Bone in the Selected Armature",
        items=PickBoneCallback
    )
    
##------File Explorer and Export-----##
def getPropertiesChannels(group):
        ReturnChannels = []
        
        #Separate the Custom Properties from the LocRotScale
        channels = group.channels
        #print(len(channels))
        for channel in channels:
            #print(channel.data_path)
            if not("location" in channel.data_path or"rotation_quaternion" in channel.data_path or "scale" in channel.data_path):
                ReturnChannels.append(channel)
                #print("Property Found, Appended Channel: " + channel.data_path)
        
        return ReturnChannels
    
def WriteJSON(context, filepath):
    armature = context.scene.target
    boneSelection = context.scene.boneSelection
    actionsList = list(bpy.data.actions)
    
    Eye = armature.bones[int(boneSelection.EyeBone)]
    Mouth = armature.bones[int(boneSelection.MouthBone)]
    Left = armature.bones[int(boneSelection.LeftBone)]
    Right = armature.bones[int(boneSelection.RightBone)]
    
    print("Eye.name: " + Eye.name)
    print("Mouth.name: " + Mouth.name)
    print("Left.name: " + Left.name)
    print("Right.name: " + Right.name)
    
    #CREATE A DICTIONARY
    JSON_OUTPUT = {"actions": []}
    
    ActionNumber = 0
    
    for actionInfo in actionsList:
        if 'E-' in actionInfo.name or 'M-' in actionInfo.name or 'H-' in actionInfo.name:
            continue
        
        print(actionInfo.name)
        
        #Append new item to actions list
        JSON_OUTPUT["actions"].append({"name": actionInfo.name, "expressions": []})
        
        #Export Eye first, Mouth, Left Hand, and Right Hand.
        ExpressionNumber = 0
        ExpressionArray = []
        while(ExpressionNumber < 4):
            for group in actionInfo.groups:
                ExpressionName = ""
            
                if (ExpressionNumber == 0):
                    ExpressionName = Eye.name
                elif (ExpressionNumber == 1):
                    ExpressionName = Mouth.name
                elif (ExpressionNumber == 2):
                    ExpressionName = Left.name
                elif (ExpressionNumber == 3):
                    ExpressionName = Right.name
                
                if ExpressionName in group.name:
                    ExpressionArray.append(group)
                    ExpressionNumber += 1
                    break;
        
        #For each keyframed bone...
        for group in ExpressionArray:
            
            print(group.name)
            
            # Find the time/value keyframes, and log the times.
            Channels = getPropertiesChannels(group)
            
            #find the right property, there should only be ONE.
            for channel in Channels:
                
                channelNamePreProcessed = channel.data_path
                channelName = channel.data_path[channel.data_path.find('[') + len(group.name) + 6 : len(channel.data_path) - 2]
                
                #NO WIGGLE.
                if "wiggle" in channelNamePreProcessed or "rotation" in channelNamePreProcessed:
                    continue
                
                print("Channel Name: " + channelName)
                
                TimeKeyframes = []
                ValueKeyframes = []

                for keyframe in channel.keyframe_points:
                    TimeKeyframes.append(keyframe.co.x)
                    ValueKeyframes.append(keyframe.co.y)

                JSON_OUTPUT["actions"][ActionNumber]["expressions"].append({"name": channelName, "TimeKeyframes": TimeKeyframes, "ValueKeyframes": ValueKeyframes})
                
            ExpressionNumber += 1
            
        ActionNumber += 1    
                
                
    with open(filepath, 'w') as file:
        json.dump(JSON_OUTPUT, file)
        
    return {'FINISHED'}

class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Actions"
    
    # ExportHelper mix-in class uses this.
    filename_ext = ".json"
    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        return WriteJSON(context, self.filepath)

##-----END-----##

classes = []

classes.append(VIEW3D_PT_ExpressionsToJSON)
classes.append(ExportSomeData)
classes.append(PickBone)
        
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.target = PointerProperty(type=bpy.types.Armature)
    bpy.types.Scene.boneSelection = PointerProperty(type= PickBone)
    bpy.types.Scene.boneList = []
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.target
    del bpy.types.scene.boneSelection

if __name__ == "__main__":
    register()
    