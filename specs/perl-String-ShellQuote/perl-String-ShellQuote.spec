# $Id$
# Authority: dries
# Upstream: Roderick Schertler <roderick$argon,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-ShellQuote

Summary: Quote a string for passing through a shell
Name: perl-String-ShellQuote
Version: 1.03
Release: 2.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-ShellQuote/

Source: http://www.cpan.org/modules/by-module/String/String-ShellQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_bindir}/shell-quote
%{_mandir}/man3/String::ShellQuote.3pm*
%{_mandir}/man1/shell-quote.1*
%dir %{perl_vendorlib}/String/
%{perl_vendorlib}/String/ShellQuote.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-2.2
- Rebuild for Fedora Core 5.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 1.03-2
- Rebuild due to problematic 1.03-1 builds. (Dean Takemori)

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
