# $Id$

# Authority: dag

Summary: Mobile phone tools.
Name: gammu
Version: 0.94.0
Release: 1
License: GPL
Group: Applications/Communications
URL: http://www.mwiacek.com/gsm/gammu/gammu.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mwiacek.com/zips/gsm/gammu/older/gammu-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: bluez-libs-devel

%description
Gammu can do such things with cellular phones as making data calls,
updating the address book, changing calendar and ToDo entries, sending and
receiving SMS messages, loading and getting ring tones and pictures (different
types of logos), synchronizing time, enabling NetMonitor, managing WAP
settings and bookmarks and much more. Functions depend on the phone model.

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

%{__perl} -pi.orig -e '
		s|^(port) =.*$|$1 = /dev/ttyS0|;
		s|^(connection) =.*$|$1 = dlr3|;
		s|||;
	' docs/examples/config/gammurc

%build
%configure \
	--enable-cb \
	--enable-7110incoming
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} installlib \
	DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%{__install} -m0644 docs/examples/config/gammurc %{buildroot}%{_sysconfdir}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%files
%defattr(-, root, root, 0755)
%doc changelog copying readme.txt docs/examples/ docs/docs/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/gammurc
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/gammu/

%files devel
%defattr(-,root,root)
%doc docs/develop/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/gammu/
%{_libdir}/pkgconfig/*.pc

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Mar 05 2004 Dag Wieers <dag@wieers.com> - 0.94.0-1
- Updated to release 0.94.0.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.93.0-1
- Added BuildRequires for bluez-libs-devel. (Soós Péter)

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.93.0-0
- Initial package. (using DAR)
