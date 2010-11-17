# $Id$
# Authority: dag
# Upstream: Mark Shelor <mshelor$cpan,org>

### EL6 ships with perl-Digest-SHA-5.47-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-SHA

Summary: Perl extension for SHA-1/224/256/384/512
Name: perl-Digest-SHA
Version: 5.48
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.003
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.003

%description
Digest-SHA Perl module

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man1/shasum.1*
%doc %{_mandir}/man3/Digest::SHA.3pm*
%{_bindir}/shasum
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/SHA/
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/SHA.pm

%changelog
* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 5.48-1
- Updated to version 5.48.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 5.47-1
- Updated to release 5.47.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 5.45-1
- Updated to release 5.45.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 5.44-1
- Updated to release 5.44.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 5.43-1
- Updated to release 5.43.

* Sun Jan 15 2005 Dag Wieers <dag@wieers.com> - 5.32-1
- Initial package. (using DAR)
