# $Id$

# Authority: dries
# Upstream: Daniel P. Berrangé <dan$berrange,com>

%define real_name Config-Record
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Configuration file access
Name: perl-Config-Record
Version: 1.0.5
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Record/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANBERR/Config-Record-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Config::Record provides a module for loading configuration
records. It supports scalar, array and hash parameters nested
to an arbitrary depth.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES AUTHORS
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Config/Record.pm
%{perl_vendorlib}/Config/Record.pod
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.5
- Initial package.
