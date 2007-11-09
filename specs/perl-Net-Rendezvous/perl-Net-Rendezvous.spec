# $Id$
# Authority: dries
# Upstream: George Chlipala <chips_g$ameritech,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Rendezvous

Summary: mDNS or Rendezvous support for service discovery
Name: perl-Net-Rendezvous
Version: 0.90
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Rendezvous/

Source: http://www.cpan.org/modules/by-module/Net/Net-Rendezvous-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Net::Rendezvous, a set of perl modules to utilize mDNS for service
discovery.  This method of service discovery is branded as Rendezvous by
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
%{perl_vendorlib}/Net/Rendezvous.pm
%{perl_vendorlib}/Net/Rendezvous/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.90-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Updated to release 0.90.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.86-1
- Initial package.
