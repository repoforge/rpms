# $Id: $

# Authority: dries
# Upstream: 

Summary: General-purpose tool for parameter handling in C++
Name: xparam
Version: 1.22
Release: 1
License: GPL+Other
Group: Applications/
URL: http://xparam.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/xparam/xparam-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, automake, autoconf, libtool

%description
XParam is a general-purpose tool for parameter handling in C++. 
It allows object serialization and deserialization in a format that is
human-readable and -writeable, and is unaffected by issues of word-size and
endianity. The XParam format is also not confused by objects containing
pointers: it saves the objects in such a manner that their conceptual
contents can be restored perfectly. 

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
%{__aclocal}
%{__autoconf}
# {__automake} --add-missing
%configure --disable-config-examples
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO BUGS XPARAM-VERSION doc
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/xparam*

%files devel
%{_includedir}/xparam/*.h
%{_includedir}/*.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Tue May 11 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
