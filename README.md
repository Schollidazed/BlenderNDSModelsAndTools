<br/>
<div align="center">
<a href="https://github.com/ShaanCoding/ReadME-Generator">
<img src="https://avatars.githubusercontent.com/u/61301337?v=4" alt="Logo" width="80" height="80">
</a>
<h3 align="center">Schollidazed's Blender Models and Tools</h3>
<p align="center">
Low-Spec 3D Models with a bit of a High-Tech Edge.


  


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
    + [IK + FK Switch](#ik--fk-switch)
    + [Wiggle Bones](#wiggle-bones)
  * [Tool Tutorial](#tool-tutorial)
- [Roadmap](#roadmap)
- [License](#license)
 
 # Contact

#### Creator: Schollidazed (Formerly Known As ChickenWingJohnny)

###### Characters Created and Owned by SegaSammy Holdings Inc. and Sonic Team.

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
- Have Blender 4.0 or Higher installed, the models won't load otherwise.
- ***Credit me!*** While I didn't make these models, I put time and effort into making additional textures and the rigs. You can do this by either tagging me, and/or linking people back to this repo.
- Uhhhh be really cool I guess? (Which if you're reading this, you are btw, keep it up! :D) 
 ## Usage

You can use this for whatever project you'd want! Fangame, animation, whatever! My only request is that you credit me, and link back to here. Some of my various platforms are listed at the end of this ReadMe and my profile, do take a look!

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

#### IK + FK Switch

Another cool feature of note is the IK/FK switch for each limb. You'll see a cross and inside it's custom properties, it should have a toggle for IK. Flip it for position based control. Unfortunately, I've yet to figure out position tracking for easy transitions between kinematics. *Remember that custom property keyframing still applies here.*

#### Wiggle Bones
The Quills and Ears all have wiggle bones by default for easy motion tracking. It uses the very popular [Wiggle2 Addon](https://github.com/shteeve3d/blender-wiggle-2), which I'd reccomend reading up on before utilizing. It requires movement in the timeline in order to work, and you can bake the physics into the animation from there.

### Tool Tutorial
![ToolTutorial](https://drive.google.com/uc?export=view&id=1Volnm17njD8-wRayh3cayzg0D3OltkkL)

Now the HUGE tool that I've written specifically for blender is for exporting the expressions for actions that you make inside a blend file into a universal format: JSON! You can then utilize these wherever you decide to implement the main "armature" animations. We used these EXTENSIVELY for Rush 3D, though I'd love to see where YOU decide to utilize them.

Now to open it in blender, you first need to navigate to the scripts workspace shown above, click "open", and navigate to the ExpressionsToJSON python file. It should import like so. Then, click the run script button, and you'll get a pop up in your main blender workspace:

![ToolTutorial2](https://drive.google.com/uc?export=view&id=16EQFGnSIAc-TS2z0W5aFVof15fELqmDT)

***TA-DAA!!*** *Easy to navigate Blender UI!!*

Now all you need to do is link the armature you'd like to export, select the corresponding bones, and click export actions. This should bring up a file directory where you can navigate where you'd like to save the JSON, and what you'd like to call it. Click save, and it'll automatically parse your blender file for actions you've made, and extract those animations. Easy as that!

If you'd like to sort them by name, there's another helper script for that, although you'll need some form of python to run it. Just run the python script by itself, and you can navigate to the proper json file, and it'll sort your actions for you.

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
- [ ] Shadow the Hedgehog
- [ ] Amy Rose
- [ ] Knuckles the Echidna
- [ ] Vanilla the Rabbit
- [ ] Chocola the Chao
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
