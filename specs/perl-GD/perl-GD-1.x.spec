# $Id$
# Authority: dag

%define real_name GD

Summary: GD Perl interface to the GD Graphics Library
Name: perl-GD
Version: 1.41
Release: 1
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDS/GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, gd-devel >= 1.8.4, libpng-devel, zlib-devel
BuildRequires: freetype-devel, libjpeg-devel, XFree86-devel
Requires: perl >= 0:5.8.0

%description
perl-GD is a Perl interface to the gd graphics library. GD allows you
to create color drawings using a large number of graphics primitives,
and emit the drawings as PNG files.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|^#!/.*bin/perl|#!%{__perl}|i;' *.pl

%build
echo "y\ny\ny\ny\n" |
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	-options "JPEG,FT,XPM" \
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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Wed Apr 14 2004 Dag Wieers <dag@wieers.com> - 1.41-1
- Fixed /usr/local/bin/perl in qd.pl. (Tom Diehl)

* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1.41-0
- Initial package. (using DAR)
