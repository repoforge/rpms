# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan@ali.as>, L<http://ali.as/>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Math-Constrain

Summary: Scaling math used in image size constraining (such
Name: perl-Image-Math-Constrain
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Math-Constrain/

Source: http://www.cpan.org/modules/by-module/Image/Image-Math-Constrain-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Scaling math used in image size constraining (such.

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
%doc %{_mandir}/man3/Image::Math::Constrain.3pm*
%dir %{perl_vendorlib}/Image/
%dir %{perl_vendorlib}/Image/Math/
%{perl_vendorlib}/Image/Math/Constrain.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
