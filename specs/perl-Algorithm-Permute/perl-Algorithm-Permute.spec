# $Id$
# Authority: dries
# Upstream: Edwin Pratomo <epratomo$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Permute

Summary: Fast permutation
Name: perl-Algorithm-Permute
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Permute/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Permute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Handy and fast permutation with object oriented interface.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Algorithm::Permute.3pm*
%dir %{perl_vendorarch}/auto/Algorithm/
%{perl_vendorarch}/auto/Algorithm/Permute/
%dir %{perl_vendorarch}/Algorithm/
%{perl_vendorarch}/Algorithm/Permute.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
