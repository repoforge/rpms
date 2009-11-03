# $Id$
# Authority: dries
# Upstream: George Chlipala <chips_g$ameritech,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Bonjour

Summary: mDNS or Bonjour support for service discovery
Name: perl-Net-Bonjour
Version: 0.96
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Bonjour/
Obsoletes: perl-Net-Rendezvous

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHLIGE/Net-Bonjour-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Net::Bonjour, a set of perl modules to utilize mDNS for service
discovery.  This method of service discovery is branded as Bonjour by
Apple Computer.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Bonjour.pm
%{perl_vendorlib}/Net/Bonjour/*
%{perl_vendorlib}/Net/Rendezvous.pm
%{perl_vendorlib}/Net/Rendezvous/*

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.96-1
- Rename from Net::Rendezvou to Net::Bonjour
- Updated to version 0.96.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.90-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Updated to release 0.90.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.86-1
- Initial package.
