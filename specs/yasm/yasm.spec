# $Id$
# Authority: yury
# Upstream: Discussions about YASM development <yasm-devel$tortall,net>

Summary: Complete rewrite of the NASM assembler
Name: yasm
Version: 1.1.0
Release: 1%{?dist}
License: BSD and (Artistic or GPLv2+ or LGPLv2+) and LGPLv2
Group: Development/Languages
URL: http://www.tortall.net/projects/yasm/

Source: http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: byacc
BuildRequires: xmlto
BuildRequires: gettext-devel

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic.txt AUTHORS BSD.txt COPYING GNU*
%doc %{_mandir}/man1/yasm.1*
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man7/yasm_*.7*
%{_includedir}/libyasm/
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h
%{_libdir}/libyasm.a

%changelog
* Sun Jul 17 2011 Yury V. Zaytsev <yury@shurup.com> - 1.1.0-1
- Updated to release 1.1.0.

* Wed May 19 2010 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Apr 19 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sat Oct 11 2008 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 0.6.0-1
- Update to 0.6.0.
- Remove empty doc files.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.4.0-1
- Initial RPM release.

