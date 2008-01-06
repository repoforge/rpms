# $Id$
# Authority: dag
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scalar-Defer

Summary: Lazy evaluation in Perl
Name: perl-Scalar-Defer
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scalar-Defer/

Source: http://www.cpan.org/modules/by-module/Scalar/Scalar-Defer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Class::InsideOut)
BuildRequires: perl(Exporter::Lite)
Requires: perl >= 0:5.6.0

%description
Lazy evaluation in Perl.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Scalar::Defer.3pm*
%dir %{perl_vendorlib}/Scalar/
#%{perl_vendorlib}/Scalar/Defer/
%{perl_vendorlib}/Scalar/Defer.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
