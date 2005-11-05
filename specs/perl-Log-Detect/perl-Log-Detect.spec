# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Detect

Summary: Detect errors in log files
Name: perl-Log-Detect
Version: 1.420
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Detect/

Source: http://search.cpan.org/CPAN/authors/id/W/WS/WSNYDER/Log-Detect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package provides two modules, Log::Detect and Log::Delayed.
Log::Detect allows for GREPing a log file for error messages, and
reporting the results in a summary form.  Log::Delayed delays error
messages until all have been encountered, which is useful for parsers
and such that do not want to exit on the first error.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/vtrace
%{perl_vendorlib}/Log/Detect.pm
%{perl_vendorlib}/Log/Delayed.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.420-1
- Updated to release 1.420.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.415-1
- Initial package.
