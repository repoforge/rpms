# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Map8

Summary: Unicode-Map8 (Mapping table between 8-bit chars and Unicode) module for perl
Name: perl-Unicode-Map8
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Map8/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Map8-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Unicode-Map8 (Mapping table between 8-bit chars and Unicode) module for perl.

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
%doc Changes MANIFEST README map8_bin2txt rfc1345.txt
%doc %{_mandir}/man1/umap.1*
%doc %{_mandir}/man3/Unicode::Map8.3pm*
%{_bindir}/umap
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Map8/
%{perl_vendorarch}/Unicode/Map8.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Map8/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Cosmetic cleanup.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR)
