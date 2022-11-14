# Emulator 

Status: `PAUSED`

## Background

The problem with physical devices is issues with scaling.
We're limited by the number of devices that we can run and scrape data from at any given instance.

For this reason, emulators are a good choice to run ads on.

The 2 biggest ones I came across are  GenyMotin and BlueStacks.

Bluestacks' core audience is people who want to play android games on PCs, so not all apps are supported out the box along with limited support options.

GenyMotion is a better choice since you can run arm based apps on a x86 arch. You can also

The goal is to run airtest scripts on a genymotion emulator, just like running code on a real device.


## Setup

Install virtualbox

Install genymotion

Install airtest

Install ADB

Copy over the adb from airtest into your machine's adb (otherwise there is a version mismatch)

Start an emulator in genymotion

Run `adb devices -l` in terminal and you should see the genymotion emulator

Start airtest and you should see the android emulator in device window (if the adb setup was successfull)


## Problems 

1. Airtest and Genymotion don't play nicely

The adb causes issues when airtest tries to trigger it.

Under the hood airtest uses a library called minicap. Which is used to record screen movements, emulate user input and take screenshots. Since minicap was originally intended for real devices, support for emulators is an after thought for them.

2. Arm -> x86 translations only exist for android v4-v8 (currently v11).

This isn't too big of a deal for now, since many apps still support at least v8 for their apps. But eventually this might be a bottleneck as more people move on to newer devices and support for older device versions cools down.


## Solutions

Try to figure out a version of minicap that works for both airtest and genymotion. There isn't any documentation out there so this is more of a hit/miss scneario. Just test out all permutations of versions by airtest and genymotion.

Wait until more support is added (What I am doing right now). Re-visit this issue in the future, and perhaps use another emulator all together.


## References

1. [Genymotion ARM translations](https://github.com/m9rco/Genymotion_ARM_Translation)
2. [Minicap Error](https://github.com/openstf/minicap/issues/65)
3. [Airtest Bug](https://github.com/AirtestProject/AirtestIDE/issues/947)