# Proposing new packages for inclusion into Flatcar Container Linux

Flatcar Container Linux is a modern Linux distribution for running container workloads.
To stay modern, the packages included need to be kept up-to-date, and sometimes new packages introduced.
This documents explains the process for the latter.

## Project definition

When proposing new packages for inclusion into Flatcar Container Linux, it's important to keep in mind how the project defines itself:  
_Flatcar Container Linux is a fully open source, minimal-footprint, secure by default and always up-to-date Linux distribution for running containers at scale._

## New package criteria

As a minimal Linux distribution, the tools and applications included in Flatcar Container Linux are to be kept to a minimum.
This is to reduce both the image size and attack surface.
Package addition requests are evaluated with this in mind.
Other criteria that are weighed are the following.

- ***Secure by default***: Does the package increase the security of Flatcar?
- ***Always up-to-date***: Is the package actively maintained?
- ***Running containers***: Does the package make Flatcar more relevant for container environments?
- ***At scale***: Does the package improve automation of or telemetry served by Flatcar and/or ease operational burden?

## How to propose a package for inclusion

In order to propose a new package for inclusion, [open an issue using the "New Package Request" template](https://github.com/flatcar/Flatcar/issues/new?assignees=&labels=kind%2Fnew-package&template=new-package-request.md&title=New+Package+Request%3A+%5Bpackage-name%5D).
