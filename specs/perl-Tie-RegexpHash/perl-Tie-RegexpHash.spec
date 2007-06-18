# $Id$
# Authority: dries
# Upstream: Russell Harrison <rch$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-RegexpHash

Summary: Perl module to permit use of regular expressions as hash keys
Name: perl-Tie-RegexpHash
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-RegexpHash/

Source: http://ftp.cpan.org/pub/CPAN/modules/by-module/Tie/Tie-RegexpHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module allows one to use regular expressions for hash keys, so that
values can be associated with anything that matches the key.

Hashes can be operated on using the standard tied hash interface in Perl,
or using an object-oriented interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Tie::RegexpHash*
%dir %{perl_vendorlib}/Tie
%{perl_vendorlib}/Tie/RegexpHash.pm

%changelog
* Tue Jul 18 2006 Al Pacifico < adpacifico@users.sourceforge.net> - 0.15-1
Initial packaging.
