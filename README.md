# Blue-Topaz_Obsidian-css

蓝色托帕石不是贵重的宝石，以契合“黑曜石”😜。另外蓝色托帕石一般由无色或浅色黄玉经过人工处理后得到——这个主题不是我从零开始做出来的，而是大量借鉴了他人的主题后，修改而成的，就像蓝色托帕石一样，是后天人造的。在此，感谢所有共享了css文件的人。另外，“无色或浅色黄玉”没有任何暗喻的意思，也没有和别人的主题做比较的意思。如果你能喜欢这个主题，那就很好！

A blue theme for **Obsidian**. Blue Topaz is not a precious gem, like obsidian😜. Generally, Blue Topaz is obtained by artificially treating colourless topaz. Likewise，I did not make this theme from scratch, but modified it after borrowing others' themes. It is like Blue Topaz, which is a modified product. Thus, thanks for the all shared themes, which inspired me indeed! BTY, For the word "colourless topaz", there is no offence and no comparison. And it is not a metaphor. I will be glad if you enjoy the theme, *Blue Topaz*.

# Preview
![](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css/blob/master/preview_Blue%20Topaz.png)

```
===========================    TIPS   ===============================
====================================================================
===========主题中的一些特别样式 Special parts in this theme===========
=====================================================================
```
```
==========================
=====标签 Special tags=====
==========================
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
```
```
===========================
=====笔记框 Note blocks=====
===========================

----------------------------------------------------------------------
---------------不同颜色背景 Colourful note backgrounds-----------------
----------------------------------------------------------------------
语法：```note-xxx-bg 或```note-xxx-background
---------------------------------------------

```note-orange-bg

```note-yellow-bg

```note-green-bg

```note-blue-bg

```note-purple-bg

```note-pink-bg

```note-red-bg

```note-gray-bg

```note-brown-bg

-----------------------------------------------------
----------不同笔记颜色 Colourful note texts------------
-----------------------------------------------------

```note-orange

```note-yellow

```note-green

```note-blue

```note-purple

```note-pink

```note-red

```note-gray

```note-brown

-----------------------------------------------------------
------------记忆笔记框 Recall/cloze note blocks-------------
-----------------------------------------------------------
可鼠标点击显示笔记内容 To show text by clicking
-----------------------------------------------------------

```note-cloze

--------------------------------------------------------
------------重要笔记框 important note blocks-------------
--------------------------------------------------------
有笔记外框 Different block style
--------------------------------------------------------

```note-imp

```

```
==========================
========图片 Images=======
==========================

图片有两段放大：悬停(100%)，点击(110%)
Image can be zoomed in by hovering (100%) and clicking (110%).
```


```
=========================
=======列表 list=========
=========================
```
1. If you just don’t want the box
You should copy the following code to a new .txt file with any name you like, 
then rename the .txt to .css and put the .css file to “vault/.obsidian/snippets” folder, 
and activate the css snippet in Obsidian Setting–> Appearance --> CSS snippets.

```css
ul > li:not(.task-list-item), 
ol > li {
  box-shadow: none !important;
} 
```


------------------------------------------------------------
2. If you can live with the box appearing when the mouse hovers
You should copy this:

```css
ul > li:not(.task-list-item):not(:hover), 
ol > li:not(:hover) {
  box-shadow: none;
} 
```

------------------------------------------------------------
3. If you just want the previous style (without automatic counting like “1.1.2”)
You should copy the following:

```css
ul ul::before,
ol ul::before,
ul ol::before,
ol ol::before {
  content:'';
  border-left: 2px solid var(--background-modifier-border);
  position: absolute;
}

ul ul::before,
ol ul::before,
ul ol::before,
ol ol::before {
  left: -13px;
  top: 28px;
  bottom: 0;
} 

li > p:not(.task-list-item) {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}
  
ul,
ul ul, 
ol ul, 
ul ul ul,
ul ol ul,
ol ul ul, 
ol ol ul {
  list-style: disc;
}
  
ul > li:not(.task-list-item) {
  padding-left: 0px;
  list-style-position: outside;
  margin-bottom: 8px;
  padding-right: 0px;
  margin-block-start: 0.5em;
}
  
  
ul > li:not(.task-list-item) {
  border-left: none !important;
  box-shadow: none !important;
}
  
ul > li:not(.task-list-item)::before {
  display: none !important;
}
  
ol {
  display: block;
  list-style-type: decimal;
  margin-block-start: 0.5em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
  padding-inline-start: 2.5em;
  margin-left: 0px;
}
  
ol > li {
  padding-left: 0px;
  list-style-position: outside;
  margin-bottom: 8px;
  padding-right: 0px;
} 
  
ol > li {
  border-left: none !important;
  box-shadow: none !important;
} 

ol > li::before {
  display: none;
}
```
------------------------------------------------------------
4. The last one, if you want the previous style with the automatic counting
Use this:

