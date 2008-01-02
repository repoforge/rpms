# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Vec

Summary: Object-Oriented Vector Math Methods in Perl
Name: perl-Math-Vec
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Vec/

Source: http://www.cpan.org/modules/by-module/Math/Math-Vec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Object-Oriented Vector Math Methods in Perl.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Math::Vec.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Vec.pm

%changelog
* Wed Jan 02 2008 Fabian Arrotin <fabian.arrotin@arrfab.net> 
- Added a missing BuildRequires: perl(Module::Build) to build properly in Mock
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
