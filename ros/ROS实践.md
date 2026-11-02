## l  ROS文件系统介绍
### 1、rospack：允许获取软件包的有关信息
用法：$ rospack find [包名称]

示例：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478621363-eabab765-9ca8-461e-b766-5864a67b61ce.png)

### 2、roscd：
rosbash命令集中的一部分，它允许你直接切换（cd）工作目录到某个软件包或者软件包集当中。

用法：$ roscd [本地包名称[/子目录]]

示例：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478625858-4207be34-53f1-4c78-80cb-22c36a24abb5.png)

### 3、rosls：
是 rosbash 命令集中的一部分，它允许你直接按软件包的名称而不是绝对路径执行 ls 命令。

用法：$ rosls [本地包名称[/子目录]]

示例：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478623106-6347b41d-a676-4792-be6d-3ecb19f6ad93.png)

4、Tab：自动补全

用法：

① 输入：$ roscd roscpp_tut

② 按下 TAB 键

当按 TAB 键后，命令行中会自动补充剩余部分：$ roscd roscpp_tutorials/

5、ROS命令工具的命名方式：

rospack = ros + pack(age)

roscd = ros + cd

rosls = ros + ls

### <font style="color:rgb(63, 74, 86);">使用rosed编辑ROS中的文件</font>
+ 使用rosed
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosed</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 是 rosbash 的一部分。利用它可以直接通过package名来获取到待编辑的文件而无需指定该文件的存储路径了。</font>
+ <font style="color:rgb(63, 74, 86);">使用方法:</font>

```javascript
$ rosed [package_name] [filename]
```

<font style="color:rgb(63, 74, 86);">例子:</font>

```bash
$ rosed roscpp Logger.msg
```

### <font style="color:rgb(63, 74, 86);">使用 rqt_console 和 roslaunch</font>
+ <font style="color:rgb(63, 74, 86);">预先安装rqt和turtlesim程序包</font>

```bash
$ sudo apt-get install ros-kinetic-rqt ros-kinetic-rqt-common-plugins ros-kinetic-turtlesim
```

+ 使用rqt_console和rqt_logger_level
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_console</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">属于ROS日志框架(logging framework)的一部分，用来显示节点的输出信息</font>
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_logger_level</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">允许我们修改节点运行时输出信息的日志等级（logger levels）（包括 DEBUG、WARN、INFO和ERROR）。</font>

```bash
#先打开一个终端启动roscore，否则无法打开rqt_console和rqt_logger_level
roscore
#新终端
$ rosrun rqt_console rqt_console
#新终端
$ rosrun rqt_logger_level rqt_logger_level
#新终端
$ rosrun turtlesim turtlesim_node
#新终端
$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478722211-58f7c203-cf2c-4b4f-98fa-83d7ad903565.png)

| 命令片段 | 作用 / 含义 |
| --- | --- |
| `$` | Linux 终端的普通用户提示符（非核心，仅表示这是终端命令） |
| `sudo` | 以 root（管理员）权限执行后续命令（安装软件需要管理员权限） |
| `apt-get` | Debian/Ubuntu 系统的核心包管理工具，用于安装 / 卸载 / 更新软件包 |
| `install` | `apt-get`<br/> 的子命令，代表「安装软件包」 |
| `ros-kinetic-rqt` | 要安装的第一个包：ROS Kinetic 版本的 rqt 基础框架（ROS 可视化工具核心） |
| `ros-kinetic-rqt-common-plugins` | 第二个包：rqt 的常用插件集合（比如图形化控制台、数据可视化插件） |
| `ros-kinetic-turtlesim` | 第三个包：ROS 经典的海龟仿真器（新手入门常用，用于测试话题 / 服务等功能） |


+ 日志等级说明

```javascript
Fatal #最高优先级
Error
Warn
Info
Debug #最低优先级
```

    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">通过设置日志等级你可以获取该等级及其以上优先等级的所有日志消息。比如，将日志等级设为</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Warn</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">时，你会得到</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Warn</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Error</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">和</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Fatal</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">这三个等级的所有日志消息。</font>
+ 使用roslaunch
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roslaunch</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可以用来启动定义在launch文件中的多个节点。</font>
    - <font style="color:rgb(63, 74, 86);">用法：</font>

```bash
$ roslaunch [package] [filename.launch]
```

```bash
#先创建一个程序包
cd ~/catkin_ws/src
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp

#切换到beginner_tutorials程序包目录下
$ roscd beginner_tutorials

#创建一个launch文件夹
$ mkdir launch
$ cd launch
```

+ launch文件

```bash
# 创建一个名为turtlemimic.launch的launch文件
vim turtlemimic.launch

#粘贴一下内容
# 以launch标签开头以表明这是一个launch文件
<launch>  

# 创建了两个节点分组并以'命名空间（namespace)'标签来区分，其中一个名为turtulesim1，另一个名为turtlesim2，两个组里面都使用相同的turtlesim节点并命名为'sim'。这样可以让我们同时启动两个turtlesim模拟器而不会产生命名冲突。
  <group ns="turtlesim1">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <group ns="turtlesim2">
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>

  <node pkg="turtlesim" name="mimic" type="mimic">
    <remap from="input" to="turtlesim1/turtle1"/>
    <remap from="output" to="turtlesim2/turtle1"/>
  </node>

</launch>
```

| 属性 | 意思 |
| --- | --- |
| `pkg` | 功能包名字 → `turtlesim` |
| `name` | 给节点起个名字 → `sim` |
| `type` | 要运行的**可执行文件** → `turtlesim_node` |


 启动 turtlesim 包里的海龟仿真器节点  

    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">① mimic 是什么？	</font>
        * <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">ROS 官方提供的 </font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">“模仿节点”</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">作用：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">让一个海龟模仿另一个海龟</font>**
    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">② </font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"><remap></font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> 重映射（超级重要）	</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">xml</font>

```plain
<remap from="input" to="turtlesim1/turtle1"/>
```

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">意思：</font>

+ `<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">from="input"</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：mimic 原本要订阅的话题名</font>
+ `<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">to="turtlesim1/turtle1"</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">改成订阅第一只海龟</font>**

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">xml</font>

```plain
<remap from="output" to="turtlesim2/turtle1"/>
```

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">意思：</font>

    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">把输出命令发给 </font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">第二只海龟</font>**
    - **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">最终效果：第一只海龟的动作 → 传给 mimic → 控制第二只海龟</font>**
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">pkg = turtlesim</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">（包）</font>
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">type = turtlesim_node</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">（包里的可执行文件）</font>
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">name = sim</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">（你给它起的名字）</font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478741798-a6e4ae6f-783d-4a12-868b-88c191a9e95d.png)

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">roslaunch</font>

```plain
   $ roslaunch beginner_tutorials turtlemimic.launch


   # 一个新终端中使用rostopic命令发送速度设定消息：
   $ rostopic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'

   # rqt_graph来更好的理解在launch文件中所做的事情。
   $ rqt_graph
