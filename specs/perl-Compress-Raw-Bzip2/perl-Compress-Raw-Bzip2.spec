# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Raw-Bzip2

Summary: Low-Level Interface to bzip2 compression library
Name: perl-Compress-Raw-Bzip2
Version: 2.031
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Raw-Bzip2/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%filter_from_requires /^perl*/d
%filter_setup

%description
Low-Level Interface to bzip2 compression library.

%prep
%setup -q -n %{real_name}-%{version}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Compress::Raw::Bzip2.3pm*
%dir %{perl_vendorarch}/auto/Compress/
%dir %{perl_vendorarch}/auto/Compress/Raw/
%{perl_vendorarch}/auto/Compress/Raw/Bzip2/
%dir %{perl_vendorarch}/Compress/
%dir %{perl_vendorarch}/Compress/Raw/
%{perl_vendorarch}/Compress/Raw/Bzip2.pm

%changelog
* Thu Sep 23 2010 David Hrbáč <david@hrbac.cz> - 2.031-1
- new upstream release

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 2.024-1
- Updated to version 2.024.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.023-1
- Updated to version 2.023.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 2.021-1
- Updated to version 2.021.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 2.020-1
- Updated to version 2.020.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.015-1
- Updated to release 2.015.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.011-1
- Updated to release 2.011.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.010-1
- Updated to release 2.010.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.009-1
- Updated to release 2.009.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.006-1
- Updated to release 2.006.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 2.005-1
- Updated to release 2.005.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
