# $Id: alpine-test.spec 9166 2010-10-07 13:05:43Z dag $
# Authority: dag

### EL2 ships with pine-4.44-20
%{?el2:# Tag: rfx}

%{?el6:%define _without_inews 1}

%define real_name re-alpine

Summary: Alternative Pine mail user agent implementation
Name: alpine
Version: 2.02
Release: 1%{?dist}
License: Apache License
Group: Applications/Internet
URL: http://www.washington.edu/alpine/

Source0: http://dl.sf.net/project/re-alpine/re-alpine-%{version}.tar.bz2
Source1: pine.conf
Source2: pine.conf.fixed
### http://staff.washington.edu/chappa/alpine/patches/
#Patch0: http://staff.washington.edu/chappa/alpine/patches/alpine-2.00/maildir.patch.gz
Patch0: alpine-2.00-maildir.patch
#Patch1: http://staff.washington.edu/chappa/alpine/patches/alpine-2.00/fillpara.patch.gz
Patch1: alpine-2.00-fillpara.patch
#Patch2: http://staff.washington.edu/chappa/alpine/patches/alpine-2.00/rules.patch.gz
Patch2: alpine-2.00-rules.patch
#Patch3: http://staff.washington.edu/chappa/alpine/patches/alpine-2.00/searchheader.patch.gz
Patch3: alpine-2.00-searchheader.patch
Patch4: alpine-1.10-select-bold-x.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aspell
#BuildRequires: inews
BuildRequires: krb5-devel
BuildRequires: ncurses-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
### RPM bug causes package to conflict with itself
#Conflicts: pine
Obsoletes: pine <= 4.64
Provides: pine = 4.64

Provides: realpine = %{version}-%{release}
Provides: re-alpine = %{version}-%{release}

%description
Alpine (Alternatively Licensed Program for Internet News & Email) is a tool
for reading, sending, and managing electronic messages. Alpine is the
successor to Pine and was developed by Computing & Communications at the
University of Washington.

Though originally designed for inexperienced email users, Alpine supports
many advanced features, and an ever-growing number of configuration and
personal-preference options.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0 -b .orig

#%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure */Makefile */*/Makefile imap/src/osdep/unix/Makefile.gss
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' imap/src/osdep/unix/Makefile.gss

%build
touch imap/ip6
%configure \
    --with-spellcheck-prog="aspell" \
    --with-system-pinerc="%{_sysconfdir}/pine.conf" \
    --with-system-fixed-pinerc="%{_sysconfdir}/pine.conf.fixed"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 alpine/alpine %{buildroot}%{_bindir}/alpine
%{__install} -Dp -m0755 pico/pico %{buildroot}%{_bindir}/pico
%{__install} -Dp -m0755 pico/pilot %{buildroot}%{_bindir}/pilot
%{__install} -Dp -m0755 alpine/rpload %{buildroot}%{_bindir}/rpload
%{__install} -Dp -m0755 alpine/rpdump %{buildroot}%{_bindir}/rpdump
%{__install} -Dp -m0755 imap/mailutil/mailutil %{buildroot}%{_bindir}/mailutil
#if ! install -D -m2755 -gmail imap/mlock/mlock $RPM_BUILD_ROOT%{_sbindir}/mlock; then
%{__install} -Dp -m0755 imap/mlock/mlock %{buildroot}%{_sbindir}/mlock
%{__install} -Dp -m0644 doc/alpine.1 %{buildroot}%{_mandir}/man1/alpine.1
%{__install} -Dp -m0644 doc/pico.1 %{buildroot}%{_mandir}/man1/pico.1
%{__install} -Dp -m0644 doc/pilot.1 %{buildroot}%{_mandir}/man1/pilot.1
%{__install} -Dp -m0644 doc/rpload.1 %{buildroot}%{_mandir}/man1/rpload.1
%{__install} -Dp -m0644 doc/rpdump.1 %{buildroot}%{_mandir}/man1/rpdump.1
%{__install} -Dp -m0644 imap/src/mailutil/mailutil.1 %{buildroot}%{_mandir}/man1/mailutil.1

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pine.conf
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pine.conf.fixed

%{__ln_s} -f alpine %{buildroot}%{_bindir}/pine
%{__ln_s} -f alpine.1.gz %{buildroot}%{_mandir}/man1/pine.1.gz

%pre
### Clean up mess
if [ -r %{_sysconfdir}/alpine.conf -a -r %{_sysconfdir}/pine.conf ]; then
    %{__mv} -f %{_sysconfdir}/pine.conf %{_sysconfdir}/pine.conf.rpmsave
fi

if [ -r %{_sysconfdir}/alpine.conf ]; then
    %{__mv} -f %{_sysconfdir}/alpine.conf %{_sysconfdir}/pine.conf
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE NOTICE README* VERSION doc/*.txt doc/tech-notes/*.html
%doc %{_mandir}/man1/alpine.1*
%doc %{_mandir}/man1/mailutil.1*
%doc %{_mandir}/man1/pico.1*
%doc %{_mandir}/man1/pilot.1*
%doc %{_mandir}/man1/pine.1*
%doc %{_mandir}/man1/rpdump.1*
%doc %{_mandir}/man1/rpload.1*
%config(noreplace) %{_sysconfdir}/pine.conf
%config(noreplace) %{_sysconfdir}/pine.conf.fixed
%{_bindir}/alpine
%{_bindir}/mailutil
%{_bindir}/pico
%{_bindir}/pilot
%{_bindir}/pine
%{_bindir}/rpdump
%{_bindir}/rpload

%defattr(2755, root, mail, 0755)
%{_sbindir}/mlock

%changelog
* Tue Oct 05 2010 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.02 (re-alpine).

* Sat May 23 2009 Dag Wieers <dag@wieers.com> - 2.00-2
- Added searchheader patch.

* Thu Sep 11 2008 Dag Wieers <dag@wieers.com> - 2.00-1
- Updated to release 2.00.

* Thu Sep 11 2008 Dag Wieers <dag@wieers.com> - 1.10-4
- Updated rules patch. (Joe Pruett)

* Wed Jul 30 2008 Dag Wieers <dag@wieers.com> - 1.10-3
- Added rules patch.

* Sun Jul 27 2008 Dag Wieers <dag@wieers.com> - 1.10-2
- Added patch to show both X and bold on selection. (Dag Wieers)
- Added maildir and fillpara patch.
- Restore original pine.conf location.

* Tue Mar 18 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.
- Included original pine.conf, lacking anything better.
- Disable --passfile, use platform-specific password caching.

* Fri Dec 21 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Tue Nov 20 2007 Dag Wieers <dag@wieers.com> - 0.99999-1
- Updated to release 0.99999.

* Sun Oct 28 2007 Dag Wieers <dag@wieers.com> - 0.9999-2
- Enabled passfile support.

* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 0.9999-1
- Updated to release 0.9999.

* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 0.999-2
- Removed Conflicts: pine as RPM bug causes package to conflict with itself. (Bart Schaefer)

* Fri Aug 24 2007 Dag Wieers <dag@wieers.com> - 0.999-1
- Initial package. (using DAR)
