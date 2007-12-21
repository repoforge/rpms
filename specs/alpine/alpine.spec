# $Id$
# Authority: dag

Summary: Alternative Pine mail user agent implementation
Name: alpine
Version: 1.00
Release: 1
License: Apache License
Group: Applications/Internet
URL: http://www.washington.edu/alpine/

Source: ftp://ftp.cac.washington.edu/alpine/alpine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: inews, aspell, openldap-devel, openssl-devel, krb5-devel
### RPM bug causes package to conflict with itself
#Conflicts: pine
Obsoletes: pine <= 4.64
Provides: pine = 4.64

%description
Alpine (Alternatively Licensed Program for Internet News & Email) is a tool
for reading, sending, and managing electronic messages. Alpine is the
successor to Pine and was developed by Computing & Communications at the
University of Washington.  

Though originally designed for inexperienced email users, Alpine supports
many advanced features, and an ever-growing number of configuration and
personal-preference options.

%prep
%setup

%build
touch imap/ip6
%configure \
    --with-passfile=".pinepwd" \
    --with-spellcheck-prog="aspell"
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

%{__ln_s} -f alpine %{buildroot}%{_bindir}/pine
%{__ln_s} -f alpine.1.gz %{buildroot}%{_mandir}/man1/pine.1.gz

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE NOTICE README VERSION doc/*.txt
%doc %{_mandir}/man1/alpine.1*
%doc %{_mandir}/man1/mailutil.1*
%doc %{_mandir}/man1/pico.1*
%doc %{_mandir}/man1/pilot.1*
%doc %{_mandir}/man1/pine.1*
%doc %{_mandir}/man1/rpdump.1*
%doc %{_mandir}/man1/rpload.1*
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
