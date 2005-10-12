# $Id$

# Authority: dries
# Upstream: Roderick Schertler <roderick$argon,org>


%define real_name String-ShellQuote
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Quote a string for passing through a shell
Name: perl-String-ShellQuote
Version: 1.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-ShellQuote/

Source: http://www.cpan.org/modules/by-module/String/String-ShellQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_bindir}/shell-quote
%{_mandir}/man3/*
%{_mandir}/man1/*
%{perl_vendorlib}/String/ShellQuote.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
