# $Id$
# Authority: dag

Summary: Spam filter for Usenet news servers
Name: cleanfeed
Version: 0.95.7b
Release: 21.1.1%{?dist}
License: distributable
Group: System Environment/Daemons

Source: ftp://ftp.exit109.com/users/jeremy/cleanfeed-%{version}.tar.gz
Patch0: cleanfeed-0.95.7b-redhat.patch
Patch1: cleanfeed-0.95.7b-ro.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
Cleanfeed is an automatic spam filter for Usenet news servers and
routers (INN, Cyclone, Typhoon, Breeze and NNTPRelay).  Cleanfeed
looks for duplicated messages, repeated patterns, and known spamming
sites and domains.  It can be configured to block binary posts to
non-binary newsgroups, to cancel already-rejected articles, and to
reject some spamming from local users.

Install the cleanfeed package if you need a spam filter for a Usenet
news server.

%prep
%setup
%patch0 -p1 -b .rh
%patch1 -p1

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 cleanfeed.conf %{buildroot}%{_sysconfdir}/news/cleanfeed.conf
%{__install} -Dp -m0644 cleanfeed.8 %{buildroot}%{_mandir}/man8/cleanfeed.8
%{__install} -Dp -m0750 cleanfeed %{buildroot}%{_libdir}/news/bin/filter/filter_innd.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_mandir}/man8/cleanfeed.8*

%defattr(-, news, news, 0755)
%config(noreplace) %{_sysconfdir}/news/cleanfeed.conf
%dir %{_libdir}/news/
%dir %{_libdir}/news/bin/
%dir %{_libdir}/news/bin/filter/
%{_libdir}/news/bin/filter/filter_innd.pl

%changelog
* Sun May 13 2007 Dag Wieers <dag@wieers.com> - 0.95.7b-21.1.1
- Initial package. (based on Red Hat RPM package)
