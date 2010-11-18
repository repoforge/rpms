# $Id$
# Authority: dag

# ExclusiveDist: el4

%define real_name fcusb2
%define module fcusb2
%define real_version 3.11-07

Summary: dkms package for fcusb2 driver
Name: dkms-fcusb2
Version: 3.11.07
Release: 1
Patch0: fritz-xchg.patch
License: Commercial
Group: System Environment/Kernel
URL: http://www.avm.de/

Source: ftp://ftp.avm.de/cardware/fritzcrdusb.v20/linux/suse.93/fcusb2-suse93-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: dkms

%description
This package contains the fcusb2 driver for AVM GmbH|FritzCard USB 2 Ver. 2.0 ISDN TA.

%prep
%setup -n fritz/src
%patch0 -p2 -b .xchg
# copy the lib in the source tree, do not use some obscure place like /var/lib/fritz
cp ../lib/*.o .
# do not try to copy the lib in LIBDIR
perl -pi -e 's!.*cp -f \.\./lib.*!!' Makefile
# fool Makefile by using a already existing LIBDIR
perl -pi -e 's!(LIBDIR.*):=.*!$1:= \$(SUBDIRS)!' Makefile
#- dkms pass KERNELRELEASE and confuse the Makefile, rely on KERNELVERSION instead
perl -pi -e 's!(ifneq.*)KERNELRELEASE!$1KERNELVERSION!' Makefile
#- build for kernel release dkms is asking for
perl -pi -e 's!shell uname -r!KERNELRELEASE!' Makefile

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/src/fcusb2-%version/
cat > $RPM_BUILD_ROOT/usr/src/fcusb2-%version/dkms.conf <<EOF
PACKAGE_NAME=fcusb2
PACKAGE_VERSION=%version

DEST_MODULE_LOCATION[0]=/kernel/drivers/isdn/capi
BUILT_MODULE_NAME[0]=%module
MAKE[0]="make"
CLEAN="make clean"
AUTOINSTALL="yes"
EOF

tar c . | tar x -C $RPM_BUILD_ROOT/usr/src/%module-%version/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) /usr/src/%module-%version/

%post
set -x
/usr/sbin/dkms --rpm_safe_upgrade add -m %module -v %version 
/usr/sbin/dkms --rpm_safe_upgrade build -m %module -v %version
/usr/sbin/dkms --rpm_safe_upgrade install -m %module -v %version

%preun
set -x
/usr/sbin/dkms --rpm_safe_upgrade remove -m %module -v %version --all


%changelog
* Thu Mar 29 2007 Olivier Blin <oblin@mandriva.com> 3.11.07-2mdv2007.1
+ Revision: 149723
- fix build with 2.6.17 by removing merged atomic_xchg
- use our own make clean not to erase static libraries
- rely on KERNELVERSION instead of EXTRAVERSION which is not exported anymore
- Import dkms-fcusb2

* Wed Sep  8 2004 Olivier Blin <blino@mandrake.org> 3.11.07-1mdk
- initial Mandrake release
