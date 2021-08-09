# TIPS  

***主题中的一些特别样式 Special parts in this theme***

## 标记
_斜体_
*斜体*
**加粗**
__加粗__
***加粗斜体***
___加粗斜体___

*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__
***To combine***
___To combine___

## 特别标签 Special tags

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

可以打开css，按照special tags的格式，设置自己的特殊标签


## 图片 images
### 图片位置设置

**用法**

在图片末尾加上 “|left” 或 “|right” 可以让图片左或右对齐
xxx.jpg|left


---
可用变体：
left/Left/LEFT/L
right/Right/RIGHT/R

如：xxx.png|L

如果同时调整图片大小，需要把调整大小的数值放在最后
xxx.png|right|200

使用 “|inlineL” 或 “|inlineR” 可以将图片嵌入在文字中,L左，R右
xxx.png|inlineL

---

![[obsidian_image.png|100]]

![[obsidian_image.png|left|150]]

![[obsidian_image.png|R|200]]

---
可用变体：
inlineL/InlineL/INLINEL/inlL
inlineR/InlineR/INLINER/inlR

![[obsidian_image.png|inlR|200]]

如：xxx.png|inlR

-------------------

Usage

Typing "|left" or "|right" at the end of the image file can make the image shown on left or right.
For example,
xxx.jpg|left

---

![[obsidian_image.png|100]]

![[obsidian_image.png|left|150]]

![[obsidian_image.png|R|200]]

---------------------------
The variants you can use：
left/Left/LEFT/L
right/Right/RIGHT/R

![[obsidian_image.png|inlR|300]]

e.g. xxx.png|L

---------------------------

You can also change the image size with the position. You should put the "|number" at the end.
For example,
xxx.png|right|200 

Use "inlineL" or "inlineR" to embed the image on the left or right.
xxx.png|inlineL

-----------------------------
The variants you can use：
inlineL/InlineL/INLINEL/inlL
inlineR/InlineR/INLINER/inlR

e.g. xxx.png|inlL

-----------------------------

### image-captions
 *modified from Discordian by @radekkozak*

Usage

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

### image-grid adapted from Discordian by @radekkozak and orange by @echoxu
Usage

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

## 笔记框 Note blocks
### 不同颜色背景 Colourful note backgrounds
*adapted from Notation theme by @deathau*


语法：```note-xxx-bg 或```note-xxx-background


```note-orange-bg
正文text
```

```note-yellow-bg
正文text
```

```note-green-bg
正文text
```

```note-blue-bg
正文text
```

```note-purple-bg
正文text
```

```note-pink-bg
正文text
```

```note-red-bg
正文text
```

```note-gray-bg
正文text
```

```note-brown-bg
正文text
```
-----------------------------------------------------

### 不同笔记颜色 Colourful note texts

```note-orange
正文text
```

```note-yellow
正文text
```

```note-green
正文text
```

```note-blue
正文text
```

```note-purple
正文text
```

```note-pink
正文text
```

```note-red
正文text
```

```note-gray
正文text
```

```note-brown
正文text
```

-----------------------------------------------------------
### 记忆笔记框 Recall/cloze note blocks 
可鼠标点击显示笔记内容 To show text by clicking

```note-cloze
正文text
```

### 重要笔记框 important note blocks
有笔记外框 Different block style

```note-imp
正文text
```

## stickies
*thanks to death_au, Gabroel and Lithou from Obsidian Members Group on Discord* 

用法
Usage

用以下格式，可以得到不同的样式

文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字
<p class="stickies"\> 你自己的文字 </p>
文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字

<p class="stickies2"\> 你自己的文字 </p>
文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字
<p class="to-recall"\> 你自己的文字 </p>
文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字

Use the following formats, you can obtain some special styles.
<p class="stickies"\> Your words </p>
<p class="stickies2"\> Your words </p>
<p class="to-recall"\> Your words </p>

<br />

<br />

<br />

## aside
*thanks to dcoales from obsidian member group on discord  
https://discord.com/channels/686053708261228577/702656734631821413/794236352857374764*

Usage
文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字
<aside><h1> Your words </h1></aside>文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字文字
<aside><h2> Your words </h2></aside>

## css片段

开启片段后，可以在这看看效果
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