# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name File-Find-Rule
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Alternative interface to File::Find
Name: perl-File-Find-Rule
Version: 0.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/File-Find-Rule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains an alternative interface to File::Find.

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
%doc README Changes
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/findrule
%{perl_vendorlib}/File/Find/Rule.pm
%{perl_vendorlib}/File/Find/Rule/*.pod
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
