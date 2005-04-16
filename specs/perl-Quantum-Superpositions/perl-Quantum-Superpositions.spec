# $Id$
# Authority: dries
# Upstream: Steven Lembark <lembark$wrkhors,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quantum-Superpositions

Summary: QM-like superpositions in Perl
Name: perl-Quantum-Superpositions
Version: 2.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quantum-Superpositions/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEMBARK/Quantum-Superpositions-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
QM-like superpositions in Perl.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Quantum/Superpositions.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Initial package.
