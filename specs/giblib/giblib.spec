# $Id: giblib.spec,v 1.1 2004/02/26 16:02:10 thias Exp $

Summary: Simple library and a wrapper for imlib2
Name: giblib
Version: 1.2.3
Release: 3.fr
License: GPL
Group: System Environment/Libraries
Source: http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
URL: http://linuxbrit.co.uk/giblib/
BuildRoot: %{_tmppath}/%{name}-root
Requires: imlib2
BuildRequires: imlib2-devel

%description
giblib is a utility library used by many of the applications from
linuxbrit.co.uk. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2. The wrapper does two things.
It gives you access to fontstyles, which can be loaded from files,
saved to files or defined dynamically through the API. It also,
and more importantly, wraps imlib2's context API.


%package devel
Summary: Static libs and header files for giblib.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Install this package if you intend to develop using the giblib library.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%exclude %{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.2.3-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Feb 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.3.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

