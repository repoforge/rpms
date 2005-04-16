# $Id$
# Authority: dries
# Upstream: Jan Pazdziora <adelton$fi,muni,cz>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TeX-Hyphen

Summary: Hyphenate words using TeX's patterns 
Name: perl-TeX-Hyphen
Version: 0.140
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TeX-Hyphen/

Source: http://search.cpan.org/CPAN/authors/id/J/JA/JANPAZ/TeX-Hyphen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is the README file for the TeX::Hyphen module. This module uses
TeX style hyphenation patterns to find places in words to hyphenate.
You can supply any hyphenation file you like.

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
%{perl_vendorlib}/TeX/Hyphen.pm
%{perl_vendorlib}/TeX/Hyphen

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.140-1
- Initial package.