```

### roswtf入门
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">roswtf可以检查你的ROS系统并尝试发现问题，关闭之前打开的终端及程序，否则下面命令会提示错误，</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">静态检查，没有运行ROS主节点roscore</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">运行时检查，运行</font>
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">错误报告</font>
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roswtf</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">会对一些系统中看起来异常但可能是正常的运行情况发出警告。也会对确实有问题的情况报告错误。</font>
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roswtf</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">还可以发现很多其它类型的问题。如果你发现自己被一个编译或者通信之类的问题困扰的时候，可以尝试运行</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roswtf</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">看能否帮你解决。</font>
+  进入当前工作空间的 devel 或 build 目录  roscd
    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">当前工作空间 = 你</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">source 过的那个 catkin_ws</font>**
    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">比如你平时编译 ROS 代码时：</font>

```plain
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

    - **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">只要你执行过 source，这个 catkin_ws 就是 “当前工作空间”</font>**
    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">roscd、rosls、rosrun 全部认的是</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">这个被 source 过的空间</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">。</font>

## ROS程序包
### 创建ROS程序包
+ <font style="color:rgb(63, 74, 86);">一个catkin程序包由什么组成?</font>
    - <font style="color:rgb(63, 74, 86);">该程序包必须包含catkin compliant package.xml文件，这个package.xml文件提供有关程序包的元信息。</font>
    - <font style="color:rgb(63, 74, 86);">程序包必须包含一个catkin 版本的CMakeLists.txt文件，而Catkin metapackages中必须包含一个对CMakeList.txt文件的引用。</font>
        * `<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">package.xml</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：包的身份证（名字、版本、依赖）</font>
        * `<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">CMakeLists.txt</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：告诉编译器怎么编译代码</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">每个目录下只能有一个程序包。这意味着在同一个目录下不能有嵌套的或者多个程序包存在。</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">最简单的程序包也许看起来就像这样：</font>

```plain
my_package/
  CMakeLists.txt
  package.xml
```

+ catkin工作空间
    - 工作空间简介

```plain
workspace_folder/        -- WORKSPACE[工作空间]
  src/                   -- SOURCE SPACE[源代码空间]
    CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
    package_1/
      CMakeLists.txt     -- CMakeLists.txt file for package_1
      package.xml        -- Package manifest for package_1
    ...
    package_n/
      CMakeLists.txt     -- CMakeLists.txt file for package_n
      package.xml        -- Package manifest for package_n
```

+ <font style="color:rgb(63, 74, 86);">创建一个 catkin 工作空间</font>

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws
$ catkin_make
```

    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_make</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 命令在 catkin 工作空间 中是一个非常方便的工具。第一次在你的工作空间中运行它时，它会在你的 'src' 文件夹里创建一个 CMakeLists.txt 的链接。注意， 对于 Python 3 用户，在一个空的 catkin 工作空间中第一次运行 catkin_make 的命令应为</font>

```bash
$ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python
```

    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">当前目录应该能看到 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">build</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 和 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">devel</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 这两个文件夹。在 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">devel</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 文件夹里面你可以看到几个 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">setup.*sh</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 文件。</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">source</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 这些文件中的任何一个都可以将当前工作空间设置在ROS工作环境的最顶层</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">接下来首先 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">source</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 一下新生成的 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">setup.bash</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 文件：</font>

```bash
$ source devel/setup.bash
```

    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">保证工作空间已配置正确，需确保ROS_PACKAGE_PATH环境变量包含你的工作空间目录</font>

```bash
$ echo $ROS_PACKAGE_PATH
```

+ <font style="color:rgb(63, 74, 86);">创建一个catkin程序包</font>

```bash
$ cd ~/catkin_ws/src

$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```

    - catkin_create_pkg用法

```bash
# catkin_create_pkg <package_name> [依赖1] [依赖2] [依赖3]
```

+ <font style="color:rgb(63, 74, 86);">程序包依赖关系</font>
    - <font style="color:rgb(63, 74, 86);">一级依赖</font>
        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_create_pkg</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令时提供了几个程序包作为依赖包，现在我们可以使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rospack</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令工具来查看一级依赖包。</font>

```bash
$ rospack depends1 beginner_tutorials 

#输出以下三个一级依赖
rospy
roscpp
std_msgs
```

        * 查看<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">package.xml: </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rospack</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">列出了在运行</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_create_pkg</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令时作为参数的依赖包，这些依赖包随后保存在</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">package.xml</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">文件中。</font>

```bash
$ roscd beginner_tutorials
$ cat package.xml


#可以看到
<package>
...
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
...
</package>
```

    - 间接依赖
        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">一个依赖包还会有它自己的依赖包，比如，rospy还有其它依赖包。</font>

```bash
$ rospack depends1 rospy

#输出
genpy
roscpp
rosgraph
rosgraph_msgs
roslib
std_msgs
```

        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">一个程序包还可以有好几个间接的依赖包，使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rospack depends</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可以递归检测出所有的依赖包。</font>

```bash
$ rospack depends beginner_tutorials
```

            + <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777300108054-177245f7-53d9-4a0b-96b9-151354cbd520.png)
+ 自定义你的程序包
    - <font style="color:rgb(63, 74, 86);">自定义 package.xml		</font>
        * <font style="color:rgb(63, 74, 86);">描述标签</font>
            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">描述信息修改为任何你喜欢的内容，但是按照约定第一句话应该简短一些，因为它覆盖了程序包的范围。如果用一句话难以描述完全那就需要换行了。</font>

```bash
# 打开标签
$ cd ~/catkin_ws/src/beginner_tutorials
$ vim package.xml

#更新描述标签
5   <description>I Love ROS</description>
```

        * <font style="color:rgb(63, 74, 86);">维护者标签</font>
            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">这是package.xml中要求填写的一个重要标签，因为它能够让其他人联系到程序包的相关人员。至少需要填写一个维护者名称，但如果有需要的话你可以添加多个。除了在标签里面填写维护者的名称外，还应该在标签的email属性中填写邮箱地址。</font>

```bash
 <maintainer email="you@yourdomain.tld">Your Name</maintainer>
