# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define real_name Graphics-ColorPicker
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Creates a html form for selecting HEX color numbers
Name: perl-Graphics-ColorPicker
Version: 0.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorPicker/

Source: http://www.cpan.org/modules/by-module/Graphics/Graphics-ColorPicker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graphics/ColorPicker.pm
%{perl_vendorlib}/auto/Graphics/ColorPicker

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
