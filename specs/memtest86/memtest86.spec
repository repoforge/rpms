# $Id$

# Authority: dag
# Upstream: Chris Brady <bugs@memtest86.com>

%define _prefix /boot
%define rversion 3.1a

Summary: Thorough, stand alone memory test.
Name: memtest86
Version: 3.1
Release: 0.a
License: GPL
Group: System Environment/Kernel
URL: http://www.memtest86.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.memtest86.com/memtest86-%{rversion}.tar.gz
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
%setup -n %{name}-%{rversion}

%build
#%{?rh80:CC="gcc296"} %{?rh90:CC="gcc296"} %{?rhel3:CC="gcc296"} %{?rhfc1:CC="gcc296"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_prefix}
%{__install} -m644 memtest.bin %{buildroot}%{_prefix}/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x /sbin/grubby ] ; then
        /sbin/grubby --add-kernel="%{_prefix}/%{name}-%{version}" \
		--title "Memtest86 v%{version}"
fi

%postun
if [ -x /sbin/grubby ] ; then
        /sbin/grubby --remove-kernel="%{_prefix}/%{name}-%{version}"
fi

%files
%defattr(-, root, root, 0755)
%doc README
%{_prefix}/%{name}-%{version}/

%changelog
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
