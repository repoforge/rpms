# $Id$
# Authority: shuff
# Upstream: Felix von Leitner <felix$fefe,de>

Summary: GPL reimplementation of libdjb
Name: libowfat
Version: 0.28
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.fefe.de/libowfat/

Source: http://dl.fefe.de/libowfat-%{version}.tar.bz2
Patch0: libowfat-0.28_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge
Requires: pkgconfig

%description
Short answer: reimplement libdjb under GPL.

Long answer: One of the best ways to learn good programming practices is to
read others people's code. I have read the source code from a lot of people.
One of the most inspiring moments of my career as C programmer was to look at
Dan Bernstein's code. While most programmers stumble about bad APIs throughout
their life, Dan started not only question them, but he defined new and better
APIs and implemented them.

This code is only used in his own projects so far. The main reason is that Dan
does not package them in a convenient way, but many people have problems with
Dan's (lack of) licensing statements. To get rid of the first reason, I started
to extract the libraries from Dan's code a while ago. I called that project
libdjb and used the code in my own programs. I even extended the API at a few
points.

While the licensing issue did not concern me at first, Debian would only add my
programs to the non-free section if at all. I also got several inquiries about
the licensing state of my code.

So I decided to reimplement libdjb to use Dan's interfaces (with my earlier
extensions) but my implementation and place the result under the GNU General
Public License.

%prep
%setup
%patch0 -p1

%build
%{__make} %{?_smp_mflags} prefix="%{_prefix}" LIBDIR="%{_libdir}/libowfat-%{version}" INCLUDEDIR="%{_includedir}/libowfat-%{version}" MAN3DIR="%{_mandir}/man3"

# make a pkgconfig file
%{__cat} <<'PKGCONFIG' >libowfat.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}
version=%{version}

Name: libowfat
Description: GPL reimplementation of libdjb
Version: ${version}
Libs: -L${libdir}/libowfat-${version} -lowfat
Cflags: -I${includedir}/libowfat-${version}
PKGCONFIG

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" LIBDIR="%{_libdir}/libowfat-%{version}" INCLUDEDIR="%{_includedir}/libowfat-%{version}" MAN3DIR="%{_mandir}/man3"

# install the pkgconfig file
%{__install} -d -m0755 %{buildroot}%{_libdir}/pkgconfig
%{__install} -m0755 libowfat.pc %{buildroot}%{_libdir}/pkgconfig

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README TODO examples/
%doc %{_mandir}/man?/*
%{_includedir}/libowfat-%{version}/*.h
%{_libdir}/libowfat-%{version}/*.a
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Aug 19 2011 Steve Huff <shuff@vecna.org> - 0.28-1
- Initial package.
