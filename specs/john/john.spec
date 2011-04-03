# $Id$
# Authority: dag

Summary: John the Ripper password cracker
Name: john
Version: 1.7.6
Release: 3%{?dist}
License: GPL
Group: Applications/System
URL: http://www.openwall.com/john/

#Source: http://www.openwall.com/john/f/john-%{version}.tar.bz2
Source: http://www.openwall.com/john/g/john-%{version}.tar.bz2
Patch: ftp://ftp.openwall.com/pub/projects/john/contrib/john-1.7.6-jumbo-12.diff.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
John the Ripper is a fast password cracker. Its primary purpose is to
detect weak Unix passwords, but a number of other hash types are
supported as well.

%prep
%setup
%patch -p1

%{__perl} -pi.orig -e 's|^(\#define CFG_FULL_NAME)\s.+$|$1 "%{_sysconfdir}/john.conf"|' src/params.h

%build
CFLAGS="-c %{optflags} -DJOHN_SYSTEMWIDE -fomit-frame-pointer"
%ifarch %{ix86}
%define _with_cpu_fallback 1
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS -DCPU_FALLBACK=1" linux-x86-any
%{__mv} -f run/john run/john-non-mmx
%{__make} -C src clean
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS -DCPU_FALLBACK=1" linux-x86-mmx
%{__mv} -f run/john run/john-non-sse
%{__make} -C src clean
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS -DCPU_FALLBACK=1" linux-x86-sse2
%endif
%ifarch x86_64
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS" linux-x86-64
%endif
%ifarch alpha alphaev5 alphaev56 alphapca56 alphaev6 alphaev67
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS" linux-alpha
%endif
%ifarch sparc sparcv9
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS" linux-sparc
%endif
%ifarch ppc
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS" linux-ppc32
%endif
%ifarch ppc64
%{__make} %{?_smp_mflags} -C src CFLAGS="$CFLAGS" linux-ppc64
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 run/john.conf %{buildroot}%{_sysconfdir}/john.conf
%{__install} -Dp -m0755 run/john %{buildroot}%{_bindir}/john

%{__install} -d -m0755 %{buildroot}%{_datadir}/john/
%{__install} -p -m0644 run/*.chr run/password.lst %{buildroot}%{_datadir}/john/

%{__ln_s} -f john %{buildroot}%{_bindir}/unafs
%{__ln_s} -f john %{buildroot}%{_bindir}/unique
%{__ln_s} -f john %{buildroot}%{_bindir}/unshadow

%if %{?_with_cpu_fallback:1}0
%{__install} -d -m0755 -p %{buildroot}%{_libexecdir}/john
%{__install} -m0700 run/john-* %{buildroot}%{_libexecdir}/john/
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/* run/mailer
%config(noreplace) %{_sysconfdir}/john.conf
%{_bindir}/john
%{_bindir}/unafs
%{_bindir}/unique
%{_bindir}/unshadow
%{_datadir}/john/
%if %{?_with_cpu_fallback:1}0
%{_libexecdir}/john/
%endif

%changelog
* Sun Apr 03 2011 Yury V. Zaytsev <yury@shurup.com> - 1.7.6-3
- Fixed x86 builds (thanks to Alexander Kirillov!)
- Updated to the latest jumbo patch version.

* Sun Jan 24 2011 Yury V. Zaytsev <yury@shurup.com> - 1.7.6-2
- Added jumbo patch and fixed builds.
- Thanks to Alexander Kirillov!

* Mon Jun 14 2010 Dag Wieers <dag@wieers.com> - 1.7.6-1
- Updated to release 1.7.6.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 1.7.0.2-3
- Fixed systemwide installation. (Solar Designer)
- Fixed cpu fallback. (Solar Designer)

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 1.7.0.2-1
- Updated to release 1.7.0.2.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
