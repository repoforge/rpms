# $Id$
# Authority: dag
# Upstream: <irssi-dev$dragoncat,net>

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)

%define real_version 0.8.10

Summary: Modular text-mode IRC client
Name: irssi
Version: 0.8.10
Release: 1
License: GPL
Group: Applications/Communications
URL: http://irssi.org/

Source: http://mirror.irssi.org/irssi-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, ncurses-devel, libgc-devel, gcc-c++
BuildRequires: autoconf, automake, ncurses-devel, imlib-devel

%description
Irssi is a modular IRC client that currently has only text mode user
interface, but 80-90% of the code isn't text mode specific so other UI
could be created pretty easily. Also, Irssi isn't really even IRC
specific anymore, there's already a working SILC module available.
Support for other protocols like ICQ could be created some day too.

%prep
%setup -n %{name}-%{real_version}
%{?el3:%{__perl} -pi.orig -e 's|^CFLAGS = |CFLAGS = -I/usr/kerberos/include |' src/core/Makefile.in}
%{?rh9:%{__perl} -pi.orig -e 's|^CFLAGS = |CFLAGS = -I/usr/kerberos/include |' src/core/Makefile.in}

%build
%configure \
	--with-plugins \
        --enable-ipv6 \
        --with-textui \
	--with-imlib \
        --with-bot \
        --with-proxy \
	--with-perl="yes" \
	--enable-ssl \
	--with-glib2 \
        --with-ncurses \
	--with-gc \
	--with-perl-lib="%(dirname %{buildroot}%{perl_vendorarch})"
#	--with-perl-lib="%{buildroot}%{perl_vendorarch}"
#	--with-perl-lib="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}"
#	PERL_USE_LIB="%{buildroot}%{perl_vendorarch}"

%{__rm} -f %{buildroot}%{_libdir}/irssi/modules/*.{a,la} \
		%{buildroot}%{perl_vendorarch}/auto/Irssi/.packlist \
		%{buildroot}%{perl_vendorarch}/auto/Irssi/*/.packlist \
		%{buildroot}%{perl_vendorarch}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc docs/*.html docs/*.txt
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/botti
%{_bindir}/irssi
%{_libdir}/irssi/
%{_datadir}/irssi/
%{perl_vendorarch}/Irssi/
%{perl_vendorarch}/Irssi.pm
%{perl_vendorarch}/auto/Irssi/
%{_includedir}/irssi/
%exclude %{_docdir}/irssi/
#%exclude %{perl_vendorarch}

%changelog
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