```

        * <font style="color:rgb(63, 74, 86);">许可标签</font>
            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">选择一种许可协议并将它填写到这里。一些常见的开源许可协议有BSD、MIT、Boost Software License、GPLv2、GPLv3、LGPLv2.1和LGPLv3。你可以在</font>[<font style="color:rgb(53, 130, 251);">Open Source Initiative</font>](https://opensource.org/licenses/alphabetical)<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">中阅读其中的若干个许可协议的相关信息。对于本教程我们将使用BSD协议，因为ROS核心组件的剩余部分已经使用了该协议：</font>

```bash
 <license>BSD</license>
```

        * <font style="color:rgb(63, 74, 86);">依赖项标签</font>
            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">接下来的标签用来描述程序包的各种依赖项，这些依赖项分为</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">build_depend</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">buildtool_depend</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">run_depend</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">test_depend</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">。关于这些标签的更详细介绍请参考Catkin Dependencies相关的文档。在之前的操作中，因为我们将 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">std_msgs</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roscpp</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">、 和 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rospy</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">作为</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_create_pkg</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令的参数，所以生成的依赖项看起来如下：</font>

```bash
<buildtool_depend>catkin</buildtool_depend>   #编译工具依赖，编译时需要的工具
<build_depend>roscpp</build_depend>			#编译时需要的库 / 代码
<build_depend>rospy</build_depend>
<build_depend>std_msgs</build_depend>

<exec_depend>roscpp</exec_depend>			#运行时需要的库 / 代码
<exec_depend>rospy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">因为在编译和运行时我们需要用到所有指定的依赖包，因此还需要将每一个依赖包分别添加到run_depend标签中。</font>
    - <font style="color:rgb(63, 74, 86);">自定义 CMakeLists.txt	</font>

### 编译ROS软件包
1. 编译程序包

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">一旦安装了所需的系统依赖项，我们就可以开始编译刚才创建的程序包了。</font>

```bash
# 让终端能找到 ROS 的命令、库、程序包
$ source /opt/ros/kinetic/setup.bash
```

    1. 使用catkin_make

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_make</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 是一个命令行工具，它简化了catkin的标准工作流程。你可以认为</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">catkin_make</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">是在CMake标准工作流程中依次调用了</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">cmake</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 和 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">make</font>`

```bash
# 在catkin工作空间下
$ catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
```

    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">CMake标准工作流程主要可以分为以下几个步骤：</font>

```bash
# 在一个CMake项目里
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install  # (可选)
```

            + <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">多个catkin项目可以放在工作空间中一起编译，工作流程如下：</font>

```bash
# In a catkin workspace
$ catkin_make
$ catkin_make install  # (可选)
```

		<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">上述命令会编译</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">src</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">文件夹下的所有catkin工程</font>

        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">如果你的源代码不在默认工作空间中（~/catkin_ws/src),比如说存放在了</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">my_src</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">中</font>

```bash
# In a catkin workspace
$ catkin_make --source my_src
$ catkin_make install --source my_src  # (optionally)
```

    2. 开始编译你的软件包

```bash
$ cd ~/catkin_ws/
$ catkin_make
$ ls

#输出
build
devel
src
```

    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">build</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 目录是build space的默认所在位置，同时</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">cmake</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 和 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">make</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">也是在这里被调用来配置并编译你的程序包。</font>
    - `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">devel</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 目录是devel space的默认所在位置, 同时也是在你安装程序包之前存放可执行文件和库文件的地方。</font>

## ROS节点
### 理解ROS节点
1. 图概念概述
+ <font style="color:rgb(63, 74, 86);">Nodes:节点,一个节点即为一个可执行文件，它可以通过ROS与其它节点进行通信。</font>
+ <font style="color:rgb(63, 74, 86);">Messages:消息，消息是一种ROS数据类型，用于订阅或发布到一个话题。</font>
+ <font style="color:rgb(63, 74, 86);">Topics:话题,节点可以发布消息到话题，也可以订阅话题以接收消息。</font>
+ <font style="color:rgb(63, 74, 86);">Master:节点管理器，ROS名称服务 (比如帮助节点找到彼此)。</font>
+ <font style="color:rgb(63, 74, 86);">rosout: ROS中相当于stdout/stderr。</font>
+ <font style="color:rgb(63, 74, 86);">roscore: 主机+ rosout + 参数服务器 (参数服务器会在后面介绍)</font>
    1. <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">节点</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">一个节点其实只不过是ROS程序包中的一个可执行文件。ROS节点可以使用ROS客户库与其他节点通信。节点可以发布或接收一个话题。节点也可以提供或使用某种服务。</font>
    2. 客户端库

<font style="color:rgb(63, 74, 86);">ROS客户端库允许使用不同编程语言编写的节点之间互相通信:</font>

    - <font style="color:rgb(63, 74, 86);">rospy = python 客户端库</font>
    - <font style="color:rgb(63, 74, 86);">roscpp = c++ 客户端库</font>
    3. roscore

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">roscore</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 是你在运行所有ROS程序前首先要运行的命令。</font>

2. 使用rosrun

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosrun</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 允许你使用包名直接运行一个包内的节点(而不需要知道这个包的路径)。</font>

<font style="color:rgb(63, 74, 86);">用法:</font>

```bash
$ rosrun [package_name] [node_name]
```

<font style="color:rgb(63, 74, 86);">现在我们可以运行turtlesim包中的 turtlesim_node。</font>

<font style="color:rgb(63, 74, 86);">然后, 在一个</font><font style="color:rgb(63, 74, 86);"> </font>**<font style="color:rgb(63, 74, 86);">新的终端</font>**<font style="color:rgb(63, 74, 86);">:</font>

```bash
$ rosrun turtlesim turtlesim_node #会看到 turtlesim 窗口

#新终端
$ rosnode list
#输出
/rosout
/turtlesim

```

 <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">ROS的一个强大特性就是你可以通过命令行重新配置名称</font>

```bash
$ rosrun turtlesim turtlesim_node __name:=my_turtle

#新终端
$ rosnode list
#输出
/rosout
/my_turtle
```

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">我们可以看到新的</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">/my_turtle</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 节点。使用另外一个 </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosnode</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 指令, </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">ping</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">, 来测试</font>

```bash
$ rosnode ping my_turtle
```

