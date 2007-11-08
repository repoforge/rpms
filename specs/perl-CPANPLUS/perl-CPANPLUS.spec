# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

### This package is dangerous, we don't want it to be available as-is
# Tag: test

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CPANPLUS

Summary: Command-line access to the CPAN interface
Name: perl-CPANPLUS
Version: 0.80
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPANPLUS/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KANE/CPANPLUS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "CPANPLUS" library is an API to the "CPAN" mirrors and a collection
of interactive shells, commandline programs, daemons, etc, that use
this API.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} -pi -e 's|^ *\@ARGV = grep \{.*||g;' Makefile.PL
%{__perl} -pi -e 's|use Your::Module::Here|your use statements here|g;' lib/CPANPLUS/Internals/Constants/Report.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" AUTOINSTALL=1 SETUP=0 JFDI=1
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -rf %{buildroot}%{perl_archlib} \
  %{buildroot}%{perl_vendorarch} \
  %{buildroot}%{_mandir}/man3/CPANPLUS*Win32* \
  %{buildroot}%{perl_vendorlib}/CPANPLUS/inc/*/*/*Win32* \
  %{buildroot}%{perl_vendorlib}/CPANPLUS/inc/ \
  %{buildroot}%{_mandir}/man?/CPANPLUS::inc*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{perl_vendorlib}/CPANPLUS.pm
%{perl_vendorlib}/CPANPLUS/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.074-1
- Updated to release 0.074.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.061-1
- Updated to release 0.061.

* Thu Nov 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.055-3
- Rebuild.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.055-1
- Updated to release 0.055.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.053-2
- Don't install all the included modules.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.053-1
- Updated to release 0.053.

* Mon Jan 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.051-1
- Initial package.
