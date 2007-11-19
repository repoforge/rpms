# $Id$
# Authority: dries
# Upstream: Steffen Schwigon <schwigon$webit,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PDF-FDF-Simple

Summary: Read and write (Acrobat) FDF files
Name: perl-PDF-FDF-Simple
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PDF-FDF-Simple/

Source: http://www.cpan.org/modules/by-module/PDF/PDF-FDF-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Module::Build)
Requires: perl >= 1:5.6.1

%description
PDF::FDF::Simple helps creating and extracting FDF files. It is
meant to be a simple replacement for the Adobe FdfToolkit when you
just want to read or create fdf files.

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
%doc ChangeLog INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/PDF::FDF::Simple.3pm*
%dir %{perl_vendorlib}/PDF/
%dir %{perl_vendorlib}/PDF/FDF/
#%{perl_vendorlib}/PDF/FDF/Simple/
%{perl_vendorlib}/PDF/FDF/Simple.pm
%{perl_vendorlib}/PDF/FDF/Simple.pod

%changelog
* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
