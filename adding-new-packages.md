# Adding new packages to the Flatcar Linux OS image

Flatcar’s mission statement:
_Flatcar Container Linux is a fully open source, minimal-footprint, secure by default and always up-to-date Linux distribution for running containers at scale._

The tools and applications included in the Flatcar Container Linux OS image are kept to a minimum, to reduce both image size as well as attack surface. Package addition requests are vetted accordingly, and are required to strongly contribute to the other principles in order to be accepted:
- Secure by default: new package increases security. At a minimum the new package must not increase Flatcar’s attack surface.
- Always up-to-date: new package improves Flatcar’s update mechanisms.
- Running containers: new package improves container experience on Flatcar. Includes, but is not limited to, new container runtimes that offer improvements over the ones included with Flatcar.
- At scale: new package improves automation of or telemetry served by Flatcar and/or eases operational burden.

