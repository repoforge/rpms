# $Id$
# Authority: dag

Summary: POP3 mail retriever with reliable Maildir delivery
Name: getmail
Version: 3.2.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://pyropus.ca/software/getmail/

Source: http://pyropus.ca/software/getmail/old-versions/getmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3.3
Requires: python >= 2.3.3
BuildArch: noarch

%description
getmail is intended as a simple replacement for fetchmail for those people
who do not need its various and sundry configuration options, complexities,
and bugs.  It retrieves mail from one or more POP3 servers for one or more
email accounts, and reliably delivers into a Maildir specified on a
per-account basis.  It can also deliver into mbox files, although this
should not be attempted over NFS.  getmail is written entirely in python.


%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 getmail %{buildroot}%{_bindir}/getmail
%{__install} -Dp -m0755 getmail_maildir %{buildroot}%{_bindir}/getmail_maildir
%{__install} -Dp -m0755 getmail_mbox %{buildroot}%{_bindir}/getmail_mbox

%{__install} -Dp -m0755 getmail.1 %{buildroot}%{_mandir}/man1/getmail.1

%{__install} -d -m0755 %{buildroot}%{_prefix}/lib/getmail/
%{__install} -Dp -m0644 *.py %{buildroot}%{_prefix}/lib/getmail/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING THANKS TODO *.html *.txt getmailrc-example
%doc %{_mandir}/man1/getmail.1*
%{_bindir}/getmail
%{_bindir}/getmail_maildir
%{_bindir}/getmail_mbox
%{_prefix}/lib/getmail/

%changelog
* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 3.2.5-1
- Initial package. (using DAR)
