# $Id$
# Authority: matthias

Summary: Extensible Binary Meta Language library
Name: libebml
Version: 0.7.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.matroska.org/
Source: http://dl.matroska.org/downloads/libebml/libebml-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
This library is used for I/O operations in the Extensible Binary Meta Language
(EBML), which is a kind of binary version of XML.


%package devel
Summary: Development files for the Extensible Binary Meta Language
Group: Development/Libraries
# Static lib, no main package (yet)
#Requires: %{name} = %{version}

%description devel
This library is used for I/O operations in the Extensible Binary Meta Language
(EBML), which is a kind of binary version of XML.

This package contains the files required to rebuild applications which will
use the Extensible Binary Meta Language.


%prep
%setup
# Fix mode for this text file
%{__chmod} -x ChangeLog


%build
# No autotools...
%{__make} -C make/linux %{?_smp_mflags} DEBUGFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} -C make/linux install \
    libdir=%{buildroot}%{_libdir} \
    includedir=%{buildroot}%{_includedir}/ebml


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


# No files for now, as there is only a static library
#files
#defattr(-, root, root, 0755)

%files devel
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.LGPL
%{_includedir}/ebml/
%{_libdir}/*.a


%changelog
* Tue Aug  3 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Thu Jul  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Initial RPM release.

