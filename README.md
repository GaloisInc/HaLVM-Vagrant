# HaLVM Vagrant / Ansible Archive

This repository is designed as a place for storing various vagrant / ansible /
etc. files for working with the HaLVM. We strongly encourage pull requests! We
want the HaLVM to be easy to develop with, wherever you develop your machines.
So if you've got a new box you think would be fun to include, throw it in!

## Recent Changes

 * *December 7th, 2016*: Fedora 25 added.

## Using these images for developing HaLVMs

These are perfect images for developing HaLVMs for your own purposes. You have
`sudo` access to start and stop virtual machines, and all the tools we use
already installed. In addition, we've set up networking for you, which is
sometimes half the battle in setting up a HaLVM development system.

These systems are also set up to draw from the main HaLVM repositories, as
available, so that with a simple `dnf update` you can have the latest and
greatest versions of the HaLVM and Xen.

## Using these images for developing the HaLVM

We should note that these are also great platforms for working on the HaLVM
itself. You will have to pull down the HaLVM tree and build it yourself, but
most of the tools should be there, as well as everything you need to test your
modifications.

## Fedora vs Ubuntu

We strongly suggest using Fedora builds unless you have a strong affinity for
Ubuntu; Fedora is what we primarily use at HaLVM HQ, so it tends to be better
tested. In addition, we haven't quite found a good way to do automatic updates
for Ubuntu like we do for Fedora; it isn't nearly as easy to get Ubuntu's PPA
system to work for us as it is to run `createrepo`.

## Other Systems

We welcome other operating system images, as well. Please submit a pull request
with your favorite. Amongst other things, this makes it much easier for us to
keep your platform up-to-date, as well!
