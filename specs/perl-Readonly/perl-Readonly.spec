# $Id$
# Authority: dries
# Upstream: Eric J. Roode <sdn,peonies40394$zoemail,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Readonly

Summary: Facility for creating read-only scalars, arrays, hashes
Name: perl-Readonly
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Readonly/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Readonly-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Readonly.pm provides a facility for creating non-modifiable scalars,
arrays, and hashes.

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
%{perl_vendorlib}/Readonly.pm
%{perl_vendorlib}/benchmark.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
