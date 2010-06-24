# $Id$
# Authority: dag
# Upstream: MIMEDefang mailinglist <mimedefang$lists,roaringpenguin,com>

Summary: Email filtering application using sendmail's milter interface
Name: mimedefang
Version: 2.69
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.mimedefang.org/

Source: http://www.mimedefang.org/static/mimedefang-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl-Digest-SHA1
BuildRequires: perl-IO-stringy
BuildRequires: perl-MailTools
#BuildRequires: perl-Mail-SpamAssassin
BuildRequires: perl-MIME-tools
BuildRequires: perl-Unix-Syslog
BuildRequires: sendmail-devel > 8.12.0
Requires: sendmail >= 8.12.0

%description
MIMEDefang is an e-mail filter program which works with Sendmail 8.11
and later.  MIMEDefang filters all e-mail messages sent via SMTP.
MIMEDefang splits multi-part MIME messages into their components and
potentially deletes or modifies the various parts.  It then
reassembles the parts back into an e-mail message and sends it on its
way.

There are some caveats you should be aware of before using MIMEDefang.
MIMEDefang potentially alters e-mail messages.  This breaks a "gentleman's
agreement" that mail transfer agents do not modify message bodies.  This
could cause problems, for example, with encrypted or signed messages.

Deleting attachments could cause a loss of information.  Recipients must
be aware of this possibility, and must be willing to explain to senders
exactly why they cannot mail certain types of files.  You must have the
willingness of your e-mail users to commit to security, or they will
complain loudly about MIMEDefang.

%prep
%setup

%build
%configure \
    --with-milterlib="%{_libdir}" \
    --with-pthread-flag \
    --with-quarantinedir="%{_localstatedir}/spool/MD-Quarantine" \
    --with-spooldir="%{_localstatedir}/spool/MIMEDefang"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/mimedefang/
%{__make} install-redhat RPM_INSTALL_ROOT="%{buildroot}"


%pre
### Old packages may have these...
if [ -d %{_localstatedir}/spool/mimedefang -a ! -d %{_localstatedir}/spool/MIMEDefang ]; then
    %{__mv} -f %{_localstatedir}/spool/mimedefang %{_localstatedir}/spool/MIMEDefang
fi

if [ -d %{_localstatedir}/spool/quarantine -a ! -d %{_localstatedir}/spool/MD-Quarantine ]; then
    %{__mv} -f %{_localstatedir}/spool/quarantine %{_localstatedir}/spool/MD-Quarantine
fi

useradd -M -r -d %{_localstatedir}/spool/MIMEDefang -s /bin/false -c "MIMEDefang User" defang &>/dev/null || :

%post
#%{__cat} << EOF
#
#In order to complete the installation of mimedefang, you will need to add the
#following line to your sendmail mc file:
#
#   INPUT_MAIL_FILTER(\`mimedefang', \`S=unix:/var/spool/MIMEDefang/mimedefang.sock, F=T, T=S:1m;R:1m;E:5m')
#
#Use the sendmail-cf package to rebuild your /etc/mail/sendmail.cf file and
#restart your sendmail daemon.
#
#EOF
/sbin/chkconfig --add mimedefang

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service mimedefang stop &>/dev/null || :
    /sbin/chkconfig --del mimedefang
fi

%postun
if [ $1 -ne 0 ]; then
    /sbin/service mimedefang condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog contrib/ COPYING examples/ README* SpamAssassin/
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/mail/
%config(noreplace) %{_sysconfdir}/mail/mimedefang-filter
%config(noreplace) %{_sysconfdir}/mail/sa-mimedefang.cf*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config %{_initrddir}/*
%{_bindir}/*

%defattr(-, defang, defang, 0755)
%dir %{_localstatedir}/log/mimedefang/

%defattr(-, defang, defang, 0700)
%dir %{_localstatedir}/spool/MIMEDefang
%dir %{_localstatedir}/spool/MD-Quarantine

%changelog
* Fri Jun 18 2010 Dag Wieers <dag@wieers.com> - 2.69-1
- Updated to release 2.69.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 2.68-1
- Updated to release 2.68.

* Sun Feb 01 2009 Dag Wieers <dag@wieers.com> - 2.67-1
- Updated to release 2.67.

* Thu Sep 04 2008 Dag Wieers <dag@wieers.com> - 2.65-1
- Updated to release 2.65.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 2.64-1
- Updated to release 2.64.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 2.63-1
- Updated to release 2.63.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 2.62-1
- Updated to release 2.62.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 2.61-1
- Updated to release 2.61.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 2.57-1
- Updated to release 2.57.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 2.56-1
- Updated to release 2.56.

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 2.54-1
- Added --with-pthread-flag configure option. (Nathan Hruby)
- Updated to release 2.54.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 2.53-1
- Updated to release 2.53.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 2.52-1
- Fix for x86_64. (Chris Ausbrooks)
- Added perl-Unix-Syslog as a buildrequirement. (Josh Kelley)
- Updated to release 2.52.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.45-1
- Updated to release 2.45.

* Fri Jul 16 2004 Dag Wieers <dag@wieers.com> - 2.44-1
- Updated to release 2.44.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 2.43-1
- Updated to release 2.43.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 2.42-1
- Updated to release 2.42.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.40-1
- Updated to release 2.40.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 2.38-0
- Updated to release 2.38.

* Fri Sep 05 2003 Dag Wieers <dag@wieers.com> - 2.37-0
- Updated to release 2.37.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 2.35-3
- Require perl-IO-Stringy.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 2.35-2
- Changed user mimedefang to defang.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 2.35-0
- Initial package. (using DAR)
