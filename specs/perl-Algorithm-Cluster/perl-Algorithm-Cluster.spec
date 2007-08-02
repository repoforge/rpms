# $Id$
# Authority: dries
# Upstream: mdehoon <mdehoon$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Cluster

Summary: Interface to the C Clustering Library
Name: perl-Algorithm-Cluster
Version: 1.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Cluster/

Source: http://search.cpan.org//CPAN/authors/id/M/MD/MDEHOON/Algorithm-Cluster-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl interface to the C Clustering Library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Algorithm::Cluster*
%{perl_vendorarch}/Algorithm/Cluster.pm
%{perl_vendorarch}/auto/Algorithm/Cluster/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.33-1
- Initial package.
