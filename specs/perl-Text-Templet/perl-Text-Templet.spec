# $Id$
# Authority: dries
# Upstream: Denis Petrov <denispetrov$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Templet

Summary: Lightweight Text Template Processor
Name: perl-Text-Templet
Version: 3.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Templet/

Source: http://search.cpan.org/CPAN/authors/id/D/DP/DPETROV/Text-Templet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
template processor built using Perl's eval().

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Templet.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Templet/
%{perl_vendorlib}/Text/Templet.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 3.0-1
- Updated to version 3.0.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 2.9-1
- Updated to version 2.9.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.8a-1
- Updated to release 2.8a.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.8-1
- Updated to release 2.8.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Initial package.
