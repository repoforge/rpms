# $Id$
# Authority: dries
# Upstream: David Burdick <dburdickNOSPAM$systemsbiology,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Boost-Graph

Summary: Interface to the Boost-Graph C++ libraries
Name: perl-Boost-Graph
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Boost-Graph/

Source: http://www.cpan.org/modules/by-module/Boost/Boost-Graph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl interface to the Boost-Graph C++ libraries.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Boost::Graph.3pm*
%doc %{_mandir}/man3/Boost::Graph::*.3pm*
%dir %{perl_vendorarch}/Boost/
%{perl_vendorarch}/Boost/Graph/
%{perl_vendorarch}/Boost/Graph.pm
%dir %{perl_vendorarch}/auto/Boost/
%{perl_vendorarch}/auto/Boost/Graph/

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
