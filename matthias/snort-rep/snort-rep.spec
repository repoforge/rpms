# $Id: snort-rep.spec,v 1.1 2004/03/01 10:49:07 driesve Exp $

# Authority: dries

Summary: A snort reporting tool.
Summary(nl): Een programma dat rapporten maakt van snort logs.
Name: snort-rep
Version: 1.10
Release: 2
License: GPL
Group: Applications/Internet
URL: http://people.ee.ethz.ch/~dws/software/snort-rep/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://people.ee.ethz.ch/~dws/software/snort-rep/pub/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Requires: perl, perl-MIME-Lite

%description
Snort-rep is a snort reporting tool that can produce text or HTML output
from a syslog file.

%description -l nl
Snort-rep is een programma on snort rapporten te maken in tekst of HTML aan
de hand van een syslog bestand.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
echo nothing to do

%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p ${DESTDIR}/usr/bin
cp snort-rep-mail snort-rep ${DESTDIR}/usr/bin

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/snort-rep
%{_bindir}/snort-rep-mail

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.10-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.10-1
- first packaging for Fedora Core 1
