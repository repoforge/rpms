# $Id: metakit.spec,v 1.1 2004/02/26 17:57:39 thias Exp $

Summary: Embeddable database
Name: metakit
Version: 2.4.9.2
Release: 3.fr
License: GPL
Group: System Environment/Libraries
URL: http://www.equi4.com/metakit/
Source: http://www.equi4.com/pub/mk/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++, tcl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MetaKit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms. It lets you build applications which
store their data efficiently, in a portable way, and which will not
need a complex runtime installation. In terms of the data model,
MetaKit takes the middle ground between RDBMS, OODBMS, and flat-file
databases - yet it is quite different from each of them.


%package devel
Summary: Header files and development documentation for metakit
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Header files and development documentation for metakit.


%prep
%setup -q

%build
cd unix
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd unix
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README
%{_libdir}/*.so

%files devel
%defattr(-, root, root)
%doc CHANGES MetaKit.html WHATSNEW doc
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.a

%changelog
* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 2.4.9.2-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.9.2.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release, based on PLD spec file.

