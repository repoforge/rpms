# $Id$
# Authority: dries
# Upstream: Ivan Tubert-Brohman <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-MDLMol

Summary: MDL molfile reader and writer
Name: perl-Chemistry-File-MDLMol
Version: 0.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chemistry-File-MDLMol/

Source: http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-MDLMol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Chemistry::Mol) >= 0.35
BuildRequires: perl(Chemistry::Ring) >= 0.19
Requires: perl(Chemistry::Mol) >= 0.35
Requires: perl(Chemistry::Ring) >= 0.19
AutoReq: no

%description
This modules read MDL mol and sd files. Please note that they are at an early
stage of development and implement only a fraction of the standard.  However,
it is a fraction that the author finds useful for most everyday needs.

Chemistry::File::MDLMol reads and writes only the basic connection table; that
is, the coordinates and symbol of each atom, and the type and atoms of each
bond. Chemistry::File::SDF does the same, returning a list of molecules. It
also reads the data items for each molecule.

The MDLmol module automatically registers the 'mdl' format with Chemistry::Mol,
so that PDB files may be identified and read by Chemistry::Mol::read_mol().
The SDF module registers the 'sdf' format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Chemistry/File/MDLMol.pm
%{perl_vendorlib}/Chemistry/File/SDF.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17
- Initial package.
