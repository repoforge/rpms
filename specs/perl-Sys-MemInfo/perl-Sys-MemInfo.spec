# $Id$
# Authority: dries
# Upstream: sylvain cresto <scresto%20%5b_at_%5d%20gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-MemInfo

Summary: Get information about memory usage
Name: perl-Sys-MemInfo
Version: 0.4
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-MemInfo/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-MemInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module return the total amount of free and used physical memory
in bytes in totalmem and freemem variables.

%prep
%setup -n %{real_name}

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
%dir %{perl_vendorarch}/Sys/
%{perl_vendorarch}/Sys/MemInfo.pm
%dir %{perl_vendorarch}/auto/Sys/
%{perl_vendorarch}/auto/Sys/MemInfo/

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
