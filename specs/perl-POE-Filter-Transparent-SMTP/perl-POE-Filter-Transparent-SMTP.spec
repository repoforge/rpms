# $Id$
# Authority: cmr
# Upstream: George Nistorica <ultradm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-Transparent-SMTP

Summary: Make SMTP transparency a breeze :)
Name: perl-POE-Filter-Transparent-SMTP
Version: 0.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-Transparent-SMTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-Transparent-SMTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Make SMTP transparency a breeze :).

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Filter::Transparent::SMTP.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
%dir %{perl_vendorlib}/POE/Filter/Transparent/
#%{perl_vendorlib}/POE/Filter/Transparent/SMTP/
%{perl_vendorlib}/POE/Filter/Transparent/SMTP.pm

%changelog
* Tue Jul 07 2009 Christoph Maser <cmr@financial.com> - 0.2-1
- Initial package. (using DAR)
