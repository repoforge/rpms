# $Id$
# Authority: dries
# Upstream: Jeff Lavallee <jeff$zeroclue,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-Marketing

Summary: Interface for Yahoo! Search Marketing's Web Services
Name: perl-Yahoo-Marketing
Version: 3.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Marketing/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-Marketing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1 
BuildRequires: perl(Module::Build) >= 0.26
BuildRequires: perl(SOAP::Lite)
BuildRequires: perl(Test::Class)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::XPath)
BuildRequires: perl(YAML) >= 0.01
Requires: perl >= 1:5.6.1 

%description
An interface for Yahoo! Search Marketing's Web Services.

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
%doc %{_mandir}/man3/Yahoo::Marketing*3pm*
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/Marketing/
%{perl_vendorlib}/Yahoo/Marketing.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
