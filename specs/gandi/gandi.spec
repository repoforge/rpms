# $Id$
# Authority: dries
# Upstream: ygrex$mail,ru

Summary: Collection of widgets written in C for ncurses
Name: gandi
Version: 0.5.3
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://y.unlit.org/gandi/

Source: http://dl.sf.net/gandi/gandi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++

%description
GANDI (Gathering of Additional Ncurses Development Implements) is a
collection of widgets written in C for ncurses. It's designed to ease
writing new ncurses software with a user-friendly interface. GANDI is
a library for developers and not an application for end-users.

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
./configure --prefix="%{_prefix}"
%{__perl} -pi -e "s|.*ldconfig.*||g;" Makefile */Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	PREFIX="%{buildroot}%{_prefix}" \
	DOCDIR="%{buildroot}%{_mandir}" \
	LIBDIR="%{buildroot}%{_libdir}/GANDI"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README TODO
%doc %{_mandir}/man3/gandi*
%dir %{_libdir}/GANDI/
%{_libdir}/GANDI/libgandi*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GANDI/
%{_libdir}/GANDI/libgandi*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1
- Initial package.
