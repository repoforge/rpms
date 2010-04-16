# $Id$
# Authority: shuff
# Upstream: Cosmin Truta <ctruta$gmail,com>

Summary: Advanced PNG optimizer
Name: optipng
Version: 0.6.4
Release: 1%{?dist}
License: zlib/libpng
Group: Applications/Multimedia
URL: http://optipng.sourceforge.net/

Source: http://prdownloads.sourceforge.net/optipng/optipng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bash, binutils, gcc, make
BuildRequires: glibc-devel
BuildRequires: zlib-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks
and corrections.


%prep
%setup

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} \
    --with-system-zlib
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__install} -m0755 -d %{buildroot}%{_mandir}/man1
%{__gzip} man/optipng.1
%{__install} -m0755 man/optipng.1.gz %{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.txt README.txt doc/*
%doc %{_mandir}/man?/*
%{_bindir}/*
%exclude /usr/man

%changelog
* Fri Apr 16 2010 Steve Huff <shuff@vecna.org> - 0.6.4-1
- Updated to 0.6.4.
- Converted to new configure script.

* Tue Feb 02 2010 Steve Huff <shuff@vecna.org> - 0.6.3-1
- Initial package.
