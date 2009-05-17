# $Id$
# Authority: dag
# Upstream: Theo Schlossnagle <jesus$omniti,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MersenneTwister
%define real_version 1.0

Summary: Perl extension for a Mersenne Twister PRGN implementation with context
Name: perl-MersenneTwister
Version: 1.0.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MersenneTwister/

Source: http://www.cpan.org/authors/id/J/JE/JESUS/MersenneTwister-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl extension for a Mersenne Twister PRGN implementation with context.

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
%doc ChangeLog README
%doc %{_mandir}/man3/Rand::MersenneTwister.3pm*
%dir %{perl_vendorarch}/auto/Rand/
%{perl_vendorarch}/auto/Rand/MersenneTwister/
%dir %{perl_vendorarch}/Rand/
%{perl_vendorarch}/Rand/MersenneTwister.pm

%changelog
* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
