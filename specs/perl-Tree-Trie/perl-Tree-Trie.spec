# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Trie

Summary: Trie data structure
Name: perl-Tree-Trie
Version: 1.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Trie/

Source: http://search.cpan.org/CPAN/authors/id/A/AV/AVIF/Tree-Trie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Tree::Trie is an implementation of a Trie data structure in Perl.

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
%{perl_vendorlib}/Tree/Trie.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
