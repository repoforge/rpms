# $Id$
# Authority: dries
# Upstream: Christopher H. Laco <claco$chrislaco,com>
# Upstream: Tomas Doran <bobtfish$bobtfish,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-SVN

Summary: Catalyst Model to browse Subversion repositories
Name: perl-Catalyst-Model-SVN
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-SVN/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Model-SVN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Devel)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker) >= 5.8.0
BuildRequires: perl(FindBin)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)

%description
This model class uses the perl-subversion bindings to access a
Subversion repository and list items and view their contents. It is
currently only a read-only client but may expand to be a fill fledged
client at a later time.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README Todo
%doc %{_mandir}/man3/Catalyst::Model::SVN.3pm*
%doc %{_mandir}/man3/Catalyst::Model::SVN::*.3pm*
%doc %{_mandir}/man3/Catalyst::Helper::Model::SVN.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Model/
%{perl_vendorlib}/Catalyst/Model/SVN/
%{perl_vendorlib}/Catalyst/Model/SVN.pm
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Helper/
%dir %{perl_vendorlib}/Catalyst/Helper/Model/
#%{perl_vendorlib}/Catalyst/Helper/Model/SVN/
%{perl_vendorlib}/Catalyst/Helper/Model/SVN.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
