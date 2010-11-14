# $Id$
# Authority: dries
# Upstream: <autrijus$autrijus,org>

### This package is dangerous, we don't want it to be available as-is
# Tag: rft


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-AutoInstall

Summary: Automatic install of dependencies via CPAN
Name: perl-ExtUtils-AutoInstall
Version: 0.63
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-AutoInstall/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-AutoInstall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-CPANPLUS
BuildRequires: perl-Sort-Versions

%description
ExtUtils::AutoInstall is a module to let Makefile.PL automatically
install dependencies via CPAN or CPANPLUS.

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
%doc AUTHORS Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/AutoInstall.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.63-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
