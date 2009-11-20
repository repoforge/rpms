# $Id$
# Authority: shuff
# Upstream: Re-Alpine Development List <re-alpine-devel$lists,sourceforge,net>

# Test

Summary: The continuation of the Alpine email client from University of Washington
Name: re-alpine
Version: 2.01
Release: 1%{?dist}
License: Apache License
Group: Applications/Internet
URL: http://re-alpine.sourceforge.net/

Source0: http://downloads.sourceforge.net/project/re-alpine/re-alpine-%{version}.tar.bz2
Source1: pine.conf
Source2: pine.conf.fixed
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: inews, aspell, openldap-devel, openssl-devel, krb5-devel, pam-devel, ncurses-devel, tcl-devel
### RPM bug causes package to conflict with itself
#Conflicts: pine
Obsoletes: pine <= 4.64
Provides: pine = 4.64
Obsoletes: alpine <= 2.00
Provides: alpine = 2.00

%description
Alpine (Alternatively Licensed Program for Internet News & Email) is a tool
for reading, sending, and managing electronic messages. Alpine is the
successor to Pine and was developed by Computing & Communications at the
University of Washington.

Though originally designed for inexperienced email users, Alpine supports
many advanced features, and an ever-growing number of configuration and
personal-preference options.

Re-Alpine is a maintenance fork of the Alpine project.

%prep
%setup

#%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure */Makefile */*/Makefile imap/src/osdep/unix/Makefile.gss
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' imap/src/osdep/unix/Makefile.gss

%build
touch imap/ip6
%configure \
    --disable-dependency-tracking \
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
* Fri Nov 20 2009 Steve Huff <shuff@vecna.org> - 2.01-1
- Initial package.