```css
ul ul::before,
ol ul::before,
ul ol::before,
ol ol::before {
  content:'';
  border-left: 2px solid var(--background-modifier-border);
  position: absolute;
}

ul ul::before,
ol ul::before,
ul ol::before,
ol ol::before {
  left: -13px;
  top: 28px;
  bottom: 0;
} 

li > p:not(.task-list-item) {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}
  
ul,
ul ul, 
ol ul, 
ul ul ul,
ul ol ul,
ol ul ul, 
ol ol ul {
  list-style: disc;
}
  
ul > li:not(.task-list-item) {
  padding-left: 0px;
  list-style-position: outside;
  margin-bottom: 8px;
  padding-right: 0px;
  margin-block-start: 0.3em;
}
  
  
ul > li:not(.task-list-item) {
  border-left: none !important;
  box-shadow: none !important;
}
  
ul > li:not(.task-list-item)::before {
  display: none !important;
}
  
ol {
  display: block;
  margin-block-start: 0.5em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
  padding-inline-start: 2.5em;
  margin-left: 0px;
}
  
ol > li {
  padding-left: 0px;
  list-style-position: inside;
  margin-bottom: 8px;
  padding-right: 0px;
} 
  
ol > li {
  border-left: none !important;
  box-shadow: none !important;
} 

ol > li::before {
  margin-left: -17px;
}
```

---
```
=========================================
=========tapes pins and stickies=========
=========================================
```
thanks to death_au, Gabroel and Lithou from Obsidian Members Group on Discord 

用法

在图片后加上 #tape 或者 #pin
形如
```
![[Pasted image.png#pin]]
```
可以获得特别的效果

用以下格式，可以得到不同的样式
```
<p class="stickies"\> 你自己的文字 </p>
<p class="stickies2"\> 你自己的文字 </p>
<p class="to-recall"\> 你自己的文字 </p>
```

USAGE
add #tape or #pin at the end of an image,
like
```
![[Pasted image.png#pin]]
```
Then you can get a pin-like style for the image

Use the following formats, you can obtain some special styles.
```
<p class="stickies"\> Your words </p>
<p class="stickies2"\> Your words </p>
<p class="to-recall"\> Your words </p>
```

add Image Flags Snippet by Lithou
http://github.com/lithou/sandbox

Usage:
Please see https://publish.obsidian.md/lithousandbox/Image+Flags+(Core+Documentation)

```
=============================
==== <aside> </aside> =======
=============================
```
thanks to dcoales from obsidian member group on discord  
https://discord.com/channels/686053708261228577/702656734631821413/794236352857374764

Use 
```
<aside><h1> Your words </h1></aside>
<aside><h2> Your words </h2></aside>
```
to get a right-side note block


---

## BTW
```css
/* Blockquote header */
.markdown-preview-view blockquote {
   position: relative; /* for pseudos */
   color: var(--ztys);
   font-size: 1rem;
   font-weight: normal;
   line-height: 1.5;
   margin: 0;
   border: solid 2px;
   border-radius:20px;
   padding: 15px;
}

.markdown-preview-view blockquote p{
  color: var(--text-normal);
  font-size: 16px;
}

.markdown-preview-view blockquote:after {
   content:"";
   position: absolute;
   border: 2px solid var(--ztys);
   border-radius: 45px 0 0 0;
   width: 60px;
   height: 60px;
   bottom: -62px;
   left: 20px;
   border-bottom: none;
   border-left: none;
   border-right: none;
   z-index: 3; 
}

.markdown-preview-view blockquote:before {
   content:"";
   position: absolute;
   width: 25px;
   border: 10px solid var(--background-primary);
   bottom: -3px;
   left: 30px;
   z-index: 2;
}

.markdown-preview-view blockquote :first-letter {
 margin-left:2em;
}
```
![](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css/blob/master/blockquote.jpg?raw=true)

---
