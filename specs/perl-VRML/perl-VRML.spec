# $Id$
# Authority: dries
# Upstream: Hartmut Palm <palm$gfz-potsdam,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name VRML

Summary: Specification independent VRML methods
Name: perl-VRML
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/VRML/

Source: http://www.cpan.org/modules/by-module/VRML/VRML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Specification independent VRML methods (1.0, 2.0, 97).

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
%doc CHANGES.TXT META.yml README.TXT TODO.TXT doc/ examples/
%doc %{_mandir}/man3/VRML.3pm*
%doc %{_mandir}/man3/VRML::*.3pm*
%{perl_vendorlib}/VRML/
%{perl_vendorlib}/VRML.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
