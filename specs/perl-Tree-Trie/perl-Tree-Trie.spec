# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Trie

Summary: Trie data structure
Name: perl-Tree-Trie
Version: 1.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Trie/

Source: http://search.cpan.org/CPAN/authors/id/A/AV/AVIF/Tree-Trie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tree::Trie is an implementation of a Trie data structure in Perl.

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
%{perl_vendorlib}/Tree/Trie.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1-1
- Initial package.
