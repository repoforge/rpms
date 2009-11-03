# $Id$
# Authority: dries
# Upstream: Ian Docherty <pause$iandocherty,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-I18N-DBIC

Summary: Internationalization for Catalyst data loaded from a database
Name: perl-Catalyst-Plugin-I18N-DBIC
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-I18N-DBIC/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-I18N-DBIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Internationalization for Catalyst data loaded from a database.

%prep
%setup -n catalyst_plugin_i18n_dbic

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
%doc %{_mandir}/man3/Catalyst::Plugin::I18N::DBIC.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/I18N/
#%{perl_vendorlib}/Catalyst/Plugin/I18N/DBIC/
%{perl_vendorlib}/Catalyst/Plugin/I18N/DBIC.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
