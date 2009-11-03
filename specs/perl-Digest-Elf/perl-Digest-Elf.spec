# $Id$
# Authority: dries
# Upstream: Steve McKay <mckay$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-Elf

Summary: Extension for generating ElfHash values
Name: perl-Digest-Elf
Version: 1.4
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-Elf/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-Elf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Digest::Elf provides an XS based implimentation of the ElfHash algorithm.
What's that get ya? ElfHash generates resonably 32 bit integer value
from a string in a reasonably short period of time. The actual algorith
was culled from a Dr. Dobbs Journal article and they culled it, I think,
from the source for the GNU c complier. If you know better, please let
me know.

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
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/Elf.pm
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/Elf/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
