# $Id$
# Authority: dries
# Upstream: Burak Gursoy <burak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Template-Simple

Summary: Simple text template engine
Name: perl-Text-Template-Simple
Version: 0.82
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Template-Simple/

Source: http://search.cpan.org/CPAN/authors/id/B/BU/BURAK/Text-Template-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Digest::MD5) >= 1.00
BuildRequires: perl(File::Temp) >= 0.12
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Test::More) >= 0.40
Requires: perl(Digest::MD5) >= 1.00

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Simple text template engine.

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
%doc %{_mandir}/man3/Text::Template::Simple.3pm*
%doc %{_mandir}/man3/Text::Template::Simple::*.3pm*
%dir %{perl_vendorlib}/Text/
%dir %{perl_vendorlib}/Text/Template/
%{perl_vendorlib}/Text/Template/Simple/
%{perl_vendorlib}/Text/Template/Simple.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.82-1
- Updated to version 0.82.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.81-1
- Updated to version 0.81.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.80-1
- Updated to version 0.80.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.70-1
- Updated to version 0.70.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.53-1
- Updated to release 0.53.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.52-1
- Updated to release 0.52.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.50-1
- Updated to release 0.50.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Updated to release 0.47.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Wed Sep 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Updated to release 0.44.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
