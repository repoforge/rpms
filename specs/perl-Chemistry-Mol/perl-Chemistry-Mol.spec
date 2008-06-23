# $Id$
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Mol

Summary: Molecule object toolkit
Name: perl-Chemistry-Mol
Version: 0.36
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chemistry-Mol/

Source: http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Mol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
his toolkit includes basic objects and methods to describe molecules. It
consists of several modules: Chemistry::Mol, Chemistry::Atom,
Chemistry::Bond, and Chemistry::File. These are the core modules of the
PerlMol toolkit; see http://www.perlmol.org/.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/*.pm
%{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/Tutorial.pod

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
