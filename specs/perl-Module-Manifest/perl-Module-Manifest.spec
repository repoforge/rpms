# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Manifest

Summary: Parse and examine a Perl distribution MANIFEST file
Name: perl-Module-Manifest
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Manifest/

Source: http://www.cpan.org/modules/by-module/Module/Module-Manifest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.005

%description
Parse and examine a Perl distribution MANIFEST file.

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
%doc Changes README
%doc %{_mandir}/man3/Module::Manifest*
%{perl_vendorlib}/Module/Manifest.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
