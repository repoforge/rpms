# $Id$

# Authority: dag

Summary: Library to access GSM mobile phones through GSM modems
Name: gsmlib
Version: 1.10
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.pxh.de/fs/gsmlib/

Source: http://www.pxh.de/fs/gsmlib/download/gsmlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
Obsoletes: libgsm-ext <= %{version}
Provides: libgsm-ext

%description
This distribution contains a library to access GSM mobile phones
through GSM modems. Features include: modification of phonebooks
stored in the mobile phone or on the SIM card, reading and writing
of SMS messages stored in the mobile phone, sending and reception
of SMS messages.

Additionally, some simple command line programs are provided to use
these functionalities.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/FAQ doc/README.NLS ext/README.sieme
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/README.developers
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/gsmlib/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-0.2
- Rebuild for Fedora Core 5.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.10-0
- Initial package. (using DAR)
