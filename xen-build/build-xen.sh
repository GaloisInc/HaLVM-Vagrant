#!/bin/sh

VAGRANT=${PWD}/.vagrant
INVENTORY=${VAGRANT}/provisioners/ansible/inventory/vagrant_ansible_inventory

mkdir -p repos
vagrant up
ansible-playbook --inventory-file=${INVENTORY} build-xen-rpms.yml
