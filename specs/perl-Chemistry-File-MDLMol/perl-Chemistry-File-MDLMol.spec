# $Id$

# Authority: dries
# Upstream: Ivan Tubert-Brohman <itub$cpan,org>

%define real_name Chemistry-File-MDLMol
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: MDL molfile reader and writer
Name: perl-Chemistry-File-MDLMol
Version: 0.17
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chemistry-File-MDLMol/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/I/IT/ITUB/Chemistry-File-MDLMol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Chemistry/File/MDLMol.pm
%{perl_vendorlib}/Chemistry/File/SDF.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17
- Initial package.
