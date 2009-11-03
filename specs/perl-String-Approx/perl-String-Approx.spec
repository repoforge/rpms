# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Approx

Summary: Perl extension for approximate matching (fuzzy matching)
Name: perl-String-Approx
Version: 3.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Approx/

Source: http://www.cpan.org/modules/by-module/String/String-Approx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The most important change was that the underlying algorithm was
changed completely.  Instead of doing everything in Perl using regular
expressions we now do the matching in C using the so-called Manber-Wu
k-differences algorithm shift-add.  You have met this algorithm if you
have used the agrep utility or the Glimpse indexing system.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/Approx.pm
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/Approx

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 3.26-1
- Updated to release 3.26.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 3.25-1
- Updated to release 3.25.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 3.24-1
- Initial package.
