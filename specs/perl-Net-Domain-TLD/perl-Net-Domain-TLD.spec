# $Id$
# Authority: dries
# Upstream: Alex Pavlovic <alexp$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Domain-TLD

Summary: Retrieve currently available tld names and descriptions
Name: perl-Net-Domain-TLD
Version: 1.68
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Domain-TLD/

Source: http://www.cpan.org/modules/by-module/Net/Net-Domain-TLD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The purpose of this module is to provide user with current list of
available top level domain names including new ICANN additions and
ccTLDs

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
%doc %{_mandir}/man3/Net::Domain::TLD.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Domain/
#%{perl_vendorlib}/Net/Domain/TLD/
%{perl_vendorlib}/Net/Domain/TLD.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.68-1
- Updated to version 1.68.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.67-1
- Updated to release 1.67.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.65-1
- Updated to release 1.65.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.62-1
- Updated to release 1.62.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
