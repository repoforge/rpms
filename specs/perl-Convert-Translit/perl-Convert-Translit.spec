# $Id$
# Authority: dries
# Upstream: Genji Schmeder <genji$jps,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-Translit

Summary: String conversion among numerous character sets
Name: perl-Convert-Translit
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-Translit/

Source: http://search.cpan.org/CPAN/authors/id/G/GE/GENJISCH/Convert-Translit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides the function "transliterate" for
transliterating strings between any 8-bit character sets defined in
RFC 1345 (about 128 character sets).  The RFC document is
included so you can look up character set names and aliases (and it's
also read by the module when creating transliteration maps).

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
%{perl_vendorlib}/Convert/Translit.pm
%{perl_vendorlib}/Convert/example.pl
%{perl_vendorlib}/Convert/rfc1345
%{perl_vendorlib}/Convert/substitutes

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
