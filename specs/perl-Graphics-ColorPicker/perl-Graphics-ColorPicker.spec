# $Id$
# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graphics-ColorPicker

Summary: Creates a html form for selecting HEX color numbers
Name: perl-Graphics-ColorPicker
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorPicker/

Source: http://www.cpan.org/modules/by-module/Graphics/Graphics-ColorPicker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module generates a set of palettes to select a HEX or DECIMAL color
number via a web browser. make_page() can be called by "javascript" from
your web page and will set the HEX value in a variable in the calling
page and scope. The selector page can be created for 24 million or web
safe colors only.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Graphics::ColorPicker.3pm*
%dir %{perl_vendorlib}/Graphics/
%dir %{perl_vendorlib}/auto/Graphics/
%{perl_vendorlib}/auto/Graphics/ColorPicker/
#%{perl_vendorlib}/Graphics/ColorPicker/
%{perl_vendorlib}/Graphics/ColorPicker.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
