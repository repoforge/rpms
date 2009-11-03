# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-WikiFormat

Summary: Covert text in a simple Wiki markut language to other tag languages
Name: perl-Text-WikiFormat
Version: 0.79
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-WikiFormat/

Source: http://www.cpan.org/modules/by-module/Text/Text-WikiFormat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.3

%description
Text::WikiFormat converts text in a simple Wiki markup language to whatever
your little heart desires, provided you can describe it accurately in a
semi-regular tag language.

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
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::WikiFormat.3pm*
%doc %{_mandir}/man3/Text::WikiFormat::Blocks.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/WikiFormat/
%{perl_vendorlib}/Text/WikiFormat.pm

%changelog
* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.79-1
- Updated to release 0.79.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Updated to release 0.78.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.77-1
- Initial package.
