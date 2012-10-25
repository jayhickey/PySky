PySky
====

PySky is a short Python script that uses the [Dark Sky API] to display precipitation data. It displays this data in natural English language across multiple time periods:

    NOW
    Rain, 44° F

    NEXT HOUR 
    Rain for 45 min

    FOLLOWING 3 HRS
    Moderate rain

    NEXT 24 HRS 
    Moderate chance of rain

PySky also creates a plot image of the precipitation intensity for the next hour:

![](https://raw.github.com/jayhickey/PySky/master/img/ds-rain-1.png)

## Requirements


### Matplotlib


PySky uses the [matplotlib] library for plotting. If you'd rather not install it, run `pysky_noplot.py` instead, which doesn't include the plot routine and will only output the text descriptions.

Because of matplotlib's many dependencies, it can be a tricky to install on OS X. Use Chris Fonnesbeck's [Scipy Superpack] if you want to avoid the headache. The script makes installing matplotlib really easy—just make sure you already have Xcode 4.5 and the associated command line tools installed.


### Dark Sky API Key

In order to retrieve any data from Dark Sky, you first need an API key. You can [register as a developer] for free and get one. Then  just create a `.darksky` file in your home directory (~/.darksky) and add this line, replacing `123456789abcdefg` with your 32 character key:

    APIkey: 123456789abcdefg

## Running The Script ##

Change line 80

    plt.savefig('/Volumes/MacHD/Projects/darksky-scripts/ds-rain-1.png', dpi=220, \

to a local path where you'd to save the plot image.

Run PySky with the following command:

    python pysky.py {{Latitude}} {{Longitude}}

Where `{{Latitude}}` and  `{{Longitude}}` are the desired Latitude and Longitude coordinates (in decimal form) of your location. If either or both are missing, a default location of the Apple Store in Cincinnati, OH is used. 

[This tool] is handy for converting your address to coordinates.

## PySky on the Desktop with Geektool ##

[GeekTool] is my favorite way to use PySky. It allows you to have Dark Sky right on your desktop, just like this:

![](https://raw.github.com/jayhickey/PySky/master/img/desktop-1.png)

Download GeekTool from the [App Store], install it, then drag two "Geeklets" onto your desktop—one "Shell" and one "Image". 

Click on the Shell Geeklet and enter the Python run command in the "command" field. For example:

    /usr/local/bin/python /Volumes/MacHD/Projects/darksky-scripts/pysky.py {{Latitude}} {{Longitude}}

**Note:** If you installed matplotlib into your default Python interpreter make sure to use `usr/local/bin/python` instead of just `python`, or else the module won't load. GeekTool doesn't create a shell environment exactly like you see when running terminal. Specifically, it doesn’t load any of the `.profile`, `.bash_rc`, or `.bash_profile` startup files.

Next, choose the Image Geeklet, and set the `URL:` field to `file://localhost` + the plot image local path. Like this:

    file://localhost/Volumes/MacHD/Projects/darksky-scripts/ds-rain-1.png

Set the refresh time for both the image and shell script to whatever you like. Just don't make it <20 seconds or so—you'll hit the daily 10,000 API call limit. I personally have both refresh every two minutes.

[App Store]:https://itunes.apple.com/us/app/geektool/id456877552
[GeekTool]:https://itunes.apple.com/us/app/geektool/id456877552
[my Blog]:http://jayhickey.com
[register as a developer]:https://developer.darkskyapp.com/
[matplotlib]:https://github.com/matplotlib/matplotlib
[Dark Sky API]:https://developer.darkskyapp.com/
[this tool]:http://stevemorse.org/jcal/latlon.php
[Scipy Superpack]:http://fonnesbeck.github.com/ScipySuperpack/
