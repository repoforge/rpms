# $Id$
# Authority: dries
# Upstream: Luis Muñoz <luismunoz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Radius

Summary: Object-oriented Perl interface to RADIUS
Name: perl-Net-Radius
Version: 1.56
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Radius/

Source: http://www.cpan.org/modules/by-module/Net/Net-Radius-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Object-oriented Perl interface to RADIUS.

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

### Clean up docs
find contrib/ docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.3COM README.VSA README.broken README.packets README.server version.pl contrib/ docs/ examples/
%doc %{_mandir}/man3/Net::Radius::Dictionary.3pm*
%doc %{_mandir}/man3/Net::Radius::Packet.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Radius/

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.56-1
- Updated to release 1.56.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.55-1
- Initial package.
