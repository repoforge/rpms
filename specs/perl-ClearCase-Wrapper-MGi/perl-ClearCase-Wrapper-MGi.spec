# $Id$
# Authority: dag
# Upstream: Marc Girod <CENSORED>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Wrapper-MGi

Summary: Marc Girod's contributed cleartool wrapper functions
Name: perl-ClearCase-Wrapper-MGi
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Wrapper-MGi/

Source: http://search.cpan.org/CPAN/authors/id/M/MG/MGI/ClearCase-Wrapper-MGi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ClearCase::Wrapper) >= 1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(ClearCase::Wrapper) >= 1

%filter_from_requires /^perl*/d
%filter_setup

%description
Marc Girod's contributed cleartool wrapper functions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man3/ClearCase::Wrapper::MGi.3pm*
%dir %{perl_vendorlib}/auto/ClearCase/
%{perl_vendorlib}/auto/ClearCase/Wrapper/
%dir %{perl_vendorlib}/ClearCase/
%dir %{perl_vendorlib}/ClearCase/Wrapper/
#%{perl_vendorlib}/ClearCase/Wrapper/MGi/
%{perl_vendorlib}/ClearCase/Wrapper/MGi.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
