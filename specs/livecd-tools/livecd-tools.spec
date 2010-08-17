# $Id$
# Authority: dag

# ExclusiveDist: el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name livecd

Summary: Tools for building live CDs
Name: livecd-tools
Version: 014
Release: 8%{?dist}
License: GPL
Group: System Environment/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd

Source0: livecd-tools-%{version}.tar.gz
Source1: livecd-iso-to-pxeboot.sh
Patch1: livecd-creator.python24.patch
Patch2: livecd-creator.xen.patch
Patch3: livecd-mayflower.pxeboot.patch
Patch4: livecd-mayflower.cdbus.patch
Patch5: livecd-tools.libata.support.patch
Patch6: livecd-creator.extlinux.patch
Patch7: livecd-tools.checkisomd5.patch
Patch8: livecd-creator.restorecon.patch
Patch9: livecd-creator.isomd5sum.patch
Patch10: livecd-creator.mayflowerconf.patch
Patch11: livecd-creator.syslinux.patch
Patch12: livecd-creator.mkisofs.patch
Patch13: livecd-creator.typo.patch
Patch15: livecd-tools.persistent-overlay.patch
Patch16: livecd-creator.terminfo.patch
Patch17: livecd-creator.minimal-dev.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python
Requires: anaconda-runtime
Requires: coreutils
#Requires: dosfstools >= 2.11-8
Requires: dosfstools >= 2.11
Requires: e2fsprogs
#Requires: isomd5sum
Requires: mkisofs
#Requires: pykickstart >= 0.96
Requires: pykickstart >= 0.43
Requires: squashfs-tools
Requires: util-linux
Requires: yum >= 3.1.7
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc ppc64
Requires: yaboot
%endif

