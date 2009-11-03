# $Id$
# Authority: dries
# Upstream: Pritchard Musonda <stiqs$blackhills,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-WhoisNG

Summary: Perl extension for whois lookup and parsing
Name: perl-Net-WhoisNG
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-WhoisNG/

Source: http://www.cpan.org/modules/by-module/Net/Net-WhoisNG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for whois lookup and parsing.

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
%doc %{_mandir}/man3/Net::WhoisNG.3pm*
%doc %{_mandir}/man3/Net::WhoisNG::Person.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/WhoisNG/
%{perl_vendorlib}/Net/WhoisNG.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Update to release 0.03.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
