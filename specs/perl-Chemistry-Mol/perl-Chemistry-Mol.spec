# $Id$

# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define real_name Chemistry-Mol
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Molecule object toolkit
Name: perl-Chemistry-Mol
Version: 0.32
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chemistry-Mol/

Source: http://search.cpan.org/CPAN/authors/id/I/IT/ITUB/Chemistry-Mol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
his toolkit includes basic objects and methods to describe molecules. It
consists of several modules: Chemistry::Mol, Chemistry::Atom,
Chemistry::Bond, and Chemistry::File. These are the core modules of the 
PerlMol toolkit; see http://www.perlmol.org/.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Chemistry/*.pm
%{perl_vendorlib}/Chemistry/File
%{perl_vendorlib}/Chemistry/Tutorial.pod
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
