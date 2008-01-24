# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Tar

Summary: Archive-Tar module for perl
Name: perl-Archive-Tar
Version: 1.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Tar/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Tar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Module for manipulations of tar archives.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man1/ptar.1*
%doc %{_mandir}/man1/ptardiff.1*
%doc %{_mandir}/man3/Archive::Tar.3pm*
%doc %{_mandir}/man3/Archive::Tar::File.3pm*
%{_bindir}/ptar
%{_bindir}/ptardiff
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Tar/
%{perl_vendorlib}/Archive/Tar.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Updated to release 1.30.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.08-0
- Initial package. (using DAR)
