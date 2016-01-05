#!/bin/sh

mkdir -p upstream
sshfs uhsure.com:webapps/halvm_fedora upstream
cp -rv repos/* upstream/
createrepo -d upstream/22/i686
createrepo -d upstream/22/x86_64
createrepo -d upstream/23/i686
createrepo -d upstream/23/x86_64
