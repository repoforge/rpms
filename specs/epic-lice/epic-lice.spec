# $Id$

# Authority: dag

# Upstream: 

%define rname lice
%define rversion 420pre7

Summary: LiCe IRC scripts for epic.
Name: epic-lice
Version: 4.2.0
Release: 0.pre7
Group: Applications/Communications
License: GPL
URL: http://lice.codehack.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://lice.codehack.com/files/lice/scripts/%{rname}%{rversion}.tar.gz
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
* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 4.2.0-0.pre7
- Initial package. (using DAR)
