# $Id$
# Authority: dag

Summary: Tool to migrate across IMAP servers
Name: imapsync
Version: 1.241
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.linux-france.org/prj/imapsync/

Source: http://www.linux-france.org/prj/imapsync/dist/imapsync-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Mail::IMAPClient)
#Requires: perl(IO::Socket::SSL)
#Requires: perl(Digest::HMAC)
#Requires: perl(Digest::MD5::M4p)
#Requires: perl(Mail::IMAPClient)
#Requires: perl(Net::SSLeay)

%define __perl_requires %{_builddir}/%{buildsubdir}/imapsync-filter-requires.sh

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox
migration, and reduces the amount of data transferred by only copying
messages that are not present on both servers. Read, unread, and
deleted flags are preserved, and the process can be stopped and
resumed. The original messages can optionally be deleted after a
successful transfer.

%prep
%setup

%{__cat} <<'EOF' >imapsync-filter-requires.sh
#!/bin/sh
/usr/lib/rpm/perl.req $* | sed -e '/perl(--prefix2)/d'
EOF
%{__chmod} a+x imapsync-filter-requires.sh

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS FAQ GPL INSTALL README TODO
%doc %{_mandir}/man1/imapsync.1*
%{_bindir}/imapsync

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 1.241-1
- Updated to release 1.241.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 1.233-1
- Updated to release 1.233.

* Thu Sep 13 2007 Dag Wieers <dag@wieers.com> - 1.223-1
- Updated to release 1.223.

* Thu Aug 16 2007 Fabian Arrotin <fabian.arrotin@arrfab.net> - 1.219-1
- Update to 1.219.
- Cosmetic changes for Requires: specific to RHEL/CentOS.

* Mon Mar 19 2007 Neil Brown <neilb@inf.ed.ac.uk>
- Packaged up source tarball into the RPM. Had to add a fix
  to stop the perl_requires script wrongly matching on "use --prefix"
  in the docs as a genuine perl "use module;"
