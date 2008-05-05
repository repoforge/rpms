# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Flat

Summary: Implements a flat filesystem
Name: perl-File-Flat
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Flat/

Source: http://www.cpan.org/modules/by-module/File/File-Flat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(Test::ClassAPI) >= 1.04
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Implements a flat filesystem.

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
%doc %{_mandir}/man3/File::Flat.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/Flat/
%{perl_vendorlib}/File/Flat.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
