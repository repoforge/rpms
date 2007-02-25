# $Id$
# Authority: matthias

%{?fc2:%define _without_gettextdevel 1}
%{?fc1:%define _without_gettextdevel 1}
%{?el3:%define _without_gettextdevel 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh7:%define _without_gettextdevel 1}
%{?el2:%define _without_gettextdevel 1}
%{?el2:%define _without_xmlto 1}

Summary: Complete rewrite of the NASM assembler
Name: yasm
Version: 0.6.0
Release: 1
License: BSD
Group: Development/Languages
URL: http://www.tortall.net/projects/yasm/
Source: http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bison, byacc

%{!?_without_xmlto:BuildRequires:xmlto}
%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}


%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.


%package devel
Summary: Header files and static libraries for yasm
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.
Install this package if you need to rebuild applications that use yasm.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc Artistic.txt AUTHORS BSD.txt COPYING GNU*
%{_bindir}/yasm
#%{_libdir}/*.so.*
#%dir %{_libdir}/yasm/
#%{_libdir}/yasm/*.so
%{_mandir}/man1/yasm.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libyasm/
%{_includedir}/libyasm-stdint.h
%{_includedir}/libyasm.h
%{_libdir}/libyasm.a
#%exclude %{_libdir}/*.la
#%{_libdir}/*.so
#%dir %{_libdir}/yasm/
#%{_libdir}/yasm/*.a
#%exclude %{_libdir}/yasm/*.la
%{_mandir}/man7/yasm_*.7*


%changelog
* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 0.6.0-1
- Update to 0.6.0.
- Remove empty doc files.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.4.0-1
- Initial RPM release.

