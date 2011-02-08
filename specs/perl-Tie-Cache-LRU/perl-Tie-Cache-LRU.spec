# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Cache-LRU

Summary: Least-Recently Used cache
Name: perl-Tie-Cache-LRU
Version: 20110205
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Cache-LRU/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Tie-Cache-LRU-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp::Assert)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Virtual)
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.82
BuildRequires: perl(Test::More) 
BuildRequires: perl(enum)
Requires: perl(Carp::Assert)
Requires: perl(Class::Data::Inheritable)
Requires: perl(Class::Virtual)
#Requires: perl(Test::More) >= 0.82
Requires: perl(Test::More) 
Requires: perl(enum)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
A Least-Recently Used cache.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tie/Cache/LRU.pm
%{perl_vendorlib}/Tie/Cache/LRU

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 20110205-1
- Updated to version 20110205.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 20081023.2116-1
- Updated to version 20081023.2116.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
