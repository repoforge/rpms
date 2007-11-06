# $Id$
# Authority: dries
# Upstream: Benjamin Holzman <bholzman$earthlink,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-RedBlack

Summary: Perl implementation of Red/Black tree, a type of balanced tree
Name: perl-Tree-RedBlack
Version: 0.3
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-RedBlack/

Source: http://search.cpan.org/CPAN/authors/id/B/BH/BHOLZMAN/Tree-RedBlack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Tree::RedBlack is a pure perl implementation of the Red/Black balanced tree
algorithm from the book "Algorithms" by Cormen, Leiserson & Rivest.  It
supports insertion, searching, finding minima, maxima, predecessors and
successors, and deletion (deletion definitely has bugs right now).  Each node
in the tree consists of a key and a value.  Both can be any Perl scalar, even a
complex structure.  By default, keys in the tree are ordered lexically, but the
ordering can be overriden by providing the tree with a comparison subroutine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/RedBlack.pm
%{perl_vendorlib}/Tree/RedBlack

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
