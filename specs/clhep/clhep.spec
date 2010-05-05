# $Id$
# Authority: dag
# Upstream: http://savannah.cern.ch/projects/clhep/

%define real_name CLHEP
%define superdir %{_usr}/%{real_name}

Summary: Class library for High Energy Physics
Name: clhep
Version: 2.0.4.5
Release: 1%{?dist}
License: distributable
Group: Development/Libraries
URL: http://proj-clhep.web.cern.ch/proj-clhep/

Source: http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: binutils, gcc-c++, autoconf, automake, make
Obsoletes: CLHEP <= %{version}
Provides: CLHEP = %{version}-%{release}

%description
The CLHEP project was proposed by Leif Lönnblad at CHEP 92. It is intended
to be a set of HEP-specific foundation and utility classes such as random
generators, physics vectors, geometry and linear algebra.

%package devel

Summary: Development files for CLHEP
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Install this package to develop software based on CLHEP.

%prep
%setup -n %{version}/%{real_name}

%build
%configure \
    --includedir="%{_includedir}/CLHEP/" \
    --disable-dependency-tracking \
    --disable-static \
    --enable-exceptions
# if you parallelize the make, badness happens
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

pushd %{buildroot}%{_libdir}
%{__ln_s} -f libCLHEP-g++.%{version}.a libCLHEP.a
popd

### Clean up docs
mkdir doc/
for dir in */doc; do
    %{__rm} -rf $dir/CVS
    %{__mv} -f $dir doc/$(dirname $dir)
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_libdir}/libCLHEP*.so

%files devel
%doc doc/*
%{_bindir}/Cast-config
%{_bindir}/clheplib
%{_bindir}/clhep-config
%{_bindir}/Evaluator-config
%{_bindir}/Exceptions-config
%{_bindir}/GenericFunctions-config
%{_bindir}/Geometry-config
%{_bindir}/Matrix-config
%{_bindir}/Random-config
%{_bindir}/RandomObjects-config
%{_bindir}/RefCount-config
%{_bindir}/Units-config
%{_bindir}/Vector-config
%{_includedir}/CLHEP/
%exclude %{_libdir}/libCLHEP.a

%changelog
* Fri Mar 05 2010 Steve Huff <shuff@vecna.org> - 2.0.4.5-1
- Updated to release 2.0.4.5.
- Fixed typo in doc cleanup script.
- Split off clhep-devel.

* Mon Jun 13 2005 Wei-Lun <chaoweilun@pcmail.com.tw> - 1.8.2.1-1
- Initial spec file created.
