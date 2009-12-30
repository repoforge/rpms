# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-ShareDir

Summary: Locate per-dist and per-module shared files
Name: perl-File-ShareDir
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-ShareDir/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/File-ShareDir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Inspector) >= 1.12
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Params::Util) >= 0.07
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl >= 5.005
Requires: perl(Carp)
Requires: perl(Class::Inspector) >= 1.12
Requires: perl(File::Spec) >= 0.80
Requires: perl(Params::Util) >= 0.07
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

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
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
