# $Id$
# Authority: dries
# Upstream: Michael Schilli <m$perlmeister,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Simple

Summary: Launch and control background processes
Name: perl-Proc-Simple
Version: 1.21
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Simple/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Proc/
%{perl_vendorlib}/Proc/Simple.pm
%dir %{perl_vendorlib}/auto/Proc/
%{perl_vendorlib}/auto/Proc/Simple/

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
