# $Id$
# Authority: dries
# Upstream: Dave Plonka <plonka$doit,wisc,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Patricia

Summary: Patricia Trie perl module for fast IP address lookups
Name: perl-Net-Patricia
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Patricia/

Source: http://www.cpan.org/modules/by-module/Net/Net-Patricia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module uses a Patricia Trie data structure to quickly
perform IP address prefix matching for applications such as
IP subnet, network or routing table lookups.  The data
structure is based on a radix tree using a radix of two, so
sometimes you see patricia implementations called "radix" as
well.  The term "Trie" is derived from the word "retrieval"
but is pronounced like "try".  Patricia stands for
"Practical Algorithm to Retrieve Information Coded as
Alphanumeric", and was first suggested for routing table
lookups by Van Jacobsen.  Patricia Trie performance
characteristics are well-known as it has been employed for
routing table lookups within the BSD kernel since the 4.3
Reno release.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/Patricia.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/Patricia/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.014-1
- Updated to release 1.014.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.010-1
- Initial package.
