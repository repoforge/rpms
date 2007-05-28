# $Id$
# Authority: matthias

Summary: eXtensible ARchiver
Name: xar
Version: 1.5
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
Summary: Development files for xar
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for xar.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LICENSE TODO
%{_bindir}/xar
%{_libdir}/libxar.so.*
%{_mandir}/man1/xar.1*

%files devel
%defattr(-,root,root,-)
%{_includedir}/xar/
%{_libdir}/libxar.so


%changelog
* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sun Feb 25 2007 Matthias Saou <http://freshrpms.net/> 1.4-1
- Initial RPM release.

