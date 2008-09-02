# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Compare

Summary: Compare two images in a variety of ways
Name: perl-Image-Compare
Version: 0.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Compare/

Source: http://www.cpan.org/modules/by-module/Image/Image-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Imager)
BuildRequires: perl(LWP)
BuildRequires: perl(Regexp::Common), perl(Test::Pod), perl(Test::Pod::Coverage), perl(Pod::Coverage)

%description
Image::Compare is a module for performing comparisons of images.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Image::Compare.3pm*
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Compare/
%{perl_vendorlib}/Image/Compare.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
