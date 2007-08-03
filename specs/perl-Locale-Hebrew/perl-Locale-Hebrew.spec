# $Id$
# Authority: dag
# Upstream: ☺唐鳳☻ <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Hebrew

Summary: Perl module for bidirectional Hebrew support
Name: perl-Locale-Hebrew
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Hebrew/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Hebrew-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Locale-Hebrew is a Perl module for bidirectional Hebrew support.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Locale::Hebrew.3pm*
%dir %{perl_vendorarch}/Locale/
%{perl_vendorarch}/Locale/Hebrew.pm
%dir %{perl_vendorarch}/auto/Locale/
%{perl_vendorarch}/auto/Locale/Hebrew/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
