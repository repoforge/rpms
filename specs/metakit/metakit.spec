# $Id$
# Authority: matthias
# Upstream: <metakit@equi4.com>

Summary: Embeddable database
Name: metakit
Version: 2.4.9.3
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.equi4.com/metakit/
Source: http://www.equi4.com/pub/mk/metakit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, tcl

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
%setup


%build
pushd unix
    %configure
    %{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
pushd unix
    %{__make} install DESTDIR=%{buildroot}
popd


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/*.so

%files devel
%defattr(-, root, root, 0755)
%doc CHANGES WHATSNEW doc
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.a


%changelog
* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 2.4.9.3-2
- Rebuild for Fedora Core 2.

* Sun May 16 2004 Matthias Saou <http://freshrpms.net/> 2.4.9.3-1
- Updated to release 2.4.9.3.

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 2.4.9.2-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.9.2.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release, based on PLD spec file.

