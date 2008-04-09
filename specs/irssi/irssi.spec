# $Id$
# Authority: dag
# Upstream: <irssi-dev$dragoncat,net>

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)

Summary: Modular text-mode IRC client
Name: irssi
Version: 0.8.12
Release: 1
License: GPL
Group: Applications/Communications
URL: http://irssi.org/

Source: http://mirror.irssi.org/irssi-%{version}.tar.bz2
Patch0: irssi-0.8.10-dcc-unregister.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++,
BuildRequires: glib2-devel
BuildRequires: imlib-devel
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: zlib-devel
%{?_with_gc:BuildRequires: libgc-devel}

Provides: irssi-devel = %{version}-%{release}
Obsoletes: irssi-devel <= %{version}-%{release}

%description
Irssi is a modular IRC client that currently has only text mode user
interface, but 80-90% of the code isn't text mode specific so other UI
could be created pretty easily. Also, Irssi isn't really even IRC
specific anymore, there's already a working SILC module available.
Support for other protocols like ICQ could be created some day too.

%prep
%setup
#patch0 -p0
%{?el3:%{__perl} -pi.orig -e 's|^CFLAGS = |CFLAGS = -I/usr/kerberos/include |' src/core/Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^CFLAGS = |CFLAGS = -I/usr/kerberos/include |' src/core/Makefile.in}

%build
%configure \
    --enable-ipv6 \
    --enable-ssl \
    --with-bot \
%{?_with_gc:--with-gc} \
    --with-glib2 \
    --with-imlib \
    --with-ncurses \
    --with-perl="yes" \
    --with-perl-lib="vendor" \
    --with-plugins \
    --with-proxy \
    --with-textui
#    --with-perl-lib="%(dirname %{buildroot}%{perl_vendorarch})" \
#    --with-perl="module" \
#    --with-perl-lib="%{buildroot}%{perl_vendorarch}" \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall PERL_INSTALL_ROOT="%{buildroot}" INSTALL="%{__install} -p"
#makeinstall PREFIX="%{buildroot}%{_prefix}"
#   PERL_USE_LIB="%{buildroot}%{perl_vendorarch}"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
%{__rm} -f %{buildroot}%{_libdir}/irssi/modules/*.{a,la}
%{__rm} -f %{buildroot}%{perl_vendorarch}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc docs/*.html docs/*.txt
%doc %{_mandir}/man1/irssi.1*
%config(noreplace) %{_sysconfdir}/irssi.conf
%{_bindir}/botti
%{_bindir}/irssi
%{_datadir}/irssi/
%{perl_vendorarch}/Irssi/
%{perl_vendorarch}/Irssi.pm
%{perl_vendorarch}/auto/Irssi/
%{_includedir}/irssi/
%{_libdir}/irssi/
%exclude %{_docdir}/irssi/

%changelog
* Wed Apr 09 2008 Dag Wieers <dag@wieers.com> - 0.8.12-1
- Updated to release 0.8.12.

* Thu Aug 02 2007 Dag Wieers <dag@wieers.com> - 0.8.10a-4
- Disabled libgc for all distributions. (And be done with this mess)

* Fri Jul 27 2007 Dag Wieers <dag@wieers.com> - 0.8.10a-3
- Rebuild against libgc-7.0.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.8.10a-2
- Remove --with-perl="module" as it disables /script support. (Tom�Laovika)

* Fri Apr 20 2007 Dag Wieers <dag@wieers.com> - 0.8.10a-1
- Updated to release 0.8.10a.
- Fixed invalid pointer when DCC unregister. (Saleem Abdulrasool)
- Disabled GC because it causes segfaults on RHEL5.

* Sun Dec 11 2005 Dag Wieers <dag@wieers.com> - 0.8.10-1
- Updated to release 0.8.10.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.10-0.rc7
- Updated to release 0.8.10-rc7.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.8.9-4
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 0.8.9-2
- Another attempt to fix the brokeness of the irssi perl stuff.
- Now using %%perl_vendorlib instead of the correcter %%perl_archlib.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.8.9-1
- Rebuild against new fc1 perl package. (Christopher Stone)

* Fri Dec 12 2003 Dag Wieers <dag@wieers.com> - 0.8.9-0
- Updated to release 0.8.9.

* Fri Dec 12 2003 Dag Wieers <dag@wieers.com> - 0.8.9-0
- Updated to release 0.8.9.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.8.8-0
- Fixed the longstanding problem with the perl modules !! (Rudolf Kastl)
- Updated to release 0.8.8.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.8.6-4
- Fixed compilation-errors for RH9.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.8.6-3
- Fixed the Perl module problem.

* Fri Jan 17 2003 Dag Wieers <dag@wieers.com> - 0.8.6-0
- Initial package. (using DAR)
