# $Id$
# Authority: dries
# Upstream: Geoff Hutchison <geoff$geoffhutchison,net>

Summary: Convert between file formats used in molecular modeling chemistry
Name: openbabel
Version: 1.100.2
Release: 1
License: GPL
Group: Development/Libraries
URL: http://openbabel.sourceforge.net/

Source: http://dl.sf.net/openbabel/openbabel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Open Babel is a project designed to pick up where Babel left off, 
as a cross-platform program and library designed to interconvert 
between many file formats used in molecular modeling and computational 
chemistry.

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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/babel
%{_bindir}/obfit
%{_bindir}/obgrep
%{_bindir}/obrotate
%{_libdir}/libopenbabel.so.*
%{_datadir}/openbabel

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/openbabel
%{_libdir}/pkgconfig/openbabel.pc
%{_libdir}/libopenbabel.a
%{_libdir}/libopenbabel.so
%exclude %{_libdir}/libopenbabel.la

%changelog
* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> - 1.100.2-1
- Initial package.
