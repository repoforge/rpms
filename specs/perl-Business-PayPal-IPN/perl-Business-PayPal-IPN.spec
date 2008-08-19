# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-PayPal-IPN

Summary: Perl extension that implements PayPal IPN v1.5
Name: perl-Business-PayPal-IPN
Version: 1.94
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-PayPal-IPN/

Source: http://www.cpan.org/modules/by-module/Business/Business-PayPal-IPN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension that implements PayPal IPN v1.5.

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
%doc Changes MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/Business::PayPal::IPN.3pm*
%dir %{perl_vendorlib}/Business/
%dir %{perl_vendorlib}/Business/PayPal/
#%{perl_vendorlib}/Business/PayPal/IPN/
%{perl_vendorlib}/Business/PayPal/IPN.pm

%changelog
* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 1.94-1
- Initial package. (using DAR)
