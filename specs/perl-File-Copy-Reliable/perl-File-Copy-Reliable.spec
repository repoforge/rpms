# $Id$
# Authority: dries
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Copy-Reliable

Summary: Copy and move files with extra checking
Name: perl-File-Copy-Reliable
Version: 0.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Copy-Reliable/

Source: http://www.cpan.org/modules/by-module/File/File-Copy-Reliable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Copy and move files with extra checking.

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
%doc %{_mandir}/man3/File::Copy::Reliable.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Copy/
#%{perl_vendorlib}/File/Copy/Reliable/
%{perl_vendorlib}/File/Copy/Reliable.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.32-1
- Updated to version 0.32.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
