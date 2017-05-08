<H1>﻿Music Video NFO generator for Kodi</H1>

While the TheAudioDB music video scrapper is broken for the Kodi (OSMC) media center, use this python script to generate a local nfo files for your entire music video collection.

<H2>Instruction</H2>

Open kodimvnfo.py with a text editor and change the <i>mypath</i> variable to your main music video directory.

File should be renamed in the format <i>Artist Name - Song Name (Extra Info)</i>. <i>(Extra Info)</i> is optional.

A date parameter can be provided in <i>Extra Info</i> in the format yymmdd or yyyy. The code will automatically find the date entry if multiple parameters is added to <i>Extra Info</i>

Run in terminal >> python kodimvnfo.py

In Kodi, change the Content information provier to "Local information only".
