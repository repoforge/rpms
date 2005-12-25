# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GD

Summary: GD Perl interface to the GD Graphics Library
Name: perl-GD
Version: 2.30
Release: 2
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD/

Source: http://www.cpan.org/modules/by-module/GD/GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, gd-devel >= 2.0.12, libpng-devel, zlib-devel
BuildRequires: freetype-devel, libjpeg-devel, XFree86-devel
Requires: perl >= 0:5.8.0

%description
perl-GD is a Perl interface to the gd graphics library. GD allows you
to create color drawings using a large number of graphics primitives,
and emit the drawings as PNG files.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	-options "JPEG,FT,XPM,PNG,GIF" \
	-lib_gd_path "%{_libdir}" \
	-lib_ft_path "%{_libdir}" \
	-lib_png_path "%{_libdir}" \
	-lib_jpeg_path "%{_libdir}" \
	-lib_xpm_path "%{_libdir}" \
	-lib_zlib_path "%{_libdir}" \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/GD.pm
%{perl_vendorarch}/GD/
%{perl_vendorarch}/auto/GD/
%{perl_vendorarch}/qd.pl
%{_bindir}/bdf2gdfont.pl

%changelog
* Sun Dec 25 2005 Dag Wieers <dag@wieers.com> - 2.30-2
- Added PNG support. (Why was it gone ?)

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.30-1
- Updated to release 2.30.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 2.16-1
- Updated to release 2.16.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 2.11-0
- Initial package. (using DAR)
