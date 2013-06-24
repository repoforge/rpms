# $Id$
# Authority: dries
# Upstream: Folkert Van Heusden <folkert$vanheusden,com>

Summary: Console RSS reader
Name: rsstail
Version: 1.8
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.vanheusden.com/rsstail/

Source: http://www.vanheusden.com/rsstail/rsstail-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libmrss-devel >= 0.16, curl-devel

%description
RSSTail is more or less an RSS reader. It monitors an RSS feed, and if it
detects a new entry, it will emit only that new entry.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%{__install} rsstail %{buildroot}%{_bindir}/rsstail

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/rsstail

%changelog
* Mon Jun 24 2013 David Hrbáč <david@hrbac.cz> - 1.8-1
- new upstream release

* Thu Jan  1 2009 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sun Dec 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Fri May 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Updated to release 1.1.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sun Dec 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
