# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Map8

Summary: Unicode-Map8 (Mapping table between 8-bit chars and Unicode) module for perl
Name: perl-Unicode-Map8
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Map8/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Unicode-Map8-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Unicode::String) >= 2
Requires: perl(Unicode::String) >= 2

%filter_from_requires /^perl*/d
%filter_setup

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
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Cosmetic cleanup.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR)
