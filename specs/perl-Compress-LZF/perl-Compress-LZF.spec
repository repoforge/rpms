# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-LZF

Summary: Extremely light-weight Lev-Zimpel-Free compression
Name: perl-Compress-LZF
Version: 1.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-LZF/

Source: http://www.cpan.org/modules/by-module/Compress/Compress-LZF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING COPYING.Artistic COPYING.GNU Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Compress::LZF.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Compress/
%{perl_vendorarch}/Compress/LZF.pm
%dir %{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/auto/Compress/LZF/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Updated to release 1.6.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
