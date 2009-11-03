# $Id$
# Authority: dag
# Upstream: Josh ben Jore <jjore$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Anything

Summary: Anything, even imaginary modules are loadable
Name: perl-Acme-Anything
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Anything/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Anything-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Anything, even imaginary modules are loadable.

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
%doc %{_mandir}/man3/Acme::Anything.3pm*
%dir %{perl_vendorlib}/Acme/
#%{perl_vendorlib}/Acme/Anything/
%{perl_vendorlib}/Acme/Anything.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
