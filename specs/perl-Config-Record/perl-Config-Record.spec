# $Id$
# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Record

Summary: Configuration file access
Name: perl-Config-Record
Version: 1.1.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Record/

Source: http://www.cpan.org/modules/by-module/Config/Config-Record-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
Config::Record provides a module for loading configuration
records. It supports scalar, array and hash parameters nested
to an arbitrary depth.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml META.yml.PL README examples/
%doc %{_mandir}/man3/Config::Record.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Record.pm
%{perl_vendorlib}/Config/Record.pod

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.5
- Initial package.
