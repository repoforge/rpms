# $Id$
# Authority: dries
# Upstream: Burak Gursoy <burak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Template-Simple

Summary: Simple text template engine
Name: perl-Text-Template-Simple
Version: 0.53
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Template-Simple/

Source: http://www.cpan.org/modules/by-module/Text/Text-Template-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)

%description
Simple text template engine.

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
%doc %{_mandir}/man3/Text::Template::Simple.3pm*
%doc %{_mandir}/man3/Text::Template::Simple::*.3pm*
%dir %{perl_vendorlib}/Text/
%dir %{perl_vendorlib}/Text/Template/
%{perl_vendorlib}/Text/Template/Simple/
%{perl_vendorlib}/Text/Template/Simple.pm

%changelog
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
