# $Id$
# Authority: dries
# Upstream:  Simon Josefsson <simon$josefsson,org>

Summary: Recover DNS zonefiles using the DNS protocol
Name: walker
Version: 3.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://josefsson.org/walker/

Source: http://josefsson.org/walker/releases/walker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires:

%description
DNSSEC Walker is a tool to recover DNS zonefiles using the DNS protocol.
The server does not have to support zonetransfer, but the zone must contain
DNSSEC "NXT" or "NSEC" records. Optionally, it can also verify DNSSEC
signatures on the RRsets within the zone.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%{__install} walker %{buildroot}%{_bindir}/walker
%{__gzip} walker.1
%{__install} walker.1.gz %{buildroot}%{_mandir}/man1/walker.1.gz

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING index.html README
%doc %{_mandir}/man?/walker*
%{_bindir}/walker

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.8-1.2
- Rebuild for Fedora Core 5.

* Tue Sep 21 2005 Dries Verachtert <dries@ulyssis.org> - 3.8-1
- Updated to release 3.8.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 3.7-1
- Initial package.
