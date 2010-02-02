# $Id$
# Authority: shuff
# Upstream: Cosmin Truta <ctruta$gmail,com>

Summary: Advanced PNG optimizer
Name: optipng
Version: 0.6.3
Release: 1%{?dist}
License: zlib/libpng
Group: Applications/Multimedia
URL: http://optipng.sourceforge.net/

Source: http://prdownloads.sourceforge.net/optipng/optipng-%{version}.tar.gz
Patch0: optipng-0.6.3_prefix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bash, binutils, gcc, make
BuildRequires: glibc-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks
and corrections.


%prep
%setup
%patch0 -p1

%build
pushd src
%{__make} %{?_smp_mflags} -f scripts/gcc.mak PREFIX=%{_prefix} MANDIR=%{_mandir}


popd

%install
%{__rm} -rf %{buildroot}
pushd src
%{__make} -f scripts/gcc.mak install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir}
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.txt README.txt doc/
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Feb 02 2010 Steve Huff <shuff@vecna.org> - 0.6.3-1
- Initial package.
