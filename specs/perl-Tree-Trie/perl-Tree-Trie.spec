# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Trie

Summary: Trie data structure
Name: perl-Tree-Trie
Version: 1.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Trie/

Source: http://search.cpan.org/CPAN/authors/id/A/AV/AVIF/Tree-Trie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Pod::Coverage) >= 0.18
BuildRequires: perl(Test::Pod) >= 1.26
BuildRequires: perl(Test::Pod::Coverage) >= 1.08

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Tree::Trie is an implementation of a Trie data structure in Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Tree::Trie.3pm*
%dir %{perl_vendorlib}/Tree/
#%{perl_vendorlib}/Tree/Trie/
%{perl_vendorlib}/Tree/Trie.pm


%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.7-1
- Updated to version 1.7.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
