# $Id$
# Authority: matthias

Summary: eXtensible ARchiver
Name: xar
Version: 1.5.2
Release: 1
License: BSD
Group: Applications/Archiving
URL: http://code.google.com/p/xar/

Source: http://xar.googlecode.com/files/xar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

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

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc LICENSE TODO
%doc %{_mandir}/man1/xar.1*
%{_bindir}/xar
%{_libdir}/libxar.so.*
%exclude %{_libdir}/libxar.a
%exclude %{_libdir}/libxar.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xar/
%{_libdir}/libxar.so

%changelog
* Tue Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 1.5.2-1
- Updated to release 1.5.2.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 1.5.1-1
- Updated to release 1.5.1.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 1.4-1
- Initial RPM release.