`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">rosnode ping</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 是 ROS 官方提供的节点连通性诊断工具，用于测试与指定 ROS 节点的通信可达性与响应状态。   以此验证节点是否正常运行、网络连通是否正常、进程是否卡死</font>

## <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">理解ROS话题</font>
1. 开始
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">首先确保roscore已经运行, 打开一个新的终端：</font>
+ **<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在一个新的终端中</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">运行： $ rosrun turtlesim turtlesim_node  </font>
+ <font style="color:rgb(63, 74, 86);">通过键盘远程控制turtle</font>
    - **<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在一个新的终端中</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">运行：$ rosrun turtlesim turtle_teleop_key</font><!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777387717539-586cc8d5-3254-4257-83c3-0c021532cf7c.png)
2. ROS Topics

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtlesim_node</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">节点和</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtle_teleop_key</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">节点之间是通过一个ROS</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">话题</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">来互相通信的。</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtle_teleop_key</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在一个话题上</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">发布</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">按键输入消息，而</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtlesim</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">则</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">订阅</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">该话题以接收该消息。下面让我们使用</font>[<font style="color:rgb(53, 130, 251);">rqt_graph</font>](http://wiki.ros.org/rqt_graph)<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">来显示当前运行的节点和话题。</font>

2.1 使用rqt_graph

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_graph</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">能够创建一个显示当前系统运行情况的动态图形。rqt_graph是</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">程序包中的一部分。</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在新终端中运行： $ rosrun rqt_graph rqt_graph  </font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777388060493-2da8ea7d-404a-4a58-b495-135cafded0e3.png)

2.2 rostopic介绍

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令工具能让你获取有关ROS</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">话题</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">的信息。</font>

```bash
# 使用帮助选项查看rostopic的子命令：
$ rostopic -h

# 输出
rostopic bw     display bandwidth used by topic
rostopic echo   print messages to screen
rostopic hz     display publishing rate of topic
rostopic list   print information about active topics
rostopic pub    publish data to topic
rostopic type   print topic type
```

	2.3 使用rostopic echo

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic echo</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可以显示在某个话题上发布的数据。用法：</font>

```bash
rostopic echo [topic]

#在一个新终端中看一下turtle_teleop_key节点在/turtle1/cmd_vel话题（非hydro版）上发布的数据。
$ rostopic echo /turtle1/cmd_vel
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777388595582-9d00f6fb-846e-4696-bc02-64f74ef94633.png)

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">再看一下</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_graph</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">（你可能需要刷新一下ROS graph）。正如你所看到的，</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic echo</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">(红色显示部分）现在也</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">订阅</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">了</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtle1/cmd_vel</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">话题。</font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777388758575-20a583eb-6e25-49c4-9930-190db15d17e8.png)

2.4 使用rostopic list

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic list</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">能够列出所有当前订阅和发布的话题。</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在新终端中运行： $ rostopic list -h  </font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">输出：</font>

```bash
Usage: rostopic list [/topic]

Options:
  -h, --help            show this help message and exit
  -b BAGFILE, --bag=BAGFILE
                        list topics in .bag file
  -v, --verbose         list full details about each topic
  -p                    list only publishers
  -s                    list only subscribers
```

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">在</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic list</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">中使用</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">verbose</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">选项</font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777389497838-25477b12-9687-407b-9e6d-a78fddc4bf63.png)

3. ROS Message

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">话题之间的通信是通过在节点之间发送ROS</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">消息</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">实现的。</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">对于发布器(</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtle_teleop_key</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">)和订阅器(</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtulesim_node</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">)之间的通信，发布器和订阅器之间必须发送和接收相同</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">类型</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">的消息。这意味着话题的</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">类型</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">是由发布在它上面的消息</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">类型</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">决定的。使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic type</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令可以查看发布在某个话题上的消息</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">类型</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">。</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">3.1 使用rostopic type</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">用法：</font>

```bash
rostopic type [topic]
```

运行： $ rostopic type /turtle1/cmd_vel  

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosmsg</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">命令来查看消息的详细情况： $ rosmsg show geometry_msgs/Twist  </font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777389725060-00c257b0-666d-4b16-a4bd-37741898a878.png)

3.2 rostopic pub

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rostopic pub</font>`<font style="color:rgb(63, 74, 86);">可以把数据发布到当前某个正在广播的话题上。</font>

<font style="color:rgb(63, 74, 86);">用法： rostopic pub [topic] [msg_type] [args]  </font>

```bash
$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">以上命令会发送一条消息给turtlesim，告诉它以2.0大小的线速度和1.8大小的角速度开始移动。</font>

+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">rostopic pub		这条命令将会发布消息到某个给定的话题。  </font>
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">-1	（单个破折号）这个参数选项使rostopic发布一条消息后马上退出。  </font>
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">/turtle1/cmd_vel	 这是消息所发布到的话题名称。  </font>
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">--	 （双破折号）这会告诉命令选项解析器接下来的参数部分**都不是**命令选项。这在参数里面包含有破折号`-`（比如负号）时是必须要添加的。  </font>
+ <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">你可能已经注意到turtle已经停止移动了。这是因为turtle需要一个稳定的频率为1Hz的命令流来保持移动状态。我们可以使用`rostopic pub -r`命令来发布一个稳定的命令流：</font>

```bash
$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777390818537-80eb110b-3556-4398-8392-3843a0053eee.png)

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可以看到rostopic发布器节点（红色）正在与rostopic echo节点（绿色）进行通信</font>

4. <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">使用rqt_plot</font>

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_plot</font>`<font style="color:rgb(63, 74, 86);">命令可以实时显示一个发布到某个话题上的数据变化图形。这里我们将使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_plot</font>`<font style="color:rgb(63, 74, 86);">命令来绘制正在发布到</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">/turtle1/pose</font>`<font style="color:rgb(63, 74, 86);">话题上的数据变化图形。首先，在一个新终端中运行</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rqt_plot</font>`<font style="color:rgb(63, 74, 86);">命令：</font>

```bash
$ rosrun rqt_plot rqt_plot
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777391713962-2a7d0a21-38fc-474f-ba74-ac31481029bf.png)

## 理解ROS服务和参数
<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">服务（services）是节点之间通讯的另一种方式。服务允许节点发送</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">请求（request）</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> 并获得一个</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">响应（response）</font>**

