# $Id$
# Authority: dag
# Upstream:

%define real_name lice
%define real_version 420pre7

Summary: LiCe IRC scripts for epic
Name: epic-lice
Version: 4.2.0
Release: 0.pre7.2%{?dist}
Group: Applications/Communications
License: GPL
URL: http://lice.codehack.com/

Source: http://lice.codehack.com/files/lice/scripts/%{real_name}%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires:
Requires: epic

%description
LiCe is a FREE ircii script written by srfrog for the original and
EPIC irc clients. It has been on circulation since circa 1992 and
continues to be used by many people in different countries.

It is distributed under the GNU Public License.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.2.0-0.pre7.2
- Rebuild for Fedora Core 5.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 4.2.0-0.pre7
- Initial package. (using DAR)
