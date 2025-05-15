# OSC Timestamps and Forward Synchronization in Python and Pure Data

In this workshop, we will learn about the OSC protocol and how it can be used to mitigate latency and control musical systems from afar. Specifically, the session concentrates on how we can use OSC timestamps in Python and Pure Data to Forward Synchronize audio playback in two remote places at once. Over four steps, you will develop a custom synchronization scheme using OSC and a technique called Forward Synchronization between Python and Pure Data. The goal is to learn more about how to set up and configure advanced technologies for networked music systems and synchronous online musical collaboration.

**NB!** This workshop requires an intermediate familiarity with OSC for Python and Pure Data.

## Dependencies

- [ Python 3x](https://www.python.org/downloads/)

  ```
  pip install playsound==1.2.2
  pip install python-osc
  ```

- [Pure Data Vanilla 0.54](https://puredata.info/downloads/pure-data)
  - I recommend that you install the 32-bit version of Pure Data vanilla (if possible) for mrpeach to work best.
  - Download the [mrpeach](https://github.com/pd-externals/mrpeach) library

## Preperation

Schmeder, & Freed, A. (2008). Implementation and applications of open sound control timestamps. ICMC. http://cnmat.berkeley.edu/publications/implementation-and-applications-open-sound-control-timestamps

Andrew Schmeder. (2010). Best Practices for Open Sound Control. Center for New Music and Audio Technologies (CNMAT), UC Berkeley. https://opensoundcontrol.stanford.edu/files/osc-best-practices-final.pdf


## Additional Resources

- [Python Speech recognition with OSC network communication (dispatchers, threading server, clients, etc.)](https://www.youtube.com/watch?v=T3jd-894Ar4)
- [OSC Official Homepage](https://opensoundcontrol.stanford.edu/index.html)
- [AbletonOSC](https://github.com/ideoforms/AbletonOSC)