1. 使用rosservice
+ `<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosservice</font>`<font style="color:rgb(63, 74, 86);">可以很轻松的使用 ROS 客户端/服务器框架提供的服务。</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosservice</font>`<font style="color:rgb(63, 74, 86);">提供了很多可以在topic上使用的命令，如下所示：</font>

<font style="color:rgb(63, 74, 86);">使用方法:</font>

```javascript
rosservice list         输出可用服务的信息
rosservice call         调用带参数的服务
rosservice type         输出服务类型
rosservice find         依据类型寻找服务find services by service type
rosservice uri          输出服务的ROSRPC uri
```

    1. rosservice list

在新终端中运行： $ rosservice list  

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">重置（reset）</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">, </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">清除（clear）</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">, </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">再生（spawn）</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">, </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">终止（kill）</font>`

```javascript
/clear
/kill
/reset
/rosout/get_loggers
/rosout/set_logger_level
/spawn
/teleop_turtle/get_loggers
/teleop_turtle/set_logger_level
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/get_loggers
/turtlesim/set_logger_level
```

    2. rosservice type
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">使用方法: rosservice type [service]  </font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">查看clear服务的类型，运行： </font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">$ rosservice type clear</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">  输出： std_srvs/Empty  </font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">服务的类型为空（empty),这表明在调用这个服务是不需要参数（比如，请求不需要发送数据，响应也没有数据）。</font>
    3. <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">rosservice call</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">使用方法： rosservice call [service] [args]  </font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">因为服务类型是空，所以进行无参数调用： </font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">$ rosservice call clear</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">  正如我们所期待的，服务清除了</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">turtlesim_node</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">的背景上的轨迹。</font>
    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">通过查看再生（spawn）服务的信息，我们来了解带参数的服务，运行：</font>**<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);"> $ rosservice type spawn| rossrv show  </font>**
        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">上面部分：</font><font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">请求（客户端发给服务端）， 下面部分：响应（服务端返回给客户端）</font>

```javascript
# 输出
float32 x
float32 y
float32 theta
string name
---
string name
```

    - <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">这个服务使得我们可以在给定的位置和角度生成一只新的乌龟。名字参数是可选的，这里我们不设具体的名字，让turtlesim自动创建一个，运行： $ rosservice call spawn 2 2 0.2 ""</font>
        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">服务返回了新产生的乌龟的名字：   name: turtle2  </font>
2. 使用rosparam

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosparam</font>`<font style="color:rgb(63, 74, 86);">使得我们能够存储并操作ROS [参数服务器（Parameter Server）](</font>[<font style="color:rgb(53, 130, 251);">http://wiki.ros.org/参数服务器（Parameter</font>](http://wiki.ros.org/%E5%8F%82%E6%95%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%88Parameter)<font style="color:rgb(63, 74, 86);"> </font><font style="color:rgb(63, 74, 86);">Server）)上的数据。参数服务器能够存储整型、浮点、布尔、字符串、字典和列表等数据类型。rosparam使用YAML标记语言的语法。一般而言，YAML的表述很自然：</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">1</font>`<font style="color:rgb(63, 74, 86);"> </font><font style="color:rgb(63, 74, 86);">是整型,</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">1.0</font>`<font style="color:rgb(63, 74, 86);"> </font><font style="color:rgb(63, 74, 86);">是浮点型,</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">one</font>`<font style="color:rgb(63, 74, 86);">是字符串,</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">true</font>`<font style="color:rgb(63, 74, 86);">是布尔,</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">[1, 2, 3]</font>`<font style="color:rgb(63, 74, 86);">是整型列表,</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">{a: b, c: d}</font>`<font style="color:rgb(63, 74, 86);">是字典.</font><font style="color:rgb(63, 74, 86);"> </font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosparam</font>`<font style="color:rgb(63, 74, 86);">有很多指令可以用来操作参数，如下所示:</font>

<font style="color:rgb(63, 74, 86);">使用方法:</font>

```javascript
rosparam set            设置参数
rosparam get            获取参数
rosparam load           从文件读取参数
rosparam dump           向文件中写入参数
rosparam delete         删除参数
rosparam list           列出参数名
```

    1. rosparam list

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">参数服务器上都有哪些参数运行： </font><font style="color:rgb(63, 74, 86);background-color:#D8DAD9;">$ rosparam list</font>

<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可以看到turtlesim节点在参数服务器上有3个参数用于设定背景颜色</font>

```bash
/background_b
/background_g
/background_r
/rosdistro
/roslaunch/uris/host_cg__46323
/rosversion
/run_id
```

    2. rosparam set和rosparam get
    - <font style="color:rgb(63, 74, 86);">使用方法:</font>

```bash
rosparam set [param_name]
rosparam get [param_name]
```

        * <font style="color:rgb(63, 74, 86);">现在我们修改背景颜色的红色通道：</font>

```bash
$ rosparam set background_r 150

# 调用清除服务使得修改后的参数生效
$ rosservice call clear
```

        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">现在我们来查看参数服务器上的参数值——获取背景的绿色通道的值：</font>

```bash
$ rosparam get background_g 
#输出
86
```

        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">使用</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosparam get /</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">来显示参数服务器上的所有内容：</font>

```bash
$ rosparam get /
```

			<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777402043983-15a64d27-cf59-4e6d-81b6-73ca815a5968.png)

        * <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">可能希望存储这些信息以备今后重新读取。这通过</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">rosparam</font>`<font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">很容易就可以实现:</font>
    3. <font style="color:rgb(63, 74, 86);background-color:rgb(248, 250, 251);">rosparam dump和rosparam load</font>

<font style="color:rgb(63, 74, 86);">使用方法:</font>

```bash
rosparam dump [file_name]
rosparam load [file_name] [namespace]
```

<font style="color:rgb(63, 74, 86);">现在我们将所有的参数写入params.yaml文件：</font>

```bash
$ rosparam dump params.yaml
```

<font style="color:rgb(63, 74, 86);">你甚至可以将yaml文件重载入新的命名空间，比如说</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">copy</font>`<font style="color:rgb(63, 74, 86);">空间:</font>

```bash
$ rosparam load params.yaml copy
$ rosparam get copy/background_b

#输出
255
```

		<font style="color:rgb(0, 0, 0);">命名空间是 ROS 用来区分同名资源的前缀机制，实现资源分层隔离，避免命名冲突</font>

## <font style="color:rgb(0, 0, 0);">创建ROS消息包和ROS服务</font>
### 消息（msg）和服务（srv）介绍
(1)ROS 消息（Message）是节点间通信的数据单元，定义在.msg文件中，支持基本类型（int32、float64、string等）及嵌套自定义类型。编译后由 catkin 自动生成对应的 C++/Python 头文件供节点调用。

(2) ROS服务（Service）定义在.srv 文件中，由请求（request）和响应（response）两部分组成，以"---"分隔。编译后同样生成对应的接口类，供客户端与服务端使用。

