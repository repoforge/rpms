# $Id$
# Authority: dag
# Upstream: Marcus Holland-Moritz <mhx$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-Binary-C

Summary: Binary Data Conversion using C Types
Name: perl-Convert-Binary-C
Version: 0.70
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-Binary-C/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-Binary-C-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Binary Data Conversion using C Types.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man1/ccconfig.1*
%doc %{_mandir}/man3/Convert::Binary::C.3pm*
%doc %{_mandir}/man3/Convert::Binary::C::Cached.3pm*
#%%doc %%{_mandir}/man3/*.3pm*
%{_bindir}/ccconfig
%dir %{perl_vendorarch}/auto/Convert/
%dir %{perl_vendorarch}/auto/Convert/Binary/
%{perl_vendorarch}/auto/Convert/Binary/C/
%dir %{perl_vendorarch}/Convert/
%dir %{perl_vendorarch}/Convert/Binary/
%{perl_vendorarch}/Convert/Binary/C/
%{perl_vendorarch}/Convert/Binary/C.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.69-1
- Updated to release 0.69.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.68-1
- Initial package. (using DAR)
