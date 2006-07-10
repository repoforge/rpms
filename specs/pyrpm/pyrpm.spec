# $Id$
# Authority: dag

Summary: RPM implementation in python
Name: pyrpm
Version: 0.52
Release: 1
License: GPL
Group: System Environment/Base
URL: http://people.redhat.com/laroche/pyrpm/

Source: pyrpm-%{version}.tar.bz2
#Source: http://people.redhat.com/laroche/pyrpm/download/pyrpm-%{version}-1.src.rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.3
Requires: python >= 2.3, python-urlgrabber, libxml2-python

%description
PyRPM is a RPM implementation in Python. It can be used to study how rpm based
software management happens. Also tools can build upon it to handle rpm
packages in general e.g. to extract information, check dependancies or even
install packages.

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

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README doc/*.html doc/*.txt
%{_bindir}/*
%{_datadir}/pyrpm/
%ghost %{_datadir}/pyrpm/*/*.pyo


%changelog
* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.52-1
- Updated to release 0.52.

* Tue Jun 29 2006 Dag Wieers <dag@wieers.com> - 0.51-1
- Updated to release 0.51.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Tue May 23 2006 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 0.45-1
- Initial package (using DAR)