(3)自定义消息/服务需在 package.xml中声明 message_generation 依赖，在 CMakeLists.txt中用add_message_files() / add_service_files()注册，并调用 generate_messages()触发代码生成。

关键命令

l  rosmsg show [消息类型]   查看消息字段定义

l  rossrv show [服务类型]查看服务请求/响应字段

l  catkin_make编译工作空间，生成消息/服务代码

l  rosmsg list  列出所有可用消息类型



6.2编写简单的消息发布器和订阅器（C++）

(1)发布器（Publisher）通过 ros::NodeHandle::advertise<T>() 向指定话题注册发布，返回 Publisher 对象；调用 publish() 发送消息。ros::Rate 控制发布频率，ros::spinOnce() 处理一次回调队列。

(2)订阅器（Subscriber）通过 subscribe() 注册话题与回调函数；ros::spin() 进入阻塞消息循环，持续触发回调直到节点关闭。

(3)两者均需先调用 ros::init() 初始化节点名称，再创建 NodeHandle 作为与 ROS 系统通信的统一接口。消息队列大小（queue_size）决定消息积压时的缓冲上限。



6.1 创建ROS消息和ROS服务

步骤1  在 ROS 工作空间的功能包目录下创建 msg 文件夹，新建自定义消息文件 Num.msg。

步骤2 在 msg/Num.msg 中定义消息字段，修改 package.xml 和 CMakeLists.txt 添加依赖。

步骤3 创建 srv 文件夹，新建 AddTwoInts.srv，定义请求与响应字段。

步骤4 执行 catkin_make 编译，验证消息和服务代码生成成功。

源程序：

```plain
# Num.msg ——自定义消息，包含一个整数字段
int64 num           # 消息数据字段，类型为64位整数

# AddTwoInts.srv ——自定义服务，请求两个整数，返回求和结果
int64 a            # 请求字段：第一个加数
int64 b            # 请求字段：第二个加数
---                # 分隔符，上方为 request，下方为 response
int64 sum          # 响应字段：返回两数之和
```

catkin_make 编译成功截图：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478436901-6ba778a5-6340-47f5-8969-db3c790828b8.png)

rosmsg子命令及rosmsg show所需参数如下图所示：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478431241-3d558868-5b8c-43a0-8dad-154fa468d964.png)

结果分析：catkin_make 编译成功后，在 devel/include 目录下自动生成对应的 C++ 头文件，证明自定义消息/服务定义正确。rosmsg show 命令能正确输出字段，说明 ROS 已识别该消息类型，后续节点可直接引用。

```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}
int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  ros::spin();
  return 0;
}
```

6.2编写简单的消息发布器和订阅器（C++）

步骤1 在功能包 src/ 目录下创建 talker.cpp 和 listener.cpp.

步骤2  CMakeLists.txt中添加add_executable和target_link_libraries，完成编译配置。

步骤 3 执行 catkin_make 编译两个节点。

源程序：

① 信息发布器节点（talker.app)

```plain
#include "ros/ros.h"           //引入 ROS 系统的基础核心头文件
#include "std_msgs/String.h"   //引入标准字符串消息类型的头文件
#include <sstream>             //引入 C++ 字符串流库，用于拼接字符串

int main(int argc, char **argv)
{
// 初始化节点，向 ROS 网络注册此节点的唯一名称为 "talker"
ros::init(argc, argv, "talker");
// 实例化节点句柄，它是该节点与 ROS 主节点(Master)通信的核心接口
ros::NodeHandle n;

// 创建发布器对象 chatter_pub
// 声明要在 "chatter" 这个话题上发布 std_msgs::String 类型的消息
// 参数 1000 是输出队列的大小，防止消息发送过快导致堆积丢包
ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

// 设置循环频率对象，参数 10 代表 10Hz（即每秒执行 10 次）
ros::Rate loop_rate(10);

// 初始化一个计数器变量，用来标记每条消息的序号
int count = 0;

// 开启主循环，ros::ok() 在收到 Ctrl+C 中断信号时会返回 false 退出循环
while (ros::ok())
{
// 实例化一个消息对象 msg，用于装载我们要发送的数据
std_msgs::String msg;

// 使用字符串流对象 ss，将文本 "hello world " 与整数 count 拼接
std::stringstream ss;
ss << "hello world " << count;

// 将拼接好的字符串提取出来，并赋值给消息对象的 data 属性
msg.data = ss.str();

// 将当前发送的消息内容打印在终端上，方便直观查看运行状态
ROS_INFO("%s", msg.data.c_str());

// 核心步骤：调用发布器对象的 publish 函数，将消息广播到话题中
chatter_pub.publish(msg);

// 处理所有挂起的内部回调，保障底层通信的正常运转
ros::spinOnce();

// 调用 sleep 函数进行休眠，精确控制上文设定的 10Hz 发送频率
loop_rate.sleep();

// 计数器自增，准备下一条消息的序号
++count;
}
return 0; // 节点正常结束并退出
}
```



② 消息订阅器节点（listener.cpp)

#include "ros/ros.h"           // 引入 ROS 系统的基础核心头文件

#include "std_msgs/String.h"   // 引入标准字符串消息类型的头文件



// 定义事件回调函数 chatterCallback

// 当底层网络在订阅的话题上接收到新消息时，系统会自动触发执行此函数

// 参数 msg 是一个指向接收到的 String 消息对象的常引用指针

```plain
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
// 通过 msg->data.c_str() 提取消息内部装载的字符串数据
// 使用 ROS_INFO 将接收到的内容打印在当前终端屏幕上
ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
// 初始化节点，向 ROS 网络注册此节点的唯一名称为 "listener"
ros::init(argc, argv, "listener");

// 实例化节点句柄，建立该节点与 ROS 系统的通信连接
ros::NodeHandle n;

// 创建订阅器对象 sub
// 声明订阅名为 "chatter" 的话题，输入队列缓存大小设为 1000
// 将刚才定义的 chatterCallback 函数绑定为该话题的消息处理回调函数
ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

// 开启事件监听死循环
// 该指令会阻塞主线程，使得节点持续保持运行状态以随时接收网络消息
// 一旦接收到新消息，就会立刻跳转执行绑定的回调函数
ros::spin();

return 0; // 节点正常结束并退出
}
```



6.4 测试消息发布器和订阅器

步骤 1 新开终端，确保 roscore 可用并运行

步骤 2 进入 catkin 工作空间，source 环境变量配置文件

