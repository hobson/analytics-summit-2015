% title: Data Analytics War Stories
% subtitle: Predictive Analytics Innovation Summit
% subtitle: San Diego, CA
% subtitle: <i><small>February 19-20, 2015</small></i>
% author: <a href="https://github.com/hobson">Hobson Lane</a><a href="https://twitter.com/hobsonlane">@hobsonlane</a>
% copyright: Sharp Laboratories of America
% thankyou: Thank you <a href="https://www.sharplabs.com">Sharp Labs!</a>
% thankyou_details: for being <strong>awesome</strong> by contributing to open source...
% contact: PDX Python's <a href="https://github.com/pug/pug">pug</a>
% contact: Steven Bird's <a href="https://github.com/nltk">nltk</a>
% contact: Mike Bostock's <a href="http://d3js.org">D3</a>
% favicon: http://hobson.github.com/analytics-summit-2015/favicon.ico

---
title: Hobson Lane

*Principal Data Scientist, Sharp Laboratories of America*

Hobson and his data analytics teammates are transforming the way business decisions are made at SHARP, using data to reveal new opportunities and revamp existing business strategies. Hobson brings 20 years of innovation and data analytics experience in a variety of roles and industries:  Section Head at Northrop Grumman, Quant for a Point Clear Capital, Visualization Developer at Squishy Media, Chief Data Scientist at Building Energy, and now Principal Data Scientist at Sharp Labs. Hobson will share data analytics war stories where billions of dollars of spacecraft hardware were saved and lost, and millions of dollars in returned consumer electronics were eliminated.

---
title: War Story #1
subtitle: $1.5B Asset in Hangs in the Balance

* Imagine yourself in the operations center for a $1.5B satellite
* A launch system failure has caused your satellite to tumble out of control
* Dozens of computer monitors around streaming telemetry
* As the Control System expert you must:

    1. Figure out what the data says about the satellite's motion and health
    2. Get it under control
    3. Save it before the atmosphere drags it down to the Earth

(diagram of fireball reentry)

<footer>True Story</footer>

---
title: Not So Fast

* Your gut says to turn on the "Reaction Wheel" to get sensors pointed better
* Your gut is often wrong when complex dynamics are at play
* Your simulation (predictive analytics) are wrong
* The wheel will crash and destroy the satellite if you spin it too fast
* Your team discovers your error before catastrophy

<footer>True story</footer>

---
title: Key Piece of Data

* The solar panels are oscillating in voltage so we're tumbling... fast 
* How Fast?
  - The data says it's twice as fast as what our gut says
  - You educate the team on something called "aliasing"
  - You prevent thruster burns that would have made things worse
* Corrected thruster burns save the satellite

<footer>Do the math before any big decision</footer>

---
title: War Story #2

* Our TV return rate is increasing rapidly? Why?
* What is the right denomenator (sales unit count) for each numerator (returns)

* Information Theoretic approach would produce the most accurate answer
* Sales team "rule of thumb" is much easier to explain and almost as accurate
  - Calculate the average sales "lag" to normalize the returns by
  - Aggregate report compares dealers, models, geographic locations, dates, etc

(demo or video of a typical query and lag calculation)

<footer>Do the math before any big decision</footer>

---
title: The Team

* Hobson Lane, Prinipal Data Scientist, Sharp Labs
    * <laneh@sharplabs.com>
* John Kowalski, Department Manager, Sharp Labs
    * <kowalskj@sharplabs.com>
* Steve Walker, Data Guru, Sharp Labs
    * <walkers@sharplabs.com>
* Rono Mathieson, VP, Sharp Labs
    * <rono@sharplabs.com>
* LiZhong Zheng, Professor, MIT
    * <lizhong@MIT.edu>


