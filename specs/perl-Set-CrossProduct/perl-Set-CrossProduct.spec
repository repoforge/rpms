# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-CrossProduct

Summary: Work with the cross product of two or more sets
Name: perl-Set-CrossProduct
Version: 1.93
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-CrossProduct/

Source: http://www.cpan.org/modules/by-module/Set/Set-CrossProduct-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Work with the cross product of two or more sets.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man1/cross.1*
%doc %{_mandir}/man3/Set::CrossProduct.3*
%{_bindir}/cross
%dir %{perl_vendorlib}/Set/
#%{perl_vendorlib}/Set/CrossProduct/
%{perl_vendorlib}/Set/CrossProduct.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.93-1
- Updated to release 1.93.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.92-1
- Updated to release 1.92.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Updated to release 1.8.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
