# $Id$
# Authority: dries
# Upstream: Fabien Potencier <fabpot$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Stem-Snowball

Summary: Perl interface to Snowball stemmers
Name: perl-Lingua-Stem-Snowball
Version: 0.94
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Stem-Snowball/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Stem-Snowball-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-Module-Build

%description
Perl interface to Snowball stemmers.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Lingua/
%dir %{perl_vendorarch}/Lingua/Stem/
%{perl_vendorarch}/Lingua/Stem/Snowball.pm
#%{_bindir}/add_stemmer.pl
%dir %{perl_vendorarch}/auto/Lingua/Stem/
%{perl_vendorarch}/auto/Lingua/Stem/Snowball/

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Updated to release 0.94.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.93-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.93-1
- Updated to release 0.93.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Updated to release 0.92.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
