# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graph

Summary: Graph operations
Name: perl-Graph
Version: 0.91
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graph/

Source: http://www.cpan.org/modules/by-module/Graph/Graph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This modules contains functions for manipulating graphics.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Graph.3pm*
%doc %{_mandir}/man3/Graph::*.3pm*
%doc %{_mandir}/man3/Heap071::*.3pm*
%{perl_vendorlib}/Graph/
%{perl_vendorlib}/Graph.pm
%{perl_vendorlib}/Graph.pod
%{perl_vendorlib}/Heap071/
%{perl_vendorlib}/auto/Heap071/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.91-1
- Updated to version 0.91.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.84-1
- Updated to release 0.84.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Updated to release 0.81.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.74-1
- Updated to release 0.74.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.69-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.69-1
- Updated to release 0.69.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.65-1
- Updated to release 0.65.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.20105-1
- Initial package.
