# $Id$
# Authority: dag
# Upstream: Lincoln Stein <lstein$cshl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define real_name GD

Summary: Interface to Gd Graphics Library
Name: perl-GD
Version: 2.44
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD/

Source: http://www.cpan.org/modules/by-module/GD/GD-%{version}.tar.gz
Patch0: perl-GD-2.41-Group.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: gd-devel >= 2.0.28
BuildRequires: gd-progs >= 2.0.28
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: freetype-devel
BuildRequires: libjpeg-devel
BuildRequires: perl(ExtUtils::MakeMaker)
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
Requires: perl >= 2:5.8.0
Requires: gd >= 2.0.28
Requires: libpng
Requires: zlib
Requires: freetype
Requires: libjpeg

%description
perl-GD is a Perl interface to the gd graphics library. GD allows you
to create color drawings using a large number of graphics primitives,
and emit the drawings as PNG files.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .group

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
    -options "JPEG,FT,XPM,PNG,GIF" \
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
%doc ChangeLog MANIFEST META.yml README README.QUICKDRAW README.unix
%doc %{_mandir}/man1/bdf2gdfont.pl.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/bdf2gdfont.pl
%{perl_vendorarch}/GD/
%{perl_vendorarch}/GD.pm
%{perl_vendorarch}/auto/GD/
%{perl_vendorarch}/qd.pl

%changelog
* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 2.44-1
- Updated to version 2.44.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2.43-1
- Updated to version 2.43.

* Sat Oct 11 2008 Dag Wieers <dag@wieers.com> - 2.41-2
- Added a patch to install GD::Group. (Bob Kinney)

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.41-1
- Updated to release 2.41.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.39-1
- Updated to release 2.39.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Sun Dec 25 2005 Dag Wieers <dag@wieers.com> - 2.30-2
- Added PNG support. (Why was it gone ?)

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.30-1
- Updated to release 2.30.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 2.16-1
- Updated to release 2.16.

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 2.11-0
- Initial package. (using DAR)
