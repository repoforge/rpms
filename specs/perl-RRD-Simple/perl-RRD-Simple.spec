# $Id$
# Authority: dries
# Upstream: Nicola Worthington <nicolaw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RRD-Simple

Summary: Simple interface to create and store data in RRD files
Name: perl-RRD-Simple
Version: 1.44
Release: 1
License: Apache 2.0
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RRD-Simple/

Source: http://www.cpan.org/authors/id/N/NI/NICOLAW/RRD-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
Conflicts: perl(RRDTool::Managed)

%description
RRD::Simple provides a simple interface to RRDTool's RRDs module.
This module does not currently offer the graph, fetch or info
methods that are available in the RRDs module.

It does howeve create RRD files with a sensible set of default RRA
(Round Robin Archive) definitions, and can dynamically add new
data source names to an existing RRD file.

This module is ideal for quick and simple storage of data within an
RRD file if you do not need to, nor want to bother defining custom
RRA definitions.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST META.yml NOTICE README TODO complain.txt examples/
%doc %{_mandir}/man3/RRD::Simple.3pm*
%doc %{_mandir}/man3/RRD::Simple::*.3pm*
%dir %{perl_vendorlib}/RRD/
#%{perl_vendorlib}/RRD/Simple/
%{perl_vendorlib}/RRD/Simple/
%{perl_vendorlib}/RRD/Simple.pm

%changelog
* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.44-1
- Updated to release 1.44.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.43-1
- Updated to release 1.43.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Updated to release 1.40.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.34-1
- Updated to release 1.34.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.29-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.29-2
- Fixed the license (Apache 2.0) and added the LICENSE and
  NOTICE files, thanks to Nicola Worthington.

* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.29-1
- Updated to release 1.29.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
