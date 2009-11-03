# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Detect

Summary: Detect errors in log files
Name: perl-Log-Detect
Version: 1.424
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Detect/

Source: http://www.cpan.org/modules/by-module/Log/Log-Detect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

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
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.424-1
- Updated to version 1.424.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.422-1
- Updated to release 1.422.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.421-1
- Updated to release 1.421.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.420-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.420-1
- Updated to release 1.420.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.415-1
- Initial package.
