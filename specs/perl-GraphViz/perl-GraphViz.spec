# $Id$
# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GraphViz

Summary: Interface to the GraphViz graphing tool
Name: perl-GraphViz
Version: 2.02
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GraphViz/

Source: http://www.cpan.org/modules/by-module/GraphViz/GraphViz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: graphviz
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: graphviz

%description
This module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato" and "twopi" programs from the GraphViz
project (http://www.graphviz.org/ or
http://www.research.att.com/sw/tools/graphviz/).

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/GraphViz.pm
%{perl_vendorlib}/Devel/GraphVizProf.pm
%{perl_vendorlib}/GraphViz/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.02-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Initial package.
