# $Id$
# Authority: dries
# Upstream: Kyle R. Burton <kyle,burton$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-MultiNode

Summary: Multi node unordered tree objects
Name: perl-Tree-MultiNode
Version: 1.0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-MultiNode/

Source: http://search.cpan.org/CPAN/authors/id/K/KR/KRBURTON/Tree-MultiNode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is an implementation of a multi node tree.  The uniqueness of
keys is not enforced, nor is there enforcement of ordering of nodes.

Tree::MultiNode was created to aid in modeling heriarchical 
relationships, like the relationships inherent in the records from
a RDBMS.  Where multi-to-multi relationships could produce multiple
child nodes with the same types or basic attributes.  Unique key
enforcement would be inappropriate in these cases (at least for me).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/MultiNode.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.10-1
- Initial package.
