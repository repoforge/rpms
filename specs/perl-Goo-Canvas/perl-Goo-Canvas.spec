# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Goo-Canvas

Summary: Perl interface to the GooCanvas
Name: perl-Goo-Canvas
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Goo-Canvas/

Source: http://search.cpan.org/CPAN/authors/id/Y/YE/YEWENBIN/Goo-Canvas-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Goo/Goo-Canvas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: goocanvas-devel
BuildRequires: perl

%description
Perl interface to the GooCanvas.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Goo::Canvas.3pm*
%dir %{perl_vendorarch}/auto/Goo/
%{perl_vendorarch}/auto/Goo/Canvas/
%dir %{perl_vendorarch}/Goo/
%{perl_vendorarch}/Goo/Canvas.pm

%changelog
* Thu Jun 03 2010 Dag Wieers <dag@wieers.com - 0.06-1
- Initial package. (using DAR)