步骤 3 运行 talker 节点

步骤 4 保持 roscore 和 talker 运行，新开第三个终端

步骤 5 同样 source 工作空间环境变量后，运行 listener 节点

步骤 6 观察 listener 终端是否实时收到 talker 发布的消息



talker 节点运行,持续输出”hello world”：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478476647-2e6778d1-70b6-4152-978e-906d59484fb4.png)



另一终端运行listener节点，持续输出"I heard: [hello world]" ：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478487780-40601775-4e88-4031-8415-69e2c9f77f8d.png)

## 实现服务和客户端
### 编写简单的服务器和客户端（C++）
### <font style="color:rgb(63, 74, 86);">13.1 编写Service节点</font>
<font style="color:rgb(63, 74, 86);">这里，我们将创建一个简单的service节点("add_two_ints_server")，该节点将接收到两个整形数字，并返回它们的和。</font>

<font style="color:rgb(63, 74, 86);">进入先前你在catkin workspace教程中所创建的beginner_tutorials包所在的目录：</font>

```bash
cd ~/catkin_ws/src/beginner_tutorials
```

<font style="color:rgb(63, 74, 86);">请确保已经按照</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">创建ROS消息和ROS服务</font>`<font style="color:rgb(63, 74, 86);">教程的步骤创建了本教程所需要的srv</font>

#### <font style="color:rgb(63, 74, 86);">13.1.1 代码</font>
<font style="color:rgb(63, 74, 86);">在beginner_tutorials包中创建src/add_two_ints_server.cpp文件，并复制粘贴下面的代码：</font>

```cpp
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"

bool add(beginner_tutorials::AddTwoInts::Request  &req,
         beginner_tutorials::AddTwoInts::Response &res)
{
  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}
```

#### <font style="color:rgb(63, 74, 86);">13.1.2 代码解释</font>
<font style="color:rgb(63, 74, 86);">现在，让我们来逐步分析代码。</font>

```cpp
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
```

`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">beginner_tutorials/AddTwoInts.h</font>`<font style="color:rgb(63, 74, 86);">是由编译系统自动根据我们先前创建的srv文件生成的对应该srv文件的头文件。</font>

```cpp
bool add(beginner_tutorials::AddTwoInts::Request  &req,
         beginner_tutorials::AddTwoInts::Response &res)
```

<font style="color:rgb(63, 74, 86);">这个函数提供两个int值求和的服务，int值从request里面获取，而返回数据装入response内，这些数据类型都定义在srv文件内部，函数返回一个boolean值。</font>

```cpp
{
  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}
```

<font style="color:rgb(63, 74, 86);">现在，两个int值已经相加，并存入了response。然后一些关于request和response的信息被记录下来。最后，service完成计算后返回true值。</font>

```cpp
ros::ServiceServer service = n.advertiseService("add_two_ints", add);
```

<font style="color:rgb(63, 74, 86);">这里，service已经建立起来，并在ROS内发布出来。</font>

### <font style="color:rgb(63, 74, 86);">13.2 编写Client节点</font>
#### <font style="color:rgb(63, 74, 86);">13.2.1 代码</font>
<font style="color:rgb(63, 74, 86);">在beginner_tutorials包中创建src/add_two_ints_client.cpp文件，并复制粘贴下面的代码：</font>

```cpp
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
  beginner_tutorials::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}
```

#### <font style="color:rgb(63, 74, 86);">13.2.1 代码解释</font>
<font style="color:rgb(63, 74, 86);">现在，让我们来逐步分析代码。</font>

<font style="color:rgb(63, 74, 86);"></font>

```cpp
ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
```

<font style="color:rgb(63, 74, 86);">这段代码为</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">add_two_ints</font>`<font style="color:rgb(63, 74, 86);"> </font><font style="color:rgb(63, 74, 86);">service创建一个client。</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">ros::ServiceClient</font>`<font style="color:rgb(63, 74, 86);"> </font><font style="color:rgb(63, 74, 86);">对象待会用来调用service。</font>

```cpp
beginner_tutorials::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
```

<font style="color:rgb(63, 74, 86);">这里，我们实例化一个由ROS编译系统自动生成的service类，并给其request成员赋值。一个service类包含两个成员</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">request</font>`<font style="color:rgb(63, 74, 86);">和</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">response</font>`<font style="color:rgb(63, 74, 86);">。同时也包括两个类定义</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Request</font>`<font style="color:rgb(63, 74, 86);">和</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">Response</font>`<font style="color:rgb(63, 74, 86);">。</font>

```cpp
if (client.call(srv))
```

<font style="color:rgb(63, 74, 86);">这段代码是在调用service。由于service的调用是模态过程（调用的时候占用进程阻止其他代码的执行），一旦调用完成，将返回调用结果。如果service调用成功，</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">call()</font>`<font style="color:rgb(63, 74, 86);">函数将返回true，</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">srv.response</font>`<font style="color:rgb(63, 74, 86);">里面的值将是合法的值。如果调用失败，</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">call()</font>`<font style="color:rgb(63, 74, 86);">函数将返回false，</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">srv.response</font>`<font style="color:rgb(63, 74, 86);">里面的值将是非法的。</font>

### <font style="color:rgb(63, 74, 86);">13.3 编译节点</font>
<font style="color:rgb(63, 74, 86);">再来编辑一下beginner_tutorials里面的CMakeLists.txt，文件位于</font>`<font style="color:rgb(248, 83, 83);background-color:rgb(229, 229, 229);">~/catkin_ws/src/beginner_tutorials/CMakeLists.txt</font>`<font style="color:rgb(63, 74, 86);">，并将下面的代码添加在文件末尾：</font>

```cmake
add_executable(add_two_ints_server src/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server beginner_tutorials_gencpp)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client beginner_tutorials_gencpp)
```

<font style="color:rgb(63, 74, 86);">这段代码将生成两个可执行程序"add_two_ints_server"和"add_two_ints_client"，这两个可执行程序默认被放在你的devel space下的包目录下，默认为~/catkin_ws/devel/lib/share/<package name>。你可以直接调用可执行程序，或者使用rosrun命令去调用它们。它们不会被装在<prefix>/bin目录下，因为当你在你的系统里安装这个包的时候，这样做会污染PATH变量。如果你希望在安装的时候你的可执行程序在PATH变量里面，你需要设置一下install target，请参考：catkin/CMakeLists.txt</font>

<font style="color:rgb(63, 74, 86);">关于CMakeLists.txt文件更详细的描述请参考：catkin/CMakeLists.txt</font>

