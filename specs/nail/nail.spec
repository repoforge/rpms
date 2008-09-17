# $Id$
# Authority: dag

#define _without_nss 1

%define real_name mailx

Summary: Enhanced implementation of the mailx command
Name: nail
Version: 12.3
Release: 4
Group: Applications/Internet
License: BSD
URL: http://nail.sourceforge.net/

Source: http://dl.sf.net/heirloom/mailx-%{version}.tar.bz2
Patch0: nail-11.25-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_nss:BuildRequires: nss-devel, pkgconfig}
%{!?_without_nss:BuildRequires: openssl-devel}

%description
Nail is an enhanced mail command, which provides the functionality
of the POSIX mailx command. It is derived from Berkeley Mail.

Additionally to the POSIX features, nail can work with Maildir/ e-mail
storage format (as well as mailboxes), supports IMAP, POP3 and SMTP
procotols (including over SSL) to operate with remote hosts, handles mime
types and different charsets. There are a lot of other useful features,
see %{name}.html in the documentation.

And as its ancient analogues, nail can be used as a mail script language,
both for sending and receiving mail.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

### Rename mailx to nail to avoid conflict with upstream mailx
%{__perl} -pi.orig -e 's|mailx|nail|g; s|Mailx|Nail|g; s|MAILX |NAIL |g' nail.rc nail.1 nail.1.html
%{__mv} -f mailx.1.html nail.html

%build
%{!?_without_nss:export INCLUDES="$INCLUDES $(pkg-config --cflags-only-I nss)"}
%{expand: %%define optflags %{optflags} -D_GNU_SOURCE}
%{__make} CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" \
    SYSCONFDIR="%{_sysconfdir}" \
    MAILRC="%{_sysconfdir}/nail.rc" \
    MAILSPOOL="%{_localstatedir}/mail" \
    SENDMAIL="%{_sbindir}/sendmail" \
    UCBINSTALL="install"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    PREFIX="%{_prefix}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" \
    SYSCONFDIR="%{_sysconfdir}" \
    MAILRC="%{_sysconfdir}/nail.rc" \
    MAILSPOOL="%{_localstatedir}/mail" \
    SENDMAIL="%{_sbindir}/sendmail" \
    UCBINSTALL="install"

### Rename mailx to nail to avoid conflict with upstream mailx
%{__mv} -f %{buildroot}%{_bindir}/mailx %{buildroot}%{_bindir}/nail
%{__mv} -f %{buildroot}%{_mandir}/man1/mailx.1 %{buildroot}%{_mandir}/man1/nail.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README nail.html
%doc %{_mandir}/man1/nail.1*
%config(noreplace) %{_sysconfdir}/nail.rc
%{_bindir}/nail

%changelog
* Thu Sep 11 2008 Dag Wieers <dag@wieers.com> - 12.3-1
- Initial package based on Fedora.
