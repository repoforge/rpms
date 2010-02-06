# $Id$
# Authority: dag
# Upstream: Mattia Barbon <mbarbon@users.sourceforge.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Alien-wxWidgets

Summary: Building, finding and using wxWidgets binaries
Name: perl-Alien-wxWidgets
Version: 0.50
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Alien-wxWidgets/

Source: http://search.cpan.org/CPAN/authors/id/M/MB/MBARBON/Alien-wxWidgets-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: perl(ExtUtils::CBuilder) >= 0.24
BuildRequires: perl(File::Fetch)
BuildRequires: perl(Module::Build) >= 0.28
BuildRequires: perl(Module::Pluggable) >= 2.6
BuildRequires: perl >= 5.006
BuildRequires: wget
Requires: gtk2
Requires: perl(Module::Pluggable) >= 2.6
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
Building, finding and using wxWidgets binaries.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build
./Build test

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README.txt
%doc %{_mandir}/man3/Alien::wxWidgets.3pm*
%doc %{_mandir}/man3/Alien::wxWidgets::Utility.3pm*
%dir %{perl_vendorarch}/Alien/
%{perl_vendorarch}/Alien/wxWidgets/
%{perl_vendorarch}/Alien/wxWidgets.pm
#%dir %{perl_vendorlib}/Alien/
#%{perl_vendorlib}/Alien/wxWidgets/
#%{perl_vendorlib}/Alien/wxWidgets.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.50-1
- Updated to version 0.50.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.48-1
- Updated to version 0.48.

* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.44-1
- Updated to version 0.44.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.42-1
- Updated to release 0.42.

* Sat Sep 27 2008 Dag Wieers <dag@wieers.com> - 0.39-1
- Updated to release 0.39.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 0.37-1
- Updated to release 0.37.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
