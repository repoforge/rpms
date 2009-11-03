# $Id$
# Authority: dag
# Upstream: Yuji Tamashiro <yuji$tamashiro,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-derived_classes

Summary: Perl module to return derived classes of a class
Name: perl-UNIVERSAL-derived_classes
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-derived_classes/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-derived_classes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UNIVERSAL-derived_classes is a Perl module to return derived classes
of a class.

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
%doc %{_mandir}/man3/UNIVERSAL::derived_classes.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
#%{perl_vendorlib}/UNIVERSAL/derived_classes/
%{perl_vendorlib}/UNIVERSAL/derived_classes.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
