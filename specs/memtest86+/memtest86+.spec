# $Id$

# Authority: dag
# Upstream: Samuel Demeulemeester <memtest@memtest.org>
# Screenshot: http://www.memtest.org/pics/i875-big.gif

%define _prefix /boot

Summary: Thorough, stand-alone memory tester.
Name: memtest86+
Version: 1.11
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.memtest.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.memtest.org/download/memtest_source_v%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

ExclusiveArch: i386 i486 i586 i686 x86_64

%description
Memtest86+ is a thorough, stand alone memory test for 386, 486, Pentium and
AMD64 systems. Memtest86+ is a stand alone program and can be loaded from
either a disk partition via lilo or a floppy disk. Memtest86+ uses a
"moving inversions" algorithm that is proven to be effective in finding
memory errors. The BIOS based memory test is just a quick check that will
often miss many of the failures that are detected by Memtest86+.

%prep
%setup -n %{name}_v%{version}

%build
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
		--title "Memtest86+ v%{version}"
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
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
