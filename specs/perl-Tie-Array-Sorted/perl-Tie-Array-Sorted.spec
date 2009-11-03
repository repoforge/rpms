# $Id$
# Authority: dries
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Array-Sorted

Summary: Sorted array
Name: perl-Tie-Array-Sorted
Version: 1.41
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Array-Sorted/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-Array-Sorted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
An array which is kept sorted.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc %{_mandir}/man3/Tie::Array::Sorted.3pm*
%doc %{_mandir}/man3/Tie::Array::Sorted::Lazy.3pm*
%dir %{perl_vendorlib}/Tie/
%dir %{perl_vendorlib}/Tie/Array/
%{perl_vendorlib}/Tie/Array/Sorted/
%{perl_vendorlib}/Tie/Array/Sorted.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
