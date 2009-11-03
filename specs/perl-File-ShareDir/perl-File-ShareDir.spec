# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-ShareDir

Summary: Locate per-dist and per-module shared files
Name: perl-File-ShareDir
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-ShareDir/

Source: http://www.cpan.org/modules/by-module/File/File-ShareDir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Locate per-dist and per-module shared files.

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
%doc %{_mandir}/man3/File::ShareDir.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/ShareDir.pm
#%dir %{perl_vendorlib}/auto/File/
#%{perl_vendorlib}/auto/File/ShareDir/
%exclude %{perl_vendorlib}/auto/share/

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
