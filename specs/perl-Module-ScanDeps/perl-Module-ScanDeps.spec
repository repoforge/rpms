# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-ScanDeps

Summary: Recursively scan Perl programs for dependencies
Name: perl-Module-ScanDeps
Version: 0.66
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-ScanDeps/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/Module-ScanDeps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Module::ScanDeps, a module to recursively
scan Perl programs for dependencies.

An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects,
PAR and App::Packer.  Please see their respective documentations on CPAN
for further information.

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
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/scandeps*
%{_bindir}/scandeps.pl
%{perl_vendorlib}/Module/ScanDeps.pm
%{perl_vendorlib}/Module/ScanDeps/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.66-1
- Updated to release 0.66.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Updated to release 0.63.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.60-1
- Updated to release 0.60.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Updated to release 0.57.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
