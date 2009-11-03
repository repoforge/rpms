# $Id$
# Authority: dries
# Upstream: David Schweikert <dws$ee,ethz,ch>

Summary: Snort reporting tool
Name: snort-rep
Version: 1.10
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://people.ee.ethz.ch/~dws/software/snort-rep/

Source: http://people.ee.ethz.ch/~dws/software/snort-rep/pub/snort-rep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: perl, perl-MIME-Lite

%description
Snort-rep is a snort reporting tool that can produce text or HTML output
from a syslog file.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 snort-rep %{buildroot}%{_bindir}/snort-rep
%{__install} -Dp -m0755 snort-rep-mail %{buildroot}%{_bindir}/snort-rep-mail

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-2.2
- Rebuild for Fedora Core 5.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.10-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 1.10-1
- first packaging for Fedora Core 1