<font style="color:rgb(63, 74, 86);">现在运行catkin_make命令：</font>

```bash
# In your catkin workspace
cd ~/catkin_ws
catkin_make
```

### 测试运行
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">终端 1：启动 ROS 核心</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">运行</font>

```plain
roscore
```

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">终端 2：启动服务端</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">运行</font>

```plain
source ~/catkin_ws/devel/setup.bash
rosrun beginner_tutorials add_two_ints_server
```

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">终端 3：启动客户端（测试）</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">运行</font>

```plain
source ~/catkin_ws/devel/setup.bash
rosrun beginner_tutorials add_two_ints_client 10 20
```

---

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">结果  
</font><font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">服务端：</font>

```plain
request: x=10, y=20
sending back response: 30
```

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">客户端：</font>

```plain
Sum: 30
```











2. 实验8 录制与回放  
实验步骤1：启动核心程序  
实验步骤2：录制所有话题数据  
实验步骤3：回放 bag 数据  
源代码：  
——bash1——  
roscore #启动ROS核心  
——bash2——  
rosrun turtlesim turtlesim_node #启动小乌龟仿真窗口  
——bash3——  
rosrun turtlesim turtle_teleop_key #启动键盘控制  
——bash4——  
mkdir ~/bagfiles   
cd ~/bagfiles  
rosbag record -a # 开始录制所有话题

——关闭bash3——  
——bash4——  
rosbag play 2026-04-26-08-09-50.bag #回放录制的轨迹

（开始录制）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478053919-419d74de-bf9b-49c7-bb16-c195e2b61a1e.png)

（录制结束，查看bag）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478065195-cb550aca-71a1-4110-9a82-1a49c4f323a1.png)

（开始回放）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478078298-41ba3203-ba5a-4f86-91f7-baaa154d5cc2.png)

（这有个视频）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478089965-e143563b-1ea2-4225-8002-612a39a1cd14.png)  
3. 实验9  
实验步骤1：启动 Gazebo 仿真环境；启动 SLAM 建图节点；启动 RVIZ 可视化；启动键盘控制；保存地图  
实验步骤2：关闭终端 2、3、4，启动 AMCL 导航节点，然后重新启动 RVIZ 导航界面。  
源代码：  
——bash1——  
export TURTLEBOT_GAZEBO_WORLD_FILE="/opt/ros/kinetic/share/turtlebot_gazebo/worlds/playground.world" roslaunch turtlebot_gazebo turtlebot_world.launch  #启动 Gazebo 仿真环境  
——bash2——  
roslaunch turtlebot_gazebo gmapping_demo.launch  #启动 SLAM 建图节点  
——bash3——  
roslaunch turtlebot_rviz_launchers view_navigation.launch #启动 RVIZ 可视化  
——bash4——  
roslaunch turtlebot_teleop keyboard_teleop.launch #启动键盘控制  
——bash5——  
cd /opt/ros/kinetic/share/turtlebot_gazebo/launch/   
rosrun map_server map_saver -f turtlebot_test_map#保存地图  
——关闭bash2,3,4——  
——bash2——  
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/opt/ros/kinetic/share/turtlebot_gazebo/launch/turtlebot_test_map.yaml #启动 AMCL 导航节点  
——bash3——  
roslaunch turtlebot_rviz_launchers view_navigation.launch #重新启动 RVIZ 导航界面

(Gazebo仿真环境)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478118449-4b671443-7543-4f37-8e69-9738e3bf711d.png)

（SLAM建图节点）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478132149-0cc92321-8205-4822-b216-8301d89cc70c.png)

（RVIZ可视化）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478176808-3ec79d7c-0e95-44ec-a361-715d524194f5.png)

（启动键盘控制）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478189035-e92f5242-bc99-4f7b-a822-679d517c3363.png)

（自主导航）（视频2）

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/62803570/1777478234119-eb39f418-97b4-42b7-b2ff-4b99920bc549.png)





```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

int main(int argc, char **argv)
{
    ros::NodeHandle n;
    ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(10);
    int count = 0;
    while (ros::ok())
        {
            /**
     * This is a message object. You stuff it with data, and then publish it.
     */
            std_msgs::String msg;

            std::stringstream ss;
            ss << "hello world " << count;
            msg.data = ss.str();

            ROS_INFO("%s", msg.data.c_str());

            /**
     * The publish() function is how you send messages. The parameter
     * is the message object. The type of this object must agree with the type
     * given as a template parameter to the advertise<>() call, as was done
     * in the constructor above.
     */
            chatter_pub.publish(msg);

            ros::spinOnce();

            loop_rate.sleep();
            ++count;
        }


    return 0;
}
```

```cpp
#include "ros/ros.h"   // 包含ROS核心功能头文件
#include "std_msgs/String.h"  // 包含字符串消息类型，用于发布文本消息
#include <sstream>	// C++字符串流，用于拼接字符串

int main(int argc, char **argv)
{
  // 初始化ROS节点，节点名称：talker
  ros::init(argc, argv, "talker");
  // 创建节点句柄，管理ROS节点的所有资源与通信
  ros::NodeHandle n;
  // 创建发布者：话题名：chatter，消息类型：std_msgs::String，队列长度：1000
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  // 设置循环频率 10Hz（每秒执行10次）
  ros::Rate loop_rate(10);
  int count = 0;
  while (ros::ok()) // ROS主循环：只要节点正常运行，就一直循环
  {
    std_msgs::String msg;  // 创建要发布的消息对象
    std::stringstream ss;	// 创建字符串流，用于拼接消息内容
    ss << "hello world " << count;
    // 将拼接好的字符串赋值给消息的data字段
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    // 发布消息到话题 /chatter
    chatter_pub.publish(msg);
    // 处理一次ROS回调函数（保持节点活跃）
    ros::spinOnce();
    loop_rate.sleep(); // 根据设定的10Hz频率休眠，控制循环速度
    ++count;
  }
  return 0;
}
```

```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"
// 回调函数：当收到chatter话题的消息时，会自动调用这个函数
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  // ROS日志输出，打印收到的消息内容
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}
int main(int argc, char **argv)
{
  // 初始化ROS节点，节点名称：listener
  ros::init(argc, argv, "listener");

  // 创建节点句柄，管理ROS节点的所有资源与通信
  ros::NodeHandle n;
  // 创建订阅者：话题名：chatter，队列长度：1000，回调函数：chatterCallback
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  // 进入ROS主循环，持续监听话题消息，直到节点被关闭
  ros::spin();
  return 0;
}
```

