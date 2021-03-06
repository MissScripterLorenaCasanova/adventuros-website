---
layout: article
title: "Development Update #16"
---

<p>It&#39;s been a long time since we started working on AdventurOS.<br />
<br />
Before we even made public the concept, it came to life as a Pygame project.<br />
As the project grew bigger, we started adding more content to the little engine and not much later it obviously started to slow down.<br />
Most of you might already know Python/Pygame is not very efficient when it comes to games. That is why we decided to develop it using Game Maker when we launched the indiegogo campaign. We were all familiar with the tool and it was powerful enough to perform the way we had in mind.<br />
By that moment we were using Game Maker 8, so part of the money of the crowdfunding went towards an upgrade of our license to GM:Studio.<br />
The new version of the program, developed by Yoyo Games, was going to allow us to develop a cross platform game. &quot;Code once, run everywhere&quot;, they said.<br />
But reality is when we started coding the nightmare began. &quot;Code once, suck everywhere&quot;.</p>

<p><img alt="" src="http://i.imgur.com/CGrlzMo.png" style="height:336px; width:726px" /></p>

<p>&nbsp;&nbsp; &nbsp;After the fresh installation we noticed several changes in the software.<br />
Some were good, some were bad and some were just TERRIBLE.<br />
AdventurOS&#39; key feature is precisely the indexing of files and folders to generate the levels, monsters and adventures.<br />
While game maker 8 was great at doing this, the newest version GM:S dramatically limited that to only ONE folder per operative system. Adventcalypse.<br />
The documentation about it is very poor and there is no information to be found about OSX or Linux.<br />
The program has a feature to add external libraries as a complement to the engine, but the only external libraries allowed are DLLs which of course don&#39;t work on any other platform than Windows, so there was really nothing we could to to bypass this limitation.<br />
After asking on forums and contacting Yoyogames itself, all we got was pretty much a &nbsp;&quot;Go f**k yourself&quot;.</p>

<p><a href="http://i.imgur.com/jpfkK9e.png"><img alt="" src="http://i.imgur.com/jpfkK9e.png" style="height:336px; width:726px" /></a></p>

<p>&nbsp;&nbsp; &nbsp;By the time we launched the project, the NSA scandal was all over the internet and &nbsp;people were skeptical about us indexing their system.<br />
This meant that using any kind of networking to bypass the limitations of the engine was out of the question.<br />
We refused, and still refuse, to send any package containing the user private information, not even locally. So, there was only one solution left.<br />
We had to create a parallel process with Python in order to gather the information needed and store it as a temporary file on the game&#39;s directory.<br />
Developing that is not as simple as it seems, specially when it is expected to work on all platforms. Right now the indexer is pretty awesome but it was one of the hardest challenges we had to face during the early development of the game.</p>

<p><a href="http://i.imgur.com/lrctV9z.png"><img alt="" src="http://i.imgur.com/lrctV9z.png" style="height:336px; width:726px" /></a></p>

<p><a href="http://i.imgur.com/IsdZnFs.png"><img alt="" src="http://i.imgur.com/IsdZnFs.png" style="height:336px; width:726px" /></a></p>

<p>We have always had modding support in mind.<br />
We designed the source to include many modding capabilities so other people can do whatever they want with the core idea of using the computer as a procedural generator seed. But once again GM got on our way.<br />
From the documentation: &quot;These functions cannot be used any more due to changes in the underlying runner that GameMaker: Studio uses to generate the device specific packages making it impossible to generate objects, images or code &quot;on the fly&quot; as was done before.&quot; This means that all the resources have to be implemented, added and coded from within the GM IDE itself, so there was no way for us to allow any kind of modding without giving away all the game&#39;s source code. We are still looking into ways of doing this but we might have to wait a little bit longer.</p>

<p><a href="http://i.imgur.com/IaDaWw2.png"><img alt="" src="http://i.imgur.com/IaDaWw2.png" style="height:336px; width:726px" /></a></p>

<p>&nbsp;&nbsp; &nbsp;As for the gameplay itself, we are in continuous iteration.<br />
It feels and looks very good, and lately we have been increasing the speed and adding variety to the enemies&#39; IA. The latest additions to the hero&#39;s abilities are the bow and arrow, but there are still some other magic skills ready to be implemented.</p>

<p>&nbsp;&nbsp; &nbsp;We have long wanted to give you this insight on the overall development process of the game since day 1, because there have been so many ups and downs, so many challenges to overcome! We are determined to accomplish our vision and deliver the best AdventurOS we can craft. Thank you for being so awesome!</p>
