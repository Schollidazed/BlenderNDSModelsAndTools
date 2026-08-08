<br/>
<div align="center">
<a href="https://github.com/ShaanCoding/ReadME-Generator">
<img src="https://avatars.githubusercontent.com/u/61301337?v=4" alt="Logo" width="80" height="80">
</a>
<h3 align="center">Schollidazed's Blender Models and Tools</h3>
<p align="center">
Low-Spec 3D Models, with all the fun and whimsy in the world embedded into them.


  


</p>
</div>

# Table of Contents

- [Contact](#contact)
- [About This Page](#about-this-page)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
- [Usage](#usage)
  * [Blender Tutorial](#blender-tutorial)
    + [Custom Properties and Expressions](#custom-properties-and-expressions)
    + [Pose Library](#pose-library)
    + [Creating Your Own Expressions](#creating-your-own-expressions)
    + [IK + FK Switch](#ik--fk-switch)
    + [Wiggle Bones](#wiggle-bones)
  * [Tool Tutorial](#tool-tutorial)
    + [Expressions to JSON](#expressions-to-json)
    + [Atlas Creator](#altas-creator)
- [Roadmap](#roadmap)
- [License](#license)
 
 # Contact

#### Creator: Schollidazed (Formerly Known As ChickenWingJohnny)

###### Sonic Characters Created and Owned by SegaSammy Holdings Inc. and Sonic Team.
###### Deltarune Characters Created and Owned by Toby Fox

###### NOTE: Sonic, Super Sonic, Blaze, and Tails 3D models were all originally made by Sonic Team for 2007's Sonic Rush Adventure. They have been slightly modified by me (texture work/animation-ready rigging). All other characters in this repository have been modeled by yours truly :D


Newgrounds - [@Schollidazed](https://schollidazed.newgrounds.com/)

Twitter/X - [@Schollidazed](https://twitter.com/Schollidazed)

Youtube - [@Schollidazed](https://www.youtube.com/@Schollidazed)

Project Link - https://github.com/Schollidazed/BlenderNDSModelsAndTools

 # About This Page

![Example Render](https://drive.google.com/uc?export=view&id=1ETYov5OI15nmrHiku7zq2ck14905W2Hf)

So you wanna check out these models? You may have seen them used in many of my/others projects, such as the fan game **Sonic Rush 3D** and some animations of mine/others on the world wide web. Awesome! Just go ahead, download the repo, and import them to get started. However, before doing that, I'd recommend taking a look through this ReadMe. It's short, concise, organized, and will only take 5 minutes of your time. 

Trust me, **it will save you time!** 

 ## Getting Started

As I said earlier, just download the source code, and you'll be more than set. However, please take note of these few things...
 ### Prerequisites

In order to utilize these models, you'll need to:
- Have Blender 4.0 or Higher installed, the models may not load otherwise. (I usually use the latest version to keep up to date, give me a shout if these break blender for you!!)
- ***Credit me!*** While I didn't make some of these models, I put time and effort into making additional textures and the rigs. You can tag me, and/or link people back to this repo so that more people can create cool things! Tagging me will also get me to see what my models are being used for, and see all the amazing stuff you make.
- Uhhhh be really cool I guess? (Which if you've read this far, you are btw. Keep it up! :D) 
 ## Usage

You can use this for whatever project you'd want! Fangame, animation, whatever! My only request is that you drop my @, and link back to here. Some of my various platforms are listed at the end of this ReadMe and my profile, do take a look!

When it comes to things I don't want them used for, no NSFW or hate. I don't want these models and myself to be affiliated with those. 

### Blender Tutorial

The way these models work are really cool and the part of my methods that I used, particularly of the facial rig, was taught to me by the amazing [@TheSicklyWizard](https://www.youtube.com/@TheSicklyWizard) on Youtube. He's been making some FANTASTIC content over there, and I highly recommend his tutorials when it comes to his rigging series.

![image](https://drive.google.com/uc?export=view&id=1GqjYl8SGP-SSQ6mFBwj7ZNJyEilEOq5R)

#### Custom Properties and Expressions

Let's take a deep dive into this screenshot here. On the right of the viewport, underneath the model LocRotScale info is the elusive **Custom Properties** channel... *oooOOOoooOooOooOoo*

You have nothing to be afraid of though! Click on one of the expression bones above sonic, and changing his expression is as simple as changing the number on the right. But that's if you want a more direct approach. for a more intuitive approach, you can use the **Pose Library**.

#### Pose Library

Shift your attention to the bottom of the viewport, and you're met with all the possible expressions the character can pull off. In order to apply one, you'll need first be in pose mode and make sure no bones are highlighted beforehand. Just click on any expression you want to apply it. 

***NOTE THAT, in order to keyframe expressions for animation, you MUST have the EXRESSIONS Bone Group enabled, and make sure include the custom properties while keyframing.***

Pretty cool huh?

#### Creating Your Own Expressions

Most of my models now use a texture atlas that respective UVs scroll through to change the facial expression. This is far more performance efficent than housing every texture separately, which is what I did before.

History lesson aside, creating your own textures may require a more in-depth explanation on how the system works, let's dive in!

![ShaderDiagram](https://drive.google.com/uc?export=view&id=1ZWwv_uQoorkhJ-o_UxPudG-gAxKteQ6l)

Focus your attention on the bottom of the screenshot shown above. On the left is the texture atlas that is currently being used in the shader, in this case the eyes. The node graph in the center is the brains of the shader. Data flows left to right here, we first get the UV Map of the model that is calling the material, in this case polygons on the sonic model that are assigned the material, which then is manipulated by the UV Altas Driver. The size of the UVs is controlled by setting the rows/columns, and the position is controlled by the index, moving left to right, and jumping down to the row below once it reaches out of room. It is indexed from 0, meaning that the first row on the texture altas on the left consist of indicies 0-2. 0 being the normal eyes, 1 being the angry eyes, and 2 being the panicked eyes. **This index cannot be directly set in the shader, I've connected this value to the respective bone controller.** This is why I initially directed you to the bone first! That bone is the one that DRIVES this whole expression changing shabang.

Now if it feels like I'm over-explaining things there, I kind of am, but I just want to make sure we're all on the same page.

Every model's expressions were originally UV Mapped with one texture, this is a holdover from my original way of texturing, hence the small history lesson at the start of the section. This holdover, however, can make it easier for you if you want to create your own texture on its own image. If you want to turn off the atlas and focus on a single texture, you can do that by disconnecting the UV atlas driver, and replacing the image in the orange node in the middle with your own.

Alternitively, if you want to draw on the atlas, you're completely free to do so. Just know that 

  a) All textures have been packed into the file. In order to change them, first unpack them, and then change the png accordingly
  
  b) Each expression is the same width and the same height, so just divide the width by the number of columns, and the height by the number of rows, and you should get the exact dimension of space that your texture should take up.
  
  or just eyeball it, that's valid.

Now that you've added your expression(s) to the atlas, and have adjusted the dimensions of the UV Driver accordingly, you now may realize that when you try to increase the expression number on the bone, you arbitrarly hit a the number of original expressions placed (for sonic, that's 7 for his eyes).

That's on purpose, **I've set a minimum/maximium index so that unintended effects don't happen**, but you can alter this quite easily.

![BoneControl](https://drive.google.com/uc?export=view&id=1QWgC8UHEjxc8E99ucXyrx62yc47UEwxC)

First go into pose-mode, then click on the expressionbone which you want to change the limits for.

Then go into the properties tab on the bottom right, click on the bone icon, and scroll allllll the way down to the custom properties tab. You should see the respective control variable there. 

All that's left is to click the gear, and change the maximum to the new number, or just get rid of it entirely by increasing it to 999, or whatever large number you can think of.

That should be it for expressions! Please contact me, or drop an issue if you have any questions or come across any problems.

#### IK + FK Switch

Another cool feature of note is the IK/FK switch for each limb. Set out from the character's joints (knee or elbow), you'll see a cross. Clicking inside, and looking at the custom properties on the right, there should have a toggle for IK. Flip it for position based control of feet, hands, or whatever i've applied it to. Unfortunately, I've yet to figure out position tracking for easy transitions between kinematics. *Remember that custom property keyframing still applies here.*

#### Wiggle Bones
Quills, Ears, and some clothing have wiggle bones for easy physics! It uses the popular [Wiggle2 Addon](https://github.com/shteeve3d/blender-wiggle-2), which I'd reccomend reading up on and installing as a part of your regular animation pipeline. It requires timeline to be actively playing in order for it to work. You can bake the physics into the animation from there.

### Tool Tutorial

I've included some blender scripts that I've created that you might find useful! These directly interface with the Blender API to do certain things. If you want to learn how to run these scripts, see the below section on Expressions to JSON.

#### Expressions to JSON
![ToolTutorial](https://drive.google.com/uc?export=view&id=1Volnm17njD8-wRayh3cayzg0D3OltkkL)

Now the HUGE tool that I've written specifically for blender is for exporting the expressions for actions that you make inside a blend file into a universal format: JSON! You can then utilize these wherever you decide to implement the main "armature" animations in a different application, like Unity. We used these EXTENSIVELY for Rush 3D, though I'd love to see where YOU decide to utilize them.

Now to open it in blender, you first need to navigate to the scripts workspace shown above, click "open", and navigate to the ExpressionsToJSON python file. It should import like so. Then, click the run script button, and you'll get a pop up in your main blender workspace:

![ToolTutorial2](https://drive.google.com/uc?export=view&id=16EQFGnSIAc-TS2z0W5aFVof15fELqmDT)

***TA-DAA!!*** *Easy to navigate Blender UI!!*

Now all you need to do is link the armature you'd like to export, select the corresponding bones, and click export actions. This should bring up a file directory where you can navigate where you'd like to save the JSON, and what you'd like to call it. Click save, and it'll automatically parse your blender file for actions you've made, and extract those animations. Easy as that!

If you'd like to sort them by name, there's another helper script for that, although you'll need some form of python to run it. Just run the python script by itself, and you can navigate to the proper json file, and it'll sort your actions for you.

The JSON itself is fairly easy to dig into, and can be easily unpacked into your other application if it has some sort of scripting interface. 

#### Altas Creator

I made this when transitioning to the altas system, and I figure it might be useful to other people as well.

Much like the previous one, open it in the scripting tab in Blender, and click run. Go over to the texture editor, open the properties tab on the right of the texture viewport, and it should have it's own dedicated tab.

![AtlasTutorial](https://drive.google.com/uc?export=view&id=1vB7xeW4Fg4Pv_OOsZQOERSxzIbfjyEih)

There you can manually select how many rows and columns you want, add pictures to it, mirror those pictures, rename them for organization, move them around, sort them aphabetically, what have you. 

My favorite feature is the alternate add button, which adds the current selection, and moves the current selection down by one. If you've named your separate texture files with a common dilineator (e_bsc, e_pnc, e_rit, etc,), this button can be spammed to add all of them at once.

**Keep in mind that this only works with textures imported to blender, you can't give files/filepaths to it directly**

Once you click *Create Texture Atlas*, it will go from the top of your list to the bottom, placing them row by row, from left to right, such that index 0 is your first texture, index 1 is your 2nd, etc. 

 ## Roadmap

Not in any specific order...
- [X] Sonic the Hedgehog
- [X] Blaze the Cat
- [X] Tails the Fox
- [ ] Eggman
- [ ] Eggman Nega
- [X] Cream the Rabbit
- [ ] Chao/Cheese the Chao
- [X] Super Sonic
- [ ] Burning Blaze
- [X] Shadow the Hedgehog
- [ ] Amy Rose
- [ ] Knuckles the Echidna
- [ ] Vanilla the Rabbit
- [ ] Chocola the Chao
- [ ] Marine the Racoon
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
