# $Id$
# Authority: dries
# Upstream: Matt Wilson <mattw$mattsscripts,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-XML

Summary: Converts POD to XML
Name: perl-Pod-XML
Version: 0.99
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-XML/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Module to convert POD to XML.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/pod2xml.1*
%doc %{_mandir}/man3/Pod::XML.3pm*
%{_bindir}/pod2xml
%dir %{perl_vendorlib}/Pod/
#%{perl_vendorlib}/Pod/XML/
%{perl_vendorlib}/Pod/XML.pm

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.99-1
- Updated to release 0.99.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
