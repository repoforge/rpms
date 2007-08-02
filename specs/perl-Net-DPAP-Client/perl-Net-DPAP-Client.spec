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
Version: 0.26
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DPAP-Client/

Source: http://www.cpan.org/modules/by-module/Net/Net-DPAP-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
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
