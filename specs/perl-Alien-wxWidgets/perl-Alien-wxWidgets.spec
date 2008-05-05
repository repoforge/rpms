# $Id$
# Authority: dag
# Upstream: Mattia Barbon <mbarbon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Alien-wxWidgets

Summary: building, finding and using wxWidgets binaries
Name: perl-Alien-wxWidgets
Version: 0.35
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Alien-wxWidgets/

Source: http://www.cpan.org/modules/by-module/Alien/Alien-wxWidgets-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(Module::Build) >= 0.26
Requires: perl >= 0:5.006

%description
building, finding and using wxWidgets binaries.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" </dev/null
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

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
