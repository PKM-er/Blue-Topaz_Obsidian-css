# Blue-Topaz_Obsidian-css

蓝色托帕石不是贵重的宝石，以契合“黑曜石”😜。另外蓝色托帕石一般由无色或浅色黄玉经过人工处理后得到——这个主题不是我从零开始做出来的，而是大量借鉴了他人的主题后，修改而成的，就像蓝色托帕石一样，是后天人造的。在此，感谢所有共享了css文件的人。另外，“无色或浅色黄玉”没有任何暗喻的意思，也没有和别人的主题做比较的意思。如果你能喜欢这个主题，那就很好！

A blue theme for **Obsidian**. Blue Topaz is not a precious gem, like obsidian😜. Generally, Blue Topaz is obtained by artificially treating colourless topaz. Likewise，I did not make this theme from scratch, but modified it after borrowing others' themes. It is like Blue Topaz, which is a modified product. Thus, thanks for the all shared themes, which inspired me indeed! BTY, For the word "colourless topaz", there is no offence and no comparison. And it is not a metaphor. I will be glad if you enjoy the theme, *Blue Topaz*.

# Preview
![](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css/blob/master/preview_Blue%20Topaz.png)

# Installation
1. 下载css文件。
2. 在Obsidian中开启自定义主题。
3. 把obsidian.css放到vault文件夹中（如果已经存在obsidian.css，覆盖原文件）。
---
1. Download css file.
2. Enable custom css in Obsidian.
3. Copy the obsidian.css to your vault directory (or replace, if there is an existing file).

## BTY
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
