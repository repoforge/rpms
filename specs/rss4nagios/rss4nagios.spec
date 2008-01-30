# $Id$
# Authority: dag

Summary: Authenticated RSS alerts for nagios
Name: rss4nagios
Version: 1.1
Release: 1
License: GPL
Group: Applications/System
URL: http://altinity.blogs.com/dotorg/2006/07/lessons_in_rss.html

Source: http://altinity.blogs.com/dotorg/rss4nagios-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
Requires: nagios >= 2.1
Requires: perl(XML::RSS)

%description
Authenticated RSS alerts for nagios as an alternate contact method.

%prep
%setup

%{__perl} -pi.orig -e '
        s|/usr/local/nagios/rss|%{_localstatedir}/log/nagios/rss|g;
        s|- etc/rss.cfg|- %{_sysconfdir}/nagios/rss.cfg|g;
        s|- bin/rss-multiuser|- %{_libdir}/nagios/plugins/rss-multiuser|g;
        s|- sbin/rss.cgi|- %{_libdir}/nagios/cgi/rss.cgi|g;
        s|/usr/local/nagios/bin|%{_libdir}/nagios/plugins|g;
    ' README

%{__perl} -pi.orig -e 's|/usr/local/nagios/rss|%{_localstatedir}/log/nagios/rss|g;' rss.cfg.in
%{__perl} -pi.orig -e 's|/usr/local/nagios/etc/rss.cfg|%{_sysconfdir}/nagios/rss.cfg|g;' rss.cgi rss-multiuser

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 rss.cfg.in %{buildroot}%{_sysconfdir}/nagios/rss.cfg
%{__install} -Dp -m0755 rss-multiuser %{buildroot}%{_libdir}/nagios/plugins/rss-multiuser
%{__install} -Dp -m0755 rss.cgi %{buildroot}%{_libdir}/nagios/cgi/rss.cgi

%{__install} -dp -m0755 %{buildroot}%{_localstatedir}/log/nagios/rss/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/cgi/
%{_libdir}/nagios/cgi/rss.cgi
%dir %{_libdir}/nagios/plugins/
%{_libdir}/nagios/plugins/rss-multiuser

%defattr(-, nagios, nagios, 0755)
%dir %{_sysconfdir}/nagios/
%config(noreplace) %{_sysconfdir}/nagios/rss.cfg

%defattr(-, nagios, apache, 2755)
%dir %{_localstatedir}/log/
%dir %{_localstatedir}/log/nagios/
%{_localstatedir}/log/nagios/rss/

%changelog
* Fri Jul 7 2006 Jim Perrin <jperrin@centos.org> - 1.0-1
- Initial packaging
