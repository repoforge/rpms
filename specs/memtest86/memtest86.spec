# $Id$
# Authority: dag
# Upstream: Chris Brady <bugs$memtest86,com>

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Thorough, stand alone memory test
Name: memtest86
Version: 3.5
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.memtest86.com/

Source: http://www.memtest86.com/memtest86-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386
ExclusiveOS: Linux

%description
Memtest86 is a thorough, stand alone memory test for 386, 486 and Pentium
systems. Memtest86 is a stand alone program and can be loaded from either
a disk partition via lilo or a floppy disk. Memtest86 uses a "moving
inversions" algorithm that is proven to be effective in finding memory
errors.  The BIOS based memory test is just a quick check that will often
miss many of the failures that are detected by Memtest86.

%prep
%setup

%build
#%{?rh8:CC="gcc296"} %{?rh9:CC="gcc296"} %{?el3:CC="gcc296"} %{?fc1:CC="gcc296"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m644 memtest.bin %{buildroot}/boot/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x /sbin/grubby ] ; then
    /sbin/grubby --add-kernel="/boot/%{name}-%{version}" \
        --title "Memtest86 v%{version}"
fi

%postun
if [ -x /sbin/grubby ] ; then
    /sbin/grubby --remove-kernel="/boot/%{name}-%{version}"
fi

%files
%defattr(-, root, root, 0755)
%doc README
/boot/%{name}-%{version}

%changelog
* Sat Feb 21 2009 Dag Wieers <dag@wieers.com> - 3.5-1
- Updated to release 3.5.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 3.4-1
- Updated to release 3.4.

* Sun Jun 24 2007 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Fri Dec 31 2004 Dag Wieers <dag@wieers.com> - 3.2-1
- Updated to release 3.2.

* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 3.1-1.a
- Fixed the location of the memtest kernel. (Greg Cope)

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 3.1-0.a
- Updated to release 3.1a.

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 3.0-1
- Changes for Red Hat 8.0

* Mon Aug 19 2002 Dag Wieers <dag@wieers.com> - 3.0-0
- Moved to 3.0 and use grubby

* Tue Jul 17 2001 Dag Wieers <dag@wieers.com> - 2.7-0
- Moved to 2.7

* Sun Jun 17 2001 Dag Wieers <dag@wieers.com> - 2.6-0
- Moved to 2.6

* Mon Oct 12 1999 Dag Wieers <dag@wieers.com> - 2.0-0
- Moved to 2.0

* Mon Jun 22 1998 Peter Soos <sp@osb.hu> - 1.4-0
- Moved to 1.4

* Wed Dec 31 1997 Peter Soos <sp@osb.hu>
- Initial version