%description 
Tools for generating live CD's on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%prep
%setup -n %{real_name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/livecd-iso-to-pxeboot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HACKING README
%{_bindir}/image-creator
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_datadir}/livecd-tools/
%{_prefix}/lib/livecd-creator/
%dir %{python_sitelib}/imgcreate/
%{python_sitelib}/imgcreate/*.py
%{python_sitelib}/imgcreate/*.pyc
%{python_sitelib}/imgcreate/*.pyo

%changelog
* Fri Mar 12 2010 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-8
- Remove selinux patch as it prevented building a LiveCD with selinux in a different state than enforcing

* Wed Oct 28 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-7
- Fix typo in creator.py
- Fix "selinux --disabled"
- Add the persistence feature (persistent overlay) - thanks to Douglas McClendon
- Add terminfo bits to live initrd
- Create a minimal /dev instead of bind mounting the host's /dev

* Tue Oct 27 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-6
- Fix livecd-iso-to-pxeboot.sh script: new location for pxelinux.0
- Fix livecd-mayflower.pxeboot.patch: don't worry if $thingtomount is a regular file

* Fri Sep 11 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-5
- Add -T option to mkisofs. This should make the LiveCD compatible with 
  non-Rock Ridge capable systems.

* Fri Aug 28 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-4
- Make sure livecd-creator is compatible with newer syslinux releases

* Tue Aug 25 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-3
- Ensure md5sum implantation is optionnal (patch from Ron Yorston)
- Keep /etc/mayflower.conf file after initrd creation

* Wed Aug 19 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-2
- Fix how restorecon is called

* Tue Aug 18 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 014-1
- Updating to 014
- Migrating required patches
- Adding patch for xen (https://bugzilla.redhat.com/show_bug.cgi?id=470564)
- Adding patch for extlinux from EPEL
- Fix path for checkisomd5 in iso-to-disk utility (patch taken from EPEL)

* Tue Apr 07 2009 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 013-9
- Add sd[a-z] to mayflower init's CDLABEL udev rules (patch submitted by Brandon Davidson)
- Add support for libata (patch submitted by Brandon Davidson)
- Add support for append option in kickstart file (patch submitted by Brandon Davidson)

* Fri Jun 27 2008 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 013-8
- Change "Network Installation" option -> text mode installation by default

* Wed Jun 25 2008 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 013-7
- Apply patch to add text mode (runlevel 3) option at boot time 

* Tue Jun 10 2008 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 013-6
- Apply patch from Rene Plattner to mount correctly pxeboot images created from 
  the livecd-iso-to-pxeboot utility 

* Mon Mar 10 2008 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 013-5
- Add livecd-iso-to-pxeboot from livecd-tools-015

* Fri Dec 22 2007 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 0.13-4
- Add "Network Installation" option at boot time

* Fri Nov 30 2007 Patrice Guay <patrice.guay@nanotechnologies.qc.ca> - 0.13-3
- Rebuild for CentOS 5
- Requires pykickstart >= 0.96
- CentOS 5 does not provide isomd5sum (requires a newer anaconda)
- Add a patch to remove incompatible python syntax (try, except, finally) 
- Add a patch to avoid calling YumBase close module
- Add a patch to avoid lvm error

* Mon Oct 29 2007 Jeremy Katz <katzj@redhat.com> - 013-1
- Lots of config updates
- Support 'device foo' to say what modules go in the initramfs
- Support multiple kernels being installed
- Allow blacklisting kernel modules on boot with blacklist=foo
- Improve bootloader configs
- Split configs off for f8

* Tue Sep 25 2007 Jeremy Katz <katzj@redhat.com> - 012-1
- Allow %%post --nochroot to work for putting files in the root of the iso
- Set environment variables for when %%post is run
- Add progress for downloads (Colin Walters)
- Add cachedir option (Colin Walters)
- Fixes for ppc/ppc64 to work again
- Clean up bootloader config a little
- Enable swaps in the default desktop config
- Ensure all configs are installed (#281911)
- Convert method line to a repo for easier config reuse (jkeating)
- Kill the modprobe FATAL warnings (#240585)
- Verify isos with iso-to-disk script
- Allow passing xdriver for setting the xdriver (#291281)
- Add turboliveinst patch (Douglas McClendon)
- Make iso-to-disk support --resetmbr (#294041)
- Clean up filesystem layout (Douglas McClendon)
- Manifest tweaks for most configs

* Tue Aug 28 2007 Jeremy Katz <katzj@redhat.com> - 011-1
- Many config updates for Fedora 8
- Support $basearch in repo line of configs; use it
- Support setting up Xen kernels and memtest86+ in the bootloader config
- Handle rhgb setup
- Improved default fs label (Colin Walters)
- Support localboot from the bootloader (#252192)
- Use hidden menu support in syslinux
- Have a base desktop config included by the other configs (Colin Walters)
- Use optparse for optino parsing
- Remove a lot of command line options; things should be specified via the
  kickstart config instead
- Beginnings of PPC support (David Woodhouse)
- Clean up kernel module inclusion to take advantage of files in Fedora
  kernels listing storage drivers

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 010-1
- Separate out configs used for Fedora 7
- Add patch from Douglas McClendon to make images smaller
- Add patch from Matt Domsch to work with older syslinux without vesamenu
- Add support for using mirrorlists; use them
- Let livecd-iso-to-disk work with uncompressed images (#248081)
- Raise error if SELinux requested without being enabled (#248080)
- Set service defaults on level 2 also (#246350)
- Catch some failure cases
- Allow specifying tmpdir
- Add patch from nameserver specification from Elias Hunt

* Wed May 30 2007 Jeremy Katz <katzj@redhat.com> - 009-1
- miscellaneous live config changes
- fix isomd5 checking syntax error

* Fri May  4 2007 Jeremy Katz <katzj@redhat.com> - 008-1
- disable screensaver with default config
- add aic7xxx and sym53c8xx drivers to default initramfs
- fixes from johnp for FC6 support in the creator
- fix iso-to-stick to work on FC6

* Tue Apr 24 2007 Jeremy Katz <katzj@redhat.com> - 007-1
- Disable prelinking by default
- Disable some things that slow down the live boot substantially
- Lots of tweaks to the default package manifests
- Allow setting the root password (Jeroen van Meeuwen)
- Allow more specific network line setting (Mark McLoughlin)
- Don't pollute the host yum cache (Mark McLoughlin)
- Add support for mediachecking

* Wed Apr  4 2007 Jeremy Katz <katzj@redhat.com> - 006-1
- Many fixes to error handling from Mark McLoughlin
- Add the KDE config
- Add support for prelinking
- Fixes for installing when running from RAM or usb stick
- Add sanity checking to better ensure that USB stick is bootable

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-3
- have to use excludearch, not exclusivearch

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-2
- exclusivearch since it only works on x86 and x86_64 for now

* Wed Mar 28 2007 Jeremy Katz <katzj@redhat.com> - 005-1
- some shell quoting fixes
- allow using UUID or LABEL for the fs label of a usb stick
- work with ext2 formated usb stick

* Mon Mar 26 2007 Jeremy Katz <katzj@redhat.com> - 004-1
- add livecd-iso-to-disk for setting up the live CD iso image onto a usb 
  stick or similar

* Fri Mar 23 2007 Jeremy Katz <katzj@redhat.com> - 003-1
- fix remaining reference to run-init

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 002-1
- update for new version

* Fri Dec 22 2006 David Zeuthen <davidz@redhat.com> - 001-1%{?dist}
- Initial build.

