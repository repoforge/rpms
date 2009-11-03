# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-UI

Summary: Term::ReadLine UI made easy
Name: perl-Term-UI
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-UI/

Source: http://www.cpan.org/modules/by-module/Term/Term-UI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Term::UI provides methods to ask both elaborate questions as well
as simple yes/no questions via a Term::ReadLine interface using a
template. It can also parse options per unix style.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Term::UI.3pm*
%doc %{_mandir}/man3/Term::UI::History.3pm*
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/UI/
%{perl_vendorlib}/Term/UI.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Updated to version 0.20.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
