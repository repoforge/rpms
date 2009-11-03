# $Id$
# Authority: dag
# Upstream: Christian Gilmore <cag$nospam,us,ibm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name I18N-AcceptLanguage

Summary: Matches language preference to available languages
Name: perl-I18N-AcceptLanguage
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/I18N-AcceptLanguage/

Source: http://www.cpan.org/modules/by-module/I18N/I18N-AcceptLanguage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Matches language preference to available languages.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/I18N::AcceptLanguage.3pm*
%dir %{perl_vendorlib}/I18N/
#%{perl_vendorlib}/I18N/AcceptLanguage/
%{perl_vendorlib}/I18N/AcceptLanguage.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
