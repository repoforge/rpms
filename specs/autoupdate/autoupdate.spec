# $Id$
# Authority: dag
# Upstream: Gerald Teschl <Gerald,Teschl$univie,ac,at>

Summary: AutoUpdate, a simple perl script to keep your system up2date
Name: autoupdate
Version: 5.3.12
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.mat.univie.ac.at/~gerald/ftp/autoupdate/

Source: ftp://ftp.mat.univie.ac.at/pub/teschl/autoupdate/autoupdate-%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl >= 0:5.00503, rpm, sh-utils, perl(Net::FTP), perl(DB_File)

Obsoletes: autoupdate-cfg-autoupdate, autoupdate-cfg-caldera, autoupdate-cfg-mandrake
Obsoletes: autoupdate-cfg-powertools, autoupdate-cfg-redhat, autoupdate-cfg-suse
Obsoletes: autoupdate-cfg-yellowdog

%description
AutoUpdate is a simple Perl script which performs a task similar to RedHat's
up2date or autorpm. It can be used to automatically download and upgrade rpms
from different ftp sites. Moreover, it can also be used to keep a server with
a customized (RedHat) distribution plus all clients up to date.

%prep
%setup

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 autoupdate %{buildroot}%{_sbindir}/autoupdate
%{__install} -Dp -m0644 autoupdate.8.gz %{buildroot}%{_mandir}/man8/autoupdate.8.gz
#%{__install} -Dp -m0644 autoupdate.pm.3.gz %{buildroot}%{_mandir}/man3/autoupdate.pm.3.gz

%{__install} -d -m0755 %{buildroot}%{_libdir}/perl5/site_perl/autoupdate/
%{__install} -p -m0644 autoupdate.pm/* %{buildroot}%{_libdir}/perl5/site_perl/autoupdate/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/autoupdate.d
%{__install} -p -m0755 autoupdate.d/*.sh %{buildroot}/%{_sysconfdir}/autoupdate.d/
%{__install} -p -m0644 autoupdate.d/*.{dld,get,conf} %{buildroot}/%{_sysconfdir}/autoupdate.d/
%{__rm} -f %{buildroot}/etc/autoupdate.d/{powertools,rhsa,rpmfind,texmacs,webmin}.dld

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/{log,spool/autoupdate}
touch %{buildroot}%{_localstatedir}/log/autoupdate.log

#%{__install} -Dp -m0644 autoupdate.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/autoupdate
for file in auto{upd,ins,dld,get,mrg,prg}; do
	%{__ln_s} -f autoupdate %{buildroot}%{_sbindir}/$file
	%{__ln_s} -f autoupdate.8.gz %{buildroot}%{_mandir}/man8/$file.8.gz
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE config.html faq.html general.html install.html
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/autoupdate.d/
%{_localstatedir}/spool/autoupdate/
#%config /etc/logrotate.d/autoupdate
%ghost %{_localstatedir}/log/autoupdate.log
%{_sbindir}/*
%{_libdir}/perl5/site_perl/autoupdate/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.3.12-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 5.3.12-1
- Updated to release 5.3.12.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 5.3.5-1
- Updated to release 5.3.5.

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 5.3-0
- Updated to release 5.3.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 5.2.4-0
- Updated to release 5.2.4.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 5.1.2-0
- Updated to release 5.1.2.

* Thu Jul 10 2003 Dag Wieers <dag@wieers.com> - 5.1.1-0
- Updated to release 5.1.1.

* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 5.0.2-0
- Updated to release 5.0.2.

* Thu May 29 2003 Dag Wieers <dag@wieers.com> - 5.0.1-0
- Updated to release 5.0.1.

* Wed May 21 2003 Dag Wieers <dag@wieers.com> - 4.9.8-0
- Updated to release 4.9.8.

* Thu May 15 2003 Dag Wieers <dag@wieers.com> - 4.9.7-0
- Updated to release 4.9.7.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 4.9.5-0
- Updated to release 4.9.5.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 4.9.2-0
- Updated to release 4.9.2.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 4.9-0
- Updated to release 4.9.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 4.8.4-0
- Updated to release 4.8.4.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 4.8.3-0
- Updated to release 4.8.3.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 4.8.2-0
- Updated to release 4.8.2.

* Thu Mar 27 2003 Dag Wieers <dag@wieers.com> - 4.8.1-0
- Updated to release 4.8.1.

* Mon Mar 24 2003 Dag Wieers <dag@wieers.com> - 4.8-0
- Updated to release 4.8.

* Wed Mar 19 2003 Dag Wieers <dag@wieers.com> - 4.7.2-1
- Fixed permissions of distversion.sh. (Bert de Bruijn)

* Wed Mar 19 2003 Dag Wieers <dag@wieers.com> - 4.7.2-0
- Initial package. (using DAR)
