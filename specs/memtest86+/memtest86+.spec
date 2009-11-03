# $Id$
# Authority: dag
# Upstream: Samuel Demeulemeester <memtest$memtest,org>

# Screenshot: http://www.memtest.org/pics/i875-big.gif

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_stackprotector 1}
%{?el3:%define _without_stackprotector 1}
%{?rh9:%define _without_stackprotector 1}
%{?rh7:%define _without_stackprotector 1}
%{?el2:%define _without_stackprotector 1}

%define _prefix /boot

Summary: Thorough, stand-alone memory tester
Name: memtest86+
Version: 4.00
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.memtest.org/

Source: http://www.memtest.org/download/%{version}/memtest86+-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 i486 i586 i686 x86_64

%description
Memtest86+ is a thorough, stand alone memory test for 386, 486, Pentium and
AMD64 systems. Memtest86+ is a stand alone program and can be loaded from
either a disk partition via lilo or a floppy disk. Memtest86+ uses a
"moving inversions" algorithm that is proven to be effective in finding
memory errors. The BIOS based memory test is just a quick check that will
often miss many of the failures that are detected by Memtest86+.

%prep
%setup

%{?_without_stackprotector:%{__perl} -pi.orig -e 's|-fno-stack-protector||' Makefile}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 memtest.bin %{buildroot}%{_prefix}/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x /sbin/grubby ] ; then
  /sbin/grubby --add-kernel="%{_prefix}/%{name}-%{version}" \
    --title "Memtest86+ v%{version}"
fi

%postun
if [ -x /sbin/grubby ] ; then
  /sbin/grubby --remove-kernel="%{_prefix}/%{name}-%{version}"
fi

%files
%defattr(-, root, root, 0755)
%doc README
%{_prefix}/%{name}-%{version}

%changelog
* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 4.00-1
- Updated to release 4.00.

* Tue Dec 23 2008 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release 2.11.

* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Tue May 27 2008 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Wed Jan 17 2007 Dag Wieers <dag@wieers.com> - 1.70-1
- Updated to release 1.70.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.65-1
- Updated to release 1.65.

* Thu Feb 10 2005 Dag Wieers <dag@wieers.com> - 1.50-1
- Updated to release 1.50.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Thu Nov 04 2004 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
