# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GDGraph

Summary: Graph Plotting Module for Perl 5
Name: perl-GDGraph
Version: 1.44
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDGraph/

Source: http://www.cpan.org/authors/id/B/BW/BWARFIELD/GDGraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Graph Plotting Module for Perl 5.

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
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README samples/
%doc %{_mandir}/man3/GD::Graph.3pm*
%doc %{_mandir}/man3/GD::Graph::*.3pm*
%dir %{perl_vendorlib}/GD/
%{perl_vendorlib}/GD/Graph/
%{perl_vendorlib}/GD/Graph.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.44-1
- Initial package. (using DAR)
