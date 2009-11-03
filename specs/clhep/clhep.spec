# $Id$
# Authority: dag

%define real_name CLHEP

Summary: Class library for High Energy Physics
Name: clhep
Version: 1.8.2.1
Release: 1.2%{?dist}
License: distributable
Group: Development/Libraries
URL: http://proj-clhep.web.cern.ch/proj-clhep/

Source: http://proj-clhep.web.cern.ch/proj-clhep/export/share/CLHEP/1.8.2.1/clhep-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: gcc-c++
Obsoletes: CLHEP <= %{version}
Provides: CLHEP = %{version}-%{release}

%description
The CLHEP project was proposed by Leif Lönnblad at CHEP 92. It is intended
to be a set of HEP-specific foundation and utility classes such as random
generators, physics vectors, geometry and linear algebra.

%prep
%setup -n %{real_name}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__ln_s} -f libCLHEP-g++.%{version}.a %{buildroot}%{_libdir}/libCLHEP.a

### Clean up docs
mkdir doc/
for dir in */doc; do
	%{__rm} -rf $dir/CSV
	%{__mv} -f $dir doc/$(dirname $dir)
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README doc/*
%{_includedir}/CLHEP/
%{_libdir}/*.a

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.2.1-1.2
- Rebuild for Fedora Core 5.

* Mon Jun 13 2005 Wei-Lun <chaoweilun@pcmail.com.tw> - 1.8.2.1-1
- Initial spec file created.
