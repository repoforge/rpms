# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-LZF

Summary: Extremely light-weight Lev-Zimpel-Free compression
Name: perl-Compress-LZF
Version: 3.43
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-LZF/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-LZF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small (no
large library to be pulled in). It is also free, so there should be no
problems incoporating this module into commercial programs.

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
%doc COPYING COPYING.Artistic COPYING.GNU Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Compress::LZF.3pm*
%dir %{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/auto/Compress/LZF/
%dir %{perl_vendorarch}/Compress/
%{perl_vendorarch}/Compress/LZF.pm

%changelog
* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 3.43-1
- Updated to version 3.43.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 3.41-1
- Updated to release 3.41.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 3.11-1
- Updated to release 3.11.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.1-1
- Updated to release 3.1.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Updated to release 1.6.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
