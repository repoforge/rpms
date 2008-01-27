# $Id$
# Authority: dag

Summary: RPM implementation in python
Name: pyrpm
Version: 0.70
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
* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Tue May 08 2007 Dag Wieers <dag@wieers.com> - 0.69-1
- Updated to release 0.69.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.67-1
- Updated to release 0.67.

* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Wed Feb 07 2007 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Thu Nov 23 2006 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Sun Oct 08 2006 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 0.58-1
- Updated to release 0.58.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 0.57-1
- Updated to release 0.57.

* Mon Jul 31 2006 Dag Wieers <dag@wieers.com> - 0.56-1
- Updated to release 0.56.

* Tue Jul 25 2006 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 0.54-1
- Updated to release 0.54.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 0.53-1
- Updated to release 0.53.

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
