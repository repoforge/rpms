# $Id: $

# Authority: dries

# Far from finished, not to be released :)

Summary: A far from finished attempt of a buildserver in python
Name: pydar
Version: 0.001
Release: 1
License: GPL
Group: Development/Tools
URL: NoUrlYet

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: pydar-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

%description
Not finished, not to be released!

%prep
%setup -n pydar

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-master
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-slave
%{_bindir}/dar-remote
%{_datadir}/pydar/*.py
%{_datadir}/pydar/pydar/*.py

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
