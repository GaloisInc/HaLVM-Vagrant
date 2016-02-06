#!/bin/sh

VAGRANT=${PWD}/.vagrant
INVENTORY=${VAGRANT}/provisioners/ansible/inventory/vagrant_ansible_inventory

mkdir -p repos/22/x86_64
mkdir -p repos/22/i686
mkdir -p repos/23/x86_64
mkdir -p repos/23/i686
vagrant up
ansible-playbook --inventory-file=${INVENTORY} build-xen-rpms.yml
ansible-playbook --inventory-file=${INVENTORY} build-repo-rpms.yml
