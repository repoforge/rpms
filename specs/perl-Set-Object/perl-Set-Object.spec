# $Id$
# Authority: dries
# Upstream: Sam Vilain <sam$vilain,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-Object

Summary: Set of objects and strings
Name: perl-Set-Object
Version: 1.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Object/

Source: http://www.cpan.org/modules/by-module/Set/Set-Object-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This modules implements a set of objects, that is, an unordered
collection of objects without duplication.

The term *objects* is applied loosely - for the sake of Set::Object,
anything that is a reference is considered an object.

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
%doc Changes.pod MANIFEST META.yml README
%doc %{_mandir}/man3/Set::Object.3pm*
%doc %{_mandir}/man3/Set::Object::Weak.3pm*
%dir %{perl_vendorarch}/auto/Set/
%{perl_vendorarch}/auto/Set/Object/
%dir %{perl_vendorarch}/Set/
%{perl_vendorarch}/Set/Object/
%{perl_vendorarch}/Set/Object.pm

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
