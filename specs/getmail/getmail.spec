# $Id$
# Authority: dag

%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: POP3 mail retriever with reliable Maildir delivery
Name: getmail
Version: 4.20.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://pyropus.ca/software/getmail/

Source: http://pyropus.ca/software/getmail/old-versions/getmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3.3
Requires: python >= 2.3.3

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
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/*
%doc %{_mandir}/man1/getmail.1*
%doc %{_mandir}/man1/getmail_fetch.1*
%doc %{_mandir}/man1/getmail_maildir.1*
%doc %{_mandir}/man1/getmail_mbox.1*
%{_bindir}/getmail
%{_bindir}/getmail_fetch
%{_bindir}/getmail_maildir
%{_bindir}/getmail_mbox
%{python_sitelib}/getmailcore/
%{!?_without_egg_info:%{python_sitelib}/getmail-%{version}*.egg-info}

%changelog
* Sun Aug 14 2011 Yury V. Zaytsev <yury@shurup.com> - 4.20.4-1
- Added *.egg-info for compatibility with RHEL6+.
- Updated to release 4.20.4 (Julian Yap).

* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 4.10.0-1
- Updated to release 4.10.0.

* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 4.9.0-1
- Updated to release 4.9.0.

* Sun Sep 28 2008 Dag Wieers <dag@wieers.com> - 4.8.4-1
- Updated to release 4.8.4.

* Wed Aug 13 2008 Dries Verachtert <dries@ulyssis.org> - 4.8.3-1
- Updated to release 4.8.3.

* Thu Mar 27 2008 Dries Verachtert <dries@ulyssis.org> - 4.8.1-1
- Updated to release 4.8.1.

* Sat Feb 23 2008 Dries Verachtert <dries@ulyssis.org> - 4.8.0-1
- Updated to release 4.8.0.

* Wed Nov 14 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.7-1
- Updated to release 4.7.7.

* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.6-1
- Updated to release 4.7.6.

* Thu Jun 07 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.5-1
- Updated to release 4.7.5.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.4-1
- Updated to release 4.7.4.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.3-1
- Updated to release 4.7.3.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 4.7.2-1
- Initial package. (using DAR)
