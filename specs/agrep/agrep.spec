# $Id$
# Authority: dag
# Upstream: Sun Wu <sw$cs,arizona,edu>, Udi Manber <udi$cs,arizona.edu>

Summary: Search with approximate matching capabilities
Name: agrep
Version: 2.04
Release: 1
Group: Applications/Text
License: Redistributable for non-profit use
URL: http://www.tgries.de/agrep/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gd.tuwien.ac.at/utils/admin-tools/agrep/agrep-%{version}.tar.Z
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description 
agrep is similar to egrep (or grep or fgrep), but it is
much more general and usually faster.

%prep
%setup 

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 agrep %{buildroot}%{_bindir}/agrep
%{__install} -D -m0644 agrep.1 %{buildroot}%{_mandir}/man1/agrep.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc agrep.algorithms agrep.chronicle contribution.list COPYRIGHT README
%doc %{_mandir}/man1/agrep.1*
%{_bindir}/agrep

%changelog
* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 2.04-1
- Initial package. (using DAR)
