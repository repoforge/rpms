# $Id: $

# Authority: dries
# Upstream:

%define real_name String-ShellQuote
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Quote a string for passing through a shell
Name: perl-String-ShellQuote
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-ShellQuote/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/String-ShellQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/String/ShellQuote.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
