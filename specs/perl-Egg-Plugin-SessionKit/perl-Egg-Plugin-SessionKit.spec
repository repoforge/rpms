# $Id$
# Authority: dries
# Upstream: Masatoshi Mizuno <mizuno$bomcity,com>
# Upstream: Masatoshi Mizuno <lushe$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Egg-Plugin-SessionKit

Summary: Session plugin for Egg
Name: perl-Egg-Plugin-SessionKit
Version: 3.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Egg-Plugin-SessionKit/

Source: http://www.cpan.org/modules/by-module/Egg/Egg-Plugin-SessionKit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Install)

%description
Session plugin for Egg.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Egg::Helper::Model::Session.3pm*
%doc %{_mandir}/man3/Egg::Model::Session.3pm*
%doc %{_mandir}/man3/Egg::Model::Session::*.3pm*
%doc %{_mandir}/man3/Egg::Plugin::Session.3pm*
%doc %{_mandir}/man3/Egg::Plugin::SessionKit.3pm*
%dir %{perl_vendorlib}/Egg/
%dir %{perl_vendorlib}/Egg/Helper/
%dir %{perl_vendorlib}/Egg/Helper/Model/
%{perl_vendorlib}/Egg/Helper/Model/Session.pm
%dir %{perl_vendorlib}/Egg/Model/
%{perl_vendorlib}/Egg/Model/Session/
%{perl_vendorlib}/Egg/Model/Session.pm
%dir %{perl_vendorlib}/Egg/Plugin/
#%{perl_vendorlib}/Egg/Plugin/SessionKit/
%{perl_vendorlib}/Egg/Plugin/Session.pm
%{perl_vendorlib}/Egg/Plugin/SessionKit.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 3.05-1
- Updated to release 3.05.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
