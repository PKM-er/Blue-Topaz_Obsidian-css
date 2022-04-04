# 示例 Demo vault
感谢@cumany制作的升级版示例库 https://github.com/cumany/Blue-topaz-examples

# 更新日志
### 20220403
1. 修复admonition 9.0 升级后分栏样式错位
2. 增加文本挖空、涂黑样式，语法分别为：`==~~xx~~==` `*==~~xxx~~==*`。只在阅读模式生效。建议使用插件进行格式刷设置，不建议手打。
![5](https://user-images.githubusercontent.com/72023275/161413180-dfbd303b-c76d-44ed-87a6-b57cc9822775.gif)
3. 增加blank callout类型

### 20220402
1. 兼容admonition 9.0 升级后分栏失效的问题
2. 兼容callout 并内置众多自定义样式例如kanban hibox bookinfo  infobox等具体可以看示例库范例。
3. style settings 
2. 1.5中增加高亮背景颜色设置（==xx==）
### 20220330
1. 添加默认大纲线颜色设置选项
2. OB更新到14.2版本主题大纲线跟默认大纲线重影问题修复
3. 修复预览模式彩虹任务框显示异常
4. 修复ad代码块中任务列表溢出
5. 修复图片跟任务列表混排，任务列表显示不全问题
### 20220330
1. 添加默认大纲线颜色设置选项
2. OB更新到14.2版本主题大纲线跟默认大纲线重影问题修复
3. 修复预览模式彩虹任务框显示异常
4. 修复ad代码块中任务列表溢出
5. 修复图片跟任务列表混排，任务列表显示不全问题

### 20220320
1. 修复软件新版本中，导出pdf无法设置加粗、斜体颜色的问题

### 20220314
1. 伪看板无法折叠列表修复
2. 彩虹大纲线某些时候出现多余细线

### 20220313
1. 文件夹折叠箭头位置调整
2. 修复某些情况下切换文件时出现的页面抖动

### 20220312
1. style settings “2.3.2 列表” 中增加“列表项间距”设置
2. 列表样式优化
3. 列表、标题样式部分问题修复
4. 兼容outliner v1.x版本

### 20220311
1. 修复伪看板跟floating-toc插件冲突
2. 列表（list）样式优化
3. 调整style settings中列表设置
4. 修复标题字体大小设置时突然变大的问题

### 20220310
1. 文件夹列表单行显示，增加文件名滚动效果 （2.3.3）
2. 修复dataview  table多行结果溢出
3. 修复亮色状态下nord配色 图谱文件名显示不明显的问题
4. memos左、右侧边栏的样式优化

### 20220309
1. 调整dataview 表格字体
2. 增加dataview单行显示效果

### 20220308
1. 修复style settings 2.2.3，“编辑状态使用H1 H2 替代[#]”
2. 其他修复
3. 暂时不对版本v0.13.30进行修复，直到下次软件更新
4. 修复无序列表标记消失的问题
5. 增加ad-table 类型 实现表格不换行全宽显示
6. 增加dataview 表格 是否自动添加序号的选项
7. 修复cards样式 如果无图片，标题过大的问题

### 20220307
1. 修复最新banner插件（1.3.1），在阅读模式下显示宽度不全的问题
2. 修复memos插件输入框无法滚动的问题，另外增强memos放右侧边栏滚动效果。

### 20220305
1. 现在支持对两种数学表达式颜色进行设置(行内 $x=0$，段落 $$x=0$$)
2. BASH语言代码框（```bash）现在在阅读模式下显示语言为“SHELL”
3. 移动端阅读模式显示宽度调整
4. 再次修复部分折叠小箭头错位的问题

### 20220301
1. 尝试修复style settings 2.2.3，软件版本v0.13.27下开启“编辑状态使用H1 H2 替代[#]”后造成中文标点光标错位问题，还需要进一步的反馈
2. 修复部分折叠小箭头错位的问题

### 20220227
1. 增加导出PDF设置（style settings中）
2. 显示图片标题的居中格式![[xxx.png#centre|figure]]，现在在live preview下正确居中显示了
3. 其他一些细节问题

### 20220226
1. 增加左侧边栏（ribbon）隐藏选项（style settings中设置，默认关闭）
2. 增加表格样式选项（style settings中）

### 20220225
1. 滑动条悬浮变大，便于鼠标点选

### 20220218
1. 修复视频无法最大化问题
2. 修复Itinerary插件显示问题

### 20220216
1. 增加表格实时预览模式样式
2. 增加编辑模式 大纲线显示

### 20220211
1. 增加1.3界面元素设置：增加隐藏标题栏、侧边栏库名称设置

### 20220210
1. dialogue 插件增加样式

### 20220202
1. 默认隐藏右侧边栏，style settings中可设置“固定右侧边栏”

### 20220201
1. style settings 2.3.3中增加“激活文件夹图标”，开启后可在文件夹栏中文件夹前面增加图标

# Blue-Topaz_Obsidian-css

蓝色托帕石不是贵重的宝石，以契合“黑曜石”😜。另外蓝色托帕石一般由无色或浅色黄玉经过人工处理后得到——这个主题不是我从零开始做出来的，而是大量借鉴了他人的主题后，修改而成的，就像蓝色托帕石一样，是后天人造的。在此，感谢所有共享了css文件的人。另外，“无色或浅色黄玉”没有任何暗喻的意思，也没有和别人的主题做比较的意思。如果你能喜欢这个主题，那就很好！（更多片段请移步至QQ群：908688452）

A blue theme for **Obsidian**. Blue Topaz is not a precious gem, like obsidian😜. Generally, Blue Topaz is obtained by artificially treating colourless topaz. Likewise，I did not make this theme from scratch, but modified it after borrowing others' themes. It is like Blue Topaz, which is a modified product. Thus, thanks for the all shared themes, which inspired me indeed! BTW, For the word "colourless topaz", there is no offence and no comparison. And it is not a metaphor. I will be glad if you enjoy the theme, *Blue Topaz*.

# 示例 Demo vault
感谢@cumany制作的升级版示例库 https://github.com/cumany/Blue-topaz-examples
![image](https://user-images.githubusercontent.com/72023275/148891990-5db9c00f-98bc-41c1-b1a1-a9121c1035a8.png)
![image](https://user-images.githubusercontent.com/72023275/148891998-9f4546fd-0b06-4add-8b73-692523781037.png)
![image](https://user-images.githubusercontent.com/72023275/148892015-19ee2945-36c5-406f-b61c-b905ce85471b.png)
![image](https://user-images.githubusercontent.com/72023275/148892023-c1391a98-9445-41de-97dc-bb2c6731b70c.png)
![image](https://user-images.githubusercontent.com/72023275/148892043-d10819a8-9e4a-4786-9c24-a3adff3ec1db.png)
![image](https://user-images.githubusercontent.com/72023275/148892055-a1eca6ae-dcc8-410e-8824-ca9307ad816f.png)
![image](https://user-images.githubusercontent.com/72023275/148892062-e3bbe32e-bc7f-44ee-b1ab-055cbe4c4411.png)


# 插件 Plugin
强烈建议安装Style Settings插件，用来自定义你的Blue Topaz
It is highly recommended to install the style settings plugin to customize your Blue Topaz theme
![image](https://user-images.githubusercontent.com/72023275/148892207-ffbbb363-1a43-4267-a3f9-d95ee7cc9bd9.png)

Change the color palette
![image](https://user-images.githubusercontent.com/72023275/148892424-9cdbe7a3-68e6-4dd0-91d0-6763361e5ae3.png)


# 字体 (fonts)
中文：霞鹜文楷，免费开源，下载地址：https://github.com/lxgw/LxgwWenKai 觉得喜欢的话，也请给这个项目星星。加粗字体请使用霞鹜文楷屏幕版（因为霞鹜文楷的加粗不是很明显）https://github.com/lxgw/LxgwWenKai-Screen

# Preview
![](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css/blob/master/preview_Blue%20Topaz.png)
![image](https://user-images.githubusercontent.com/72023275/134809308-1bba5cf3-aa70-4581-ae21-2f6fe1da03f8.png)
![image](https://user-images.githubusercontent.com/72023275/134809312-19884827-0a3b-44eb-a4ab-027afa8fb62a.png)

# With Style Settings plugin
![image](https://user-images.githubusercontent.com/72023275/134859512-e9b9c774-f3f4-4b73-9383-ab750e6d5ba5.png)
![image](https://user-images.githubusercontent.com/72023275/134859548-c2083090-24b0-4fd9-8a89-0f3157a8b634.png)
![image](https://user-images.githubusercontent.com/72023275/134859561-dfe21d23-1a89-4e01-b236-8809a7d35e41.png)
![image](https://user-images.githubusercontent.com/72023275/134859571-4eb1580c-a7ba-4ecd-9231-8bfad162207f.png)
![image](https://user-images.githubusercontent.com/72023275/134859577-ca6bf35a-6a6a-45b1-ba0e-5aca7a4c4990.png)
![image](https://user-images.githubusercontent.com/72023275/134859584-ec868841-f237-4f8c-bea8-3e57cfecc3eb.png)

# Support me
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/WhyI)

If you think Blue Topaz is helpful, you can buy me a cup of coffee to support me. Thank you!

# Acknowledgements
I appreciate the help and support from @boninall @成雙醬 @Cuman @Klaas @lillian-who @shaggyfeng @Thinkbond, and other cool guys who love Blue Topaz!
