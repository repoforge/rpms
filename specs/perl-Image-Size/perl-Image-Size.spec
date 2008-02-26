# $Id$
# Authority: dries
# Upstream: Randy J. Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Size
%define real_version 3.100001

Summary: Library to extract height/width from images
Name: perl-Image-Size
Version: 3.1.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Size/

Source: http://www.cpan.org/modules/by-module/Image/Image-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
Requires: perl >= 1:5.6

%description
A library to extract height/width from images.

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README README.Win32 SIGNATURE
%doc %{_mandir}/man1/imgsize.1*
%doc %{_mandir}/man3/Image::Size.3pm*
%{_bindir}/imgsize
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Size/
%{perl_vendorlib}/Image/Size.pm
%dir %{perl_vendorlib}/auto/Image/
%{perl_vendorlib}/auto/Image/Size/

%changelog
* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 3.1-1
- Updated to release 3.1.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.992
- Initial package.
