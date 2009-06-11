# $Id$
# Authority: dries
# Upstream: Derek Price <derek$ximbiot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-MediawikiFormat

Summary: Translate Wiki markup into other text formats
Name: perl-Text-MediawikiFormat
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-MediawikiFormat/

Source: http://www.cpan.org/modules/by-module/Text/Text-MediawikiFormat-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Translate Wiki markup into other text formats.

%prep
%setup -n %{real_name}-v%{version}

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
%doc ARTISTIC Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Text::MediawikiFormat.3pm*
%doc %{_mandir}/man3/Text::MediawikiFormat::*.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/MediawikiFormat/
%{perl_vendorlib}/Text/MediawikiFormat.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.0-1
- Updated to version 1.0.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
