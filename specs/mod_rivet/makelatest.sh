#!/bin/sh

# get filename of latest snapshot
LATEST_TARBALL=`wget -q -O- http://cvs.apache.org/snapshots/tcl-rivet/ | grep tar.gz | tail -1 | cut -d\" -f 6`

# validate the name as a sanity check
if ! echo $LATEST_TARBALL | egrep -q '^tcl-rivet_[0-9]*.tar.gz$'; then
    echo Unable to query filename of latest Rivet snapshot.
    exit 1
fi
echo Latest Rivet snapshot is: $LATEST_TARBALL

# extract just the timestamp portion
LATEST_TIMESTAMP=`echo $LATEST_TARBALL | cut -d'_' -f2 | cut -d'.' -f1`

# update the spec file to use the new timestamp
sed "s/^%define rivet_snapshot .*/%define rivet_snapshot $LATEST_TIMESTAMP/" < mod_rivet.spec > mod_rivet.spec.new
if [ -s mod_rivet.spec.new ]; then
    mv mod_rivet.spec.new mod_rivet.spec
else 
    echo Failed to update the spec version number.
    exit 1
fi

# download the new tarball, if needed.
if [ ! -f ~/rpmbuild/SOURCES/$LATEST_TARBALL ]; then
    wget -O ~/rpmbuild/SOURCES/$LATEST_TARBALL http://cvs.apache.org/snapshots/tcl-rivet/$LATEST_TARBALL
fi

# actually do the build
echo "You can now run:  rpmbuild -bb mod_rivet.spec"
