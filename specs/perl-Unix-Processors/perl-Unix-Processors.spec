# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Processors

Summary: Per-processor information
Name: perl-Unix-Processors
Version: 2.041
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Processors/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Processors-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package provides access to per-processor information from Perl.

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
%doc Changes COPYING MANIFEST META.yml README readme.texi
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Processors.pm
%{perl_vendorarch}/Unix/Processors/
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Processors/

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 2.041-1
- Updated to version 2.041.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.034-1
- Updated to latest upstream version { old source not available }

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.033-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.033-1
- Updated to release 2.033.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.032-1
- Updated to release 2.032.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.031-1
- Updated to release 2.031.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.030-1
- Initial package.
