# $Id$
# Authority: shuff
# Upstream: Andrew Schofield <andrew_s$fahmon,net>

%define real_name FahMon

Summary: Folding@Home client monitor
Name: fahmon
Version: 2.3.99.1
Release: 1%{?dist}
License: GPL
Group: Applications/X11
URL: http://fahmon.net/

Source: http://fahmon.net/downloads/FahMon-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc-c++, make, autoconf, automake
BuildRequires: compat-gcc-34-g77
BuildRequires: curl-devel >= 7.15.0
BuildRequires: doxygen
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: rpm-macros-rpmforge
BuildRequires: wxGTK-devel >= 2.8.0
BuildRequires: zlib-devel
Requires: %{_datadir}/applications
Requires: %{_iconsbasedir}

# nobody should depend on us for libwxcurl
%filter_from_provides /libwxcurl/d
%filter_from_requires /libwxcurl/d
%filter_setup

%description
FahMon is a GUI monitor for Folding@Home clients.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-dependency-tracking \
    --disable-static
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f fahmon.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TEMPLATE_SYNTAX THANKS
#%doc doc/
%{_bindir}/fahmon
%{_datadir}/applications/fahmon.desktop
%{_datadir}/fahmon/
%{_datadir}/pixmaps/fahmon/
%{_iconsbasedir}/*/apps/fahmon.png
%{_libdir}/libwxcurl.so.*
%exclude %{_libdir}/libwxcurl.la
%exclude %{_libdir}/libwxcurl.so

%changelog
* Sun Apr 04 2010 Steve Huff <shuff@vecna.org> - 2.3.99.1-1
- Initial package.
