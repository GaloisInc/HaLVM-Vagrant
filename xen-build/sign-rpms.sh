#!/bin/sh

RPMS=`find repos -name "*rpm"`
rpm --resign ${RPMS}
