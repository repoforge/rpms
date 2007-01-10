# $Id$
# Authority: dries
# Upstream: David Burdick <dburdickNOSPAM$systemsbiology,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Boost-Graph

Summary: Interface to the Boost-Graph C++ libraries
Name: perl-Boost-Graph
Version: 1.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Boost-Graph/

Source: http://search.cpan.org//CPAN/authors/id/D/DB/DBURDICK/BoostGraph/Boost-Graph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, gcc-c++, boost-devel

%description
Perl interface to the Boost-Graph C++ libraries.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Boost::Graph*
%{perl_vendorarch}/Boost/Graph.pm
%{perl_vendorarch}/Boost/Graph/
%{perl_vendorarch}/auto/Boost/Graph/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
