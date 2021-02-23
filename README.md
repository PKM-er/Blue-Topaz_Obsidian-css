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
=========================
=======列表 list=========
=========================


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

By Klaas from Discord group
```css
div:not(.CodeMirror-activeline)>.HyperMD-quote>span:first-of-type::before {
  content: '“' !important;
  font: 14px/20px italic Times, serif;
  font-weight: 700;
  font-size: 3em; /* PB changed from 18px */
  color: var(--text-accent);
  left: 3px;
  top: 15px;
  position: relative;
}
```
