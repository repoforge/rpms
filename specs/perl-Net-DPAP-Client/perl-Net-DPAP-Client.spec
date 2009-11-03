# $Id$
# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DPAP-Client

Summary: Connect to iPhoto shares (DPAP)
Name: perl-Net-DPAP-Client
Version: 0.26
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DPAP-Client/

Source: http://www.cpan.org/modules/by-module/Net/Net-DPAP-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides a DPAP client. DPAP is the Digital Photo Access
Protocol and is the protocol that Apple iPhoto uses to share photos.
This allows you to browse shared albums, and download thumbnail and
hires versions of shared photos.

It currently doesn't support password-protected shares.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/DPAP/Client.pm
%{perl_vendorlib}/Net/DPAP/Client/*

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Initial package.
