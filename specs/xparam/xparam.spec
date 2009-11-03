# $Id$
# Authority: dries

Summary: General-purpose tool for parameter handling in C++
Name: xparam
Version: 1.22
Release: 1.2%{?dist}
License: GPL+Other
Group: System Environment/Libraries
URL: http://xparam.sourceforge.net/

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
%configure \
	--disable-config-examples
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot (cannot be just excluded for rh8)
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
/sbin/ldconfig 2>/dev/null
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig 2>/dev/null

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING doc INSTALL README TODO XPARAM-VERSION
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/*.info*
%{_includedir}/xparam/*.h
%{_includedir}/*.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Tue May 11 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
