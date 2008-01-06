# $Id$
# Authority: dag
# Upstream: David Schweikert <david$schweikert,ch>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Syslog

Summary: Parse Unix syslog files
Name: perl-Parse-Syslog
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Syslog/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Unix syslogs are convenient to read for humans but because
of small differences between operating systems and things
like 'last message repeated xx times' not very easy to parse
by a script.

Parse::Syslog presents a simple interface to parse syslog
files: you create a parser on a file (with new) and call
next to get one line at a time with Unix-timestamp, host,
program, pid and text returned in a hash-reference.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Parse::Syslog.3pm*
%dir %{perl_vendorlib}/Parse/
#%{perl_vendorlib}/Parse/Syslog/
%{perl_vendorlib}/Parse/Syslog.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
