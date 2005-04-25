# $Id$
# Authority: dries
# Upstream: Tim Jenness <t,jenness$jach,hawaii,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-PassGen

Summary: Generate a random password that looks like a real word
Name: perl-Crypt-PassGen
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-PassGen/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJENNESS/Crypt-PassGen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, words

%description
This module provides a single command for generating random password
that is close enough to a real word that it is easy to remember.
It does this by using the frequency of letter combinations in 
a language (the frequency table is generated during installation
although multiple tables can be generated and used for different
languages).

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/PassGen.pm
%{perl_vendorlib}/Crypt/PassGenWordFreq.dat

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
