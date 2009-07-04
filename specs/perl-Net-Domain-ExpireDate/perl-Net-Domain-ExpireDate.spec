# $Id$
# Authority: dries
# Upstream: Walery Studennikov <despair$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Domain-ExpireDate

Summary: Obtain expiration date of domain names
Name: perl-Net-Domain-ExpireDate
Version: 0.95
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Domain-ExpireDate/

Source: http://www.cpan.org/modules/by-module/Net/Net-Domain-ExpireDate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Obtain expiration date of domain names.

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
%doc %{_mandir}/man3/Net::Domain::ExpireDate.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Domain/
#%{perl_vendorlib}/Net/Domain/ExpireDate/
%{perl_vendorlib}/Net/Domain/ExpireDate.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.95-1
- Updated to version 0.95.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated to release 0.80.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Initial package.
