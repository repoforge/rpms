# $Id$
# Authority: dag
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-CreditCard

Summary: Perl module to validate/generate credit card checksums/names
Name: perl-Business-CreditCard
Version: 0.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-CreditCard/

Source: http://www.cpan.org/modules/by-module/Business/Business-CreditCard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Business-CreditCard is a Perl module to validate/generate
credit card checksums/names.

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
%doc %{_mandir}/man3/Business::CreditCard.3pm*
%dir %{perl_vendorlib}/Business/
%{perl_vendorlib}/Business/CreditCard.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)
