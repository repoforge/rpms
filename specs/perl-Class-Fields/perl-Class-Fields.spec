# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Fields

Summary: Inspect the fields of a class
Name: perl-Class-Fields
Version: 0.203
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Fields/

Source: http://www.cpan.org/modules/by-module/Class/Class-Fields-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Inspect the fields of a class.

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
%doc Changes MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/Class::Fields.3pm*
%doc %{_mandir}/man3/Class::Fields::*.3pm*
%doc %{_mandir}/man3/private.3pm*
%doc %{_mandir}/man3/protected.3pm*
%doc %{_mandir}/man3/public.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Fields/
%{perl_vendorlib}/Class/Fields/
%{perl_vendorlib}/Class/Fields.pm
%{perl_vendorlib}/private.pm
%{perl_vendorlib}/protected.pm
%{perl_vendorlib}/public.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.203-1
- Updated to release 0.203.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.201-1
- Initial package.
