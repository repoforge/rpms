# $Id$
# Authority: dries
# Upstream: Kang-min Liu <gugod$gugod,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph-Writer-GraphViz

Summary: GraphViz Writer for Graph object
Name: perl-Graph-Writer-GraphViz
Version: 0.10
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph-Writer-GraphViz/

Source: http://www.cpan.org/modules/by-module/Graph/Graph-Writer-GraphViz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Graph::Writer::GraphViz is an Writer object of Graph, using
GraphViz module. All GraphViz output format should be supported
by nature.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Graph/
%dir %{perl_vendorlib}/Graph/Writer/
%{perl_vendorlib}/Graph/Writer/GraphViz.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
