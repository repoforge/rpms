# $Id$

# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define real_name Net-DPAP-Client
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Connect to iPhoto shares (DPAP)
Name: perl-Net-DPAP-Client
Version: 0.24
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DPAP-Client/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/Net-DPAP-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provides a DPAP client. DPAP is the Digital Photo Access
Protocol and is the protocol that Apple iPhoto uses to share photos.
This allows you to browse shared albums, and download thumbnail and
hires versions of shared photos.

It currently doesn't support password-protected shares.

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
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DPAP/Client.pm
%{perl_vendorlib}/Net/DPAP/Client/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.
