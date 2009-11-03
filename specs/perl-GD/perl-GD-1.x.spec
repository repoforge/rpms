# $Id$
# Authority: dag
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define real_name GD

Summary: GD Perl interface to the GD Graphics Library
Name: perl-GD
Version: 1.41
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD/

Source: http://www.cpan.org/modules/by-module/GD/GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: gd-devel >= 1.8.4
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel
BuildRequires: libjpeg-devel
Requires: perl
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
perl-GD is a Perl interface to the gd graphics library. GD allows you
to create color drawings using a large number of graphics primitives,
and emit the drawings as PNG files.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|^#!/.*bin/perl|#!%{__perl}|i;' *.pl

%build
echo "y\ny\ny\ny\n" |
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    -options "JPEG,FT,XPM" \
    -lib_gd_path "%{_libdir}" \
    -lib_ft_path "%{_libdir}" \
    -lib_png_path "%{_libdir}" \
    -lib_jpeg_path "%{_libdir}" \
    -lib_xpm_path "%{_libdir}" \
    -lib_zlib_path "%{_libdir}"
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
%doc ChangeLog MANIFEST README README.QUICKDRAW README.unix
%doc %{_mandir}/man3/GD.3pm*
%{perl_vendorarch}/GD.pm
%{perl_vendorarch}/auto/GD/
%{perl_vendorarch}/patch_gd.pl
%{perl_vendorarch}/qd.pl

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.41-2
- Cosmetic cleanup.

* Wed Apr 14 2004 Dag Wieers <dag@wieers.com> - 1.41-1
- Fixed /usr/local/bin/perl in qd.pl. (Tom Diehl)

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.41-0
- Initial package. (using DAR)
