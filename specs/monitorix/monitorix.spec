# $Id$
# Authority: fabian
# Upstream: Jordi Sanfeliu <admin@fibranet.cat>


Summary: Monitorix system monitoring tool
Name: monitorix
Version: 1.2.4
Release: 1%{?dist}
License: GPL
Group: Applications/System 
URL: http://www.monitorix.org

Source: http://www.monitorix.org/%{name}-%{version}.tar.gz
Requires: bash, rrdtool, perl, httpd
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Monitorix is a free, open source, lightweight system monitoring tool.

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
install -m 0755 ports/Linux-RHFC/monitorix.init %{buildroot}%{_initrddir}/monitorix
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0644 monitorix-apache.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/monitorix.conf
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 monitorix.conf %{buildroot}%{_sysconfdir}/monitorix.conf
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 monitorix.pl %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/www/html/monitorix
install -m 0644 logo_top.jpg %{buildroot}%{_localstatedir}/www/html/monitorix
install -m 0644 logo_bot_black.png %{buildroot}%{_localstatedir}/www/html/monitorix
install -m 0644 logo_bot_white.png %{buildroot}%{_localstatedir}/www/html/monitorix
install -m 0644 envelope.png %{buildroot}%{_localstatedir}/www/html/monitorix
install -m 0644 monitorixico.png %{buildroot}%{_localstatedir}/www/html/monitorix
mkdir -p %{buildroot}%{_localstatedir}/www/html/monitorix/imgs
mkdir -p %{buildroot}%{_localstatedir}/www/cgi-bin
install -m 0755 monitorix.cgi %{buildroot}%{_localstatedir}/www/cgi-bin
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca/imgs_email
install -m 0644 reports/ca/traffic_report.html %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca
install -m 0755 reports/ca/traffic_report.sh %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca
install -m 0644 reports/ca/imgs_email/blank.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca/imgs_email
install -m 0644 reports/ca/imgs_email/logo.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca/imgs_email
install -m 0644 reports/ca/imgs_email/signature.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca/imgs_email
install -m 0644 reports/ca/imgs_email/title.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/ca/imgs_email
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/reports/en/imgs_email
install -m 0644 reports/en/traffic_report.html %{buildroot}%{_localstatedir}/lib/monitorix/reports/en
install -m 0755 reports/en/traffic_report.sh %{buildroot}%{_localstatedir}/lib/monitorix/reports/en
install -m 0644 reports/en/imgs_email/blank.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/en/imgs_email
install -m 0644 reports/en/imgs_email/logo.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/en/imgs_email
install -m 0644 reports/en/imgs_email/signature.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/en/imgs_email
install -m 0644 reports/en/imgs_email/title.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/en/imgs_email
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/reports/de/imgs_email
install -m 0644 reports/de/traffic_report.html %{buildroot}%{_localstatedir}/lib/monitorix/reports/de
install -m 0755 reports/de/traffic_report.sh %{buildroot}%{_localstatedir}/lib/monitorix/reports/de
install -m 0644 reports/de/imgs_email/blank.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/de/imgs_email
install -m 0644 reports/de/imgs_email/logo.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/de/imgs_email
install -m 0644 reports/de/imgs_email/signature.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/de/imgs_email
install -m 0644 reports/de/imgs_email/title.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/de/imgs_email
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/reports/it/imgs_email
install -m 0644 reports/it/traffic_report.html %{buildroot}%{_localstatedir}/lib/monitorix/reports/it
install -m 0755 reports/it/traffic_report.sh %{buildroot}%{_localstatedir}/lib/monitorix/reports/it
install -m 0644 reports/it/imgs_email/blank.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/it/imgs_email
install -m 0644 reports/it/imgs_email/logo.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/it/imgs_email
install -m 0644 reports/it/imgs_email/signature.png %{buildroot}%{_localstatedir}/lib/monitorix/reports/it/imgs_email
install -m 0644 reports/it/imgs_email/title.jpg %{buildroot}%{_localstatedir}/lib/monitorix/reports/it/imgs_email
mkdir -p %{buildroot}%{_localstatedir}/lib/monitorix/usage

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add monitorix
#mkdir -p %{_localstatedir}/www/html/monitorix/imgs
#mkdir -p %{_localstatedir}/lib/monitorix/usage
#chown apache:apache %{_localstatedir}/www/html/monitorix/imgs

%files
%defattr(-, root, root)
%{_initrddir}/monitorix
%{_sysconfdir}/httpd/conf.d/monitorix.conf
%config(noreplace) %{_sysconfdir}/monitorix.conf
%{_sbindir}/monitorix.pl
%{_localstatedir}/lib/monitorix/usage
%defattr(-, apache, apache)
%{_localstatedir}/www/html/monitorix/logo_top.jpg
%{_localstatedir}/www/html/monitorix/logo_bot_black.png
%{_localstatedir}/www/html/monitorix/logo_bot_white.png
%{_localstatedir}/www/html/monitorix/envelope.png
%{_localstatedir}/www/html/monitorix/monitorixico.png
%{_localstatedir}/www/html/monitorix/imgs
%{_localstatedir}/www/cgi-bin/monitorix.cgi
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/traffic_report.html
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/traffic_report.sh
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/imgs_email/blank.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/imgs_email/logo.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/imgs_email/signature.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/ca/imgs_email/title.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/traffic_report.html
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/traffic_report.sh
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/imgs_email/blank.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/imgs_email/logo.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/imgs_email/signature.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/en/imgs_email/title.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/traffic_report.html
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/traffic_report.sh
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/imgs_email/blank.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/imgs_email/logo.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/imgs_email/signature.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/de/imgs_email/title.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/traffic_report.html
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/traffic_report.sh
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/imgs_email/blank.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/imgs_email/logo.jpg
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/imgs_email/signature.png
%config(noreplace) %{_localstatedir}/lib/monitorix/reports/it/imgs_email/title.jpg
%defattr(-, root, root)
%doc COPYING Changes Configuration.help README README.Debian README.Slackware TODO

%changelog
* Mon Apr 06 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> 1.2.4-1
- Updated to 1.2.4
* Mon Mar 30 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> 1.2.3-1
- Cosmetic changes for RPMforge inclusion

* Thu Sep 01 2005 Jordi Sanfeliu <admin@fibranet.cat>
- Release 0.7.8.
- First public release.
- All changes are described in the Changes file.
