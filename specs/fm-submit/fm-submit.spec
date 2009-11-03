# $Id$

# Authority: dries

Summary: Script for submitting project updates to freshmeat.net using XML-RPC
Name: fm-submit
Version: 0.0.5
Release: 2.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.ivarch.com/programs/fm-submit.shtml

Source: http://dl.sf.net/fm-submit/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
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
%setup

%build
%{__make} doc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/fm-submit
%{_mandir}/man1/fm-submit.1.gz

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.5-2.2
- Rebuild for Fedora Core 5.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.0.5-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.0.5-1
- first packaging for Fedora Core 1

