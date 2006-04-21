# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Syslog

Summary: Parse Unix syslog files
Name: perl-Parse-Syslog
Version: 1.03
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-Syslog/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
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
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Parse/
%{perl_vendorlib}/Parse/Syslog.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
