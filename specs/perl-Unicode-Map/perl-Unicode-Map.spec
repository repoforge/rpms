# $Id$
# Authority: dag
# Upstream: Martin Schwartz <martin$nacho,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Map

Summary: Unicode-Map (Maps charsets from and to UTF16 unicode) module for perl
Name: perl-Unicode-Map
Version: 0.112
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Map/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Map-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Unicode-Map (Maps charsets from and to UTF16 unicode) module for perl.

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
%doc COPYING Changes INSTALL MANIFEST README
%doc %{_mandir}/man1/map.1*
%doc %{_mandir}/man1/mkmapfile.1*
%doc %{_mandir}/man3/Unicode::Map.3pm*
%{_bindir}/map
%{_bindir}/mirrorMappings
%{_bindir}/mkCSGB2312
%{_bindir}/mkmapfile
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Map/
%{perl_vendorarch}/Unicode/Map.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Map/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.112-1
- Cosmetic cleanup.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.112-0
- Initial package. (using DAR)
