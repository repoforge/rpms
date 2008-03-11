# $Id$
# Authority: dries
# Upstream: Mike Schilli <cpan$perlmeister,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Tar-Wrapper

Summary: API wrapper around the 'tar' utility
Name: perl-Archive-Tar-Wrapper
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Tar-Wrapper/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Tar-Wrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Archive::Tar::Wrapper is an API wrapper around the 'tar' command line
utility. It never stores anything in memory, but works on temporary
directory structures on disk instead. It provides a mapping between the
logical paths in the tarball and the 'real' files in the temporary
directory on disk.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README eg/
%doc %{_mandir}/man3/Archive::Tar::Wrapper.3pm*
%dir %{perl_vendorlib}/Archive/
%dir %{perl_vendorlib}/Archive/Tar/
#%{perl_vendorlib}/Archive/Tar/Wrapper/
%{perl_vendorlib}/Archive/Tar/Wrapper.pm

%changelog
* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
