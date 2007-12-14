# $Id$
# Authority: dries
# Upstream: David Hand <cogent$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-DAG_Node

Summary: (super)class for representing nodes in a tree
Name: perl-Tree-DAG_Node
Version: 1.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-DAG_Node/

Source: http://www.cpan.org/modules/by-module/Tree/Tree-DAG_Node-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Tree::DAG_Node is a (super)class for representing nodes in a tree.

This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure.  The tree structure is not an object itself, but
is emergent from the linkages you create between nodes.  This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Tree::DAG_Node.3pm*
%dir %{perl_vendorlib}/Tree/
#%{perl_vendorlib}/Tree/DAG_Node/
%{perl_vendorlib}/Tree/DAG_Node.pm

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
