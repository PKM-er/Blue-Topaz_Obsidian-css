# TIPS  

***Special parts for fun in this theme***

## Emphases

*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__
***To combine***
___To combine___

## Special tags

#dailynote
#weeklynote
#important
#重要
#inprogress
#进行中
#complete
#完成
#questions
#ideas

You can also create your own special tags by creating a css snippet like

```css
.tag[href^="#xxxxx"] {
  background-color: blue !important;
  font-weight: 600;
  font-family: var(--font-family-special-tag);
}
```

```note-imp
xxxxx: your tag
your can also use your favorite color to replace "blue" above
```

---

## Images
### To modify the position of images

***Usage***

Typing "|left" or "|right" at the end of the image file can make the image shown on left or right.
For example,
xxx.jpg|left

---------------------------
The variants you can use：
left/Left/LEFT/L
right/Right/RIGHT/R

e.g. xxx.png|L

You can also change the image size with the position. You should put the "|number" at the end.
For example,
xxx.png|right|200 

![[obsidian_image.png|100]]

![[obsidian_image.png|left|150]]

![[obsidian_image.png|R|200]]

---

Use "inlineL", "inlineR" or "inline" to embed the image on the left, right or arbitray.
xxx.png|inlineL

blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah ![[obsidian_image.png|inlR|200]]blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 

The variants you can use：
inlineL/InlineL/INLINEL/inlL
inlineR/InlineR/INLINER/inlR
inline/Inline/INLINE/inl

e.g. xxx.png|inlL

 blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah ![[obsidian_image.png|inl|200]]blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 

-----------------------------

### image-captions
 *modified from Discordian by @radekkozak*

***Usage***

1. Add the following cssclass directive in YAML

```yaml
---
cssclass: img-captions
---
```

Click here to find the demostration [[Image-captions]]

2. Then the syntax is like:
`![[xxx.png#position|captions|size]]`
position: left/right
captions: your captions

---

### image-grid 
*adapted from Discordian by @radekkozak and orange by @echoxu*

***Usage***

**To use image-grid, do not recommend using pipe for images**

**Method 1**
To add "|+grid" after the image name, like: 


`![[xxx.png|+grid]]`

Then, you should put the required images on the same line
e.g. `![[xxx.png|+grid]]![[xxx.png|+grid]]![[xxx.png|+grid]]`

Then, done.

Click here to find the demonstration [[Image-grid-1]]

---
**Method 2**

Add the following cssclass directive in YAML

```yaml
---
cssclass: img-grid
---
```

Click here to find the demonstration [[Image-grid-2]]

Likewise, you should put images on the same line
e.g. 
`![[xxx.png]]![[xxx.png]]![[xxx.png]]`

---

## Note blocks
### Colourful note backgrounds
*adapted from Notation theme by @deathau*


Syntax：`note-xxx-bg`  or `note-xxx-background`


```note-orange-bg
text
```

```note-yellow-bg
text
```

```note-green-bg
text
```

```note-blue-bg
text
```

```note-purple-bg
text
```

```note-pink-bg
text
```

```note-red-bg
text
```

```note-gray-bg
text
```

```note-brown-bg
text
```
-----------------------------------------------------

### Colourful note texts
Syntax: `note-color` 

```note-orange
text
```

```note-yellow
text
```

```note-green
text
```

```note-blue
text
```

```note-purple
text
```

```note-pink
text
```

```note-red
text
```

```note-gray
text
```

```note-brown
text
```

-----------------------------------------------------------
### Recall/cloze note blocks 
To show text by clicking

```note-cloze
text
```

### Important note blocks
Important block

```note-imp
text
```

## stickies
*thanks to death_au, Gabroel and Lithou from Obsidian Members Group on Discord* 

Usage

Using the following formats to obtain stickies or inline recall box
`<p class="stickies"> xxx  </p>`
`<p class="stickies2"> xxx </p>`
`<p class="to-recall"> xxx </p>`

Use the following formats, you can obtain some special styles.

<p class="stickies"> Your words </p>
blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
<p class="stickies2"> Your words </p>
blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
<p class="to-recall"> Your words </p>
blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
<br />

<br />

## aside
*thanks to dcoales from obsidian member group on discord  
https://discord.com/channels/686053708261228577/702656734631821413/794236352857374764*

Usage
blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
<aside><h1> Your words </h1></aside>blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah 
<aside><h2> Your words </h2></aside>

## Others
### code wrap
Add the following cssclass directive in YAML to wrap codebox
```yaml
---
cssclass: code-wrap
---
```


### inline lists
Add the following cssclass directive in YAML to embed list inline which can be used with inline images
```yaml
---
cssclass: inline-list
---
```

## css snippets

You can activate some snippets as shown below to customize your Blue Topaz to some extent

![[snippets.png|500]]


- aaa
	- bbb
- ccc
	- ddd
		- eee
1. 111
	1. 222
		1. 333
			1. 444
		2. 555
		3. 666
	2. 777

>Blockquote

>Blockquote

>Blockquote