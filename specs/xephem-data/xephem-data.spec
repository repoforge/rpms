# $Id$
# Authority: dries

# still work in progress
# Tag: rft

# Dist: nodist

Summary: Data files for xephem
Name: xephem-data
Version: 3.7.2
Release: 1%{?dist}
License: GPL
Group: Applications/Scientific
URL: http://www.clearskyinstitute.com/xephem/xephem.html

Source: v3.4-catalogs.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: xephem

%description
TODO
Data files for xephem.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/xephem/catalogs
%{__install} *.edb %{buildroot}%{_datadir}/xephem/catalogs/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_datadir}/xephem/catalogs/
%{_datadir}/xephem/catalogs/*.edb

%changelog
* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.2-1
- Initial package.
