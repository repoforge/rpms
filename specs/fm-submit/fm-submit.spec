# $Id: fm-submit.spec,v 1.2 2004/02/27 17:08:23 driesve Exp $

# Authority: dries

Summary: A script for submitting project updates to freshmeat.net using XML-RPC.
Name: fm-submit
Version: 0.0.5
Release: 2
License: GPL
Group: Development/Tools
URL: http://www.ivarch.com/programs/fm-submit.shtml

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/fm-submit/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
#BuildRequires: 
Requires: perl

%description
fm-submit is a tool to submit project release announcements to freshmeat.net
via XML-RPC, from the command line. Release information is accepted from 
binary packages (RPMs) named in the command line, or from an email-like data 
block on standard input, or from command-line flags.


%description -l nl
fm-submit is een programma dat dient om project release aankondigingen te
versturen naar freshmeat.net via XML-RPC, via de prompt. Release informatie
kan komen van binaire packages (RPMs) als argument op de commandline of via
standaard input of via commandline opties.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
make doc

%install
export DESTDIR=$RPM_BUILD_ROOT
make install

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/fm-submit
/usr/share/man/man1/fm-submit.1.gz

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.0.5-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.0.5-1
- first packaging for Fedora Core 1
