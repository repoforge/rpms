# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-MOP

Summary: Meta Object Protocol for Perl 5
Name: perl-Class-MOP
Version: 0.70
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MOP/

Source: http://www.cpan.org/modules/by-module/Class/Class-MOP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::Exception) >= 0.21
#BuildRequires: perl(Test::More) >= 0.62

%description
Class-MOP is a Perl module that implements a Meta Object Protocol.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Class::MOP.3pm*
%doc %{_mandir}/man3/Class::MOP::*.3pm*
%doc %{_mandir}/man3/metaclass.3pm*
%dir %{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/auto/Class/MOP/
%dir %{perl_vendorarch}/Class/
%{perl_vendorarch}/Class/MOP/
%{perl_vendorarch}/Class/MOP.pm
%{perl_vendorarch}/metaclass.pm

%changelog
* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.67-1
- Updated to release 0.67.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Fri Aug 22 2008 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Fri Jul 25 2008 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 0.53-1
- Updated to release 0.53.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.52-1
- Updated to release 0.52.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.51-1
- Updated to release 0.51.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.37-1
- Initial package. (using DAR)
