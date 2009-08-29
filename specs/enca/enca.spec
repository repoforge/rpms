# $Id$
# Authority: dries

Summary: Charset and encoding analyser
Name: enca
Version: 1.10
Release: 1
License: GPL
Group: Applications/Text
URL: http://gitorious.org/enca

Source: http://dl.cihar.com/enca/enca-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings.

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
%configure \
	--disable-dependency-tracking \
	--disable-external \
	--disable-gtk-doc \
	--disable-static \
	--without-librecode
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__mv} -f %{buildroot}%{_datadir}/gtk-doc/html/ rpm-docs/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL README THANKS* TODO
%doc %{_datadir}/man/man1/enca.1*
%doc %{_datadir}/man/man1/enconv.1*
%{_bindir}/enca
%{_bindir}/enconv
%{_libdir}/libenca.so.*
%exclude %{_libexecdir}/enca/

%files devel
%defattr(-, root, root, 0755)
%doc README.devel devel-docs/html/*.html
%{_includedir}/enca.h
%{_libdir}/libenca.so
%{_libdir}/pkgconfig/enca.pc
%exclude %{_libdir}/libenca.la

%changelog
* Sat Aug 29 2009 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Fri Jun 08 2007 Dag Wieers <dag@wieers.com> - 1.9-4
- Build without recode, removed recode requirement.
- Removed %%{_libexecdir} and static library.
- Added enca-devel docs.

* Sun Dec 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.9-3
- Made a devel subpackage.

* Sun Dec 18 2005 Dries Verachtert <dries@ulyssis.org> 1.9-1
- Update to release 1.9.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> 1.8-1
- Update to release 1.8.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 1.7-1
- Update to release 1.7.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 1.6-1
- update to 1.6

* Thu May 20 2004 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to 1.4

* Sun Feb 29 2004 Dries Verachtert <dries@ulyssis.org> 1.3-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
