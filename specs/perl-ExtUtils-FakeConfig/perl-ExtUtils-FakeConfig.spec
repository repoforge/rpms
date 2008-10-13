# $Id$
# Authority: dries
# Upstream: Mattia Barbon <mbarbon$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-FakeConfig

Summary: Allows overriding some config values
Name: perl-ExtUtils-FakeConfig
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-FakeConfig/

Source: http://search.cpan.org//CPAN/authors/id/M/MB/MBARBON/ExtUtils-FakeConfig-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Allows you to override some config values.

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
%doc Changes README.txt
%doc %{_mandir}/man3/*
%{perl_vendorlib}/ExtUtils/FakeConfig.pm
%{perl_vendorlib}/Config_m.pod

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
