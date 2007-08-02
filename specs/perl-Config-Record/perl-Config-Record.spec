# $Id$
# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Record

Summary: Configuration file access
Name: perl-Config-Record
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Record/

Source: http://www.cpan.org/modules/by-module/Config/Config-Record-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Record.pm
%{perl_vendorlib}/Config/Record.pod

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.5
- Initial package.
