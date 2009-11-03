# $Id$
# Authority: dag
# Upstream: Rodrigo Barbosa <rodrigob$darkover,org>

Summary: E-Mail auto-response software
Name: reply-o-matic
Version: 1.4.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://reply-o-matic.sourceforge.net/

Source: http://dl.sf.net/reply-o-matic/reply-o-matic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: smtpdaemon

%description
Reply-o-Matic is a highly configurable, secure, auto reply software, to be 
used in conjunction with any Mail Transfer Agent or local delivery agent. 
It provides an easy, uniformed way, to provide auto-responses to e-mails.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m4755 rom %{buildroot}%{_sbindir}/rom
%{__install} -Dp -m0644 rom.1 %{buildroot}%{_mandir}/man1/rom.1
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/rom/.rates/
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/rom/.ignores/
touch %{buildroot}%{_sysconfdir}/rom/paranoid

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS HEADERS LICENSE README RELEASE_NOTES
%doc %{_mandir}/man1/rom.1*
%dir %{_sysconfdir}/rom/
%dir %{_sysconfdir}/rom/.ignores/

%defattr(4755, root, root, 0755)
%{_sbindir}/rom

%defattr(0755, root, 1, 0755)
%config(noreplace) %{_sysconfdir}/rom/paranoid

%defattr(1777, root, root, 0755)
%dir %{_sysconfdir}/rom/.rates/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Updated to release 1.4.1.

* Sun Aug 20 2006 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Initial package based on RPM from Rodrigo Barbosa.
