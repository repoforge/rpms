# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-Dissociate

Summary: Dissociated Press algorithm and filter
Name: perl-Games-Dissociate
Version: 0.19
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-Dissociate/

Source: http://www.cpan.org/modules/by-module/Games/Games-Dissociate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Pod::Coverage) >= 0.18
BuildRequires: perl(Test::Pod) >= 1.26
BuildRequires: perl(Test::Pod::Coverage) >= 1.08

%description
This module provides the function `dissociate', which implements a
Dissociated Press algorithm, well known to Emacs users as "meta-x
dissociate". The algorithm here is by no means a straight port of
Emacs's 'dissociate.el', but is instead merely inspired by it.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Games::Dissociate.3pm*
%dir %{perl_vendorlib}/Games/
#%{perl_vendorlib}/Games/Dissociate/
%{perl_vendorlib}/Games/Dissociate.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
