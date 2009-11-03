# $Id$
# Authority: dag
# Upstream: Sun Wu <sw$cs,arizona,edu>, Udi Manber <udi$cs,arizona.edu>

Summary: Search with approximate matching capabilities
Name: agrep
Version: 2.04
Release: 1.2%{?dist}
Group: Applications/Text
License: Redistributable for non-profit use
URL: http://www.tgries.de/agrep/

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
%{__install} -Dp -m0755 agrep %{buildroot}%{_bindir}/agrep
%{__install} -Dp -m0644 agrep.1 %{buildroot}%{_mandir}/man1/agrep.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc agrep.algorithms agrep.chronicle contribution.list COPYRIGHT README
%doc %{_mandir}/man1/agrep.1*
%{_bindir}/agrep

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 2.04-1
- Initial package. (using DAR)
