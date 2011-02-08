# $Id$
# Authority: dries
# Upstream: John D. Shearer <jshearer$netguy,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-DHCPparse

Summary: Perl extension for parsing dhcpd lease files
Name: perl-Text-DHCPparse
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-DHCPparse/

Source: http://search.cpan.org/CPAN/authors/id/J/JS/JSHEARER/Text-DHCPparse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl extension for parsing dhcpd lease files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/Text::DHCPparse.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/DHCPparse/
%{perl_vendorlib}/Text/DHCPparse.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.10-1
- Updated to version 0.10.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
