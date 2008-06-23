# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Find-Rule-VCS

Summary: Exclude files/directories for Version Control Systems
Name: perl-File-Find-Rule-VCS
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule-VCS/

Source: http://www.cpan.org/modules/by-module/File/File-Find-Rule-VCS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Exclude files/directories for Version Control Systems.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/File::Find::Rule::VCS.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Find/
%dir %{perl_vendorlib}/File/Find/Rule/
#%{perl_vendorlib}/File/Find/Rule/VCS/
%{perl_vendorlib}/File/Find/Rule/VCS.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
