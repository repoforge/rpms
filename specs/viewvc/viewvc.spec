# $Id$
# Authority: dag

%define _default_patch_fuzz 2

Summary: Web-interface for CVS and Subversion version control repositories
Name: viewvc
Version: 1.1.12
Release: 1%{?dist}
License: BSD
Group: Development/Tools
URL: http://www.viewvc.org/

Source: http://www.viewvc.org/viewvc-%{version}.tar.gz
Patch0: viewvc-tools.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 1.5.2
Requires: httpd
Requires: python >= 1.5.2
Obsoletes: viewcvs
Provides: viewcvs = %{version}-%{release}

%description
ViewVC is a browser interface for CVS and Subversion version control 
repositories. It generates templatized HTML to present navigable 
directory, revision, and change log listings. It can display specific 
versions of files as well as diffs between those versions. Basically, 
ViewVC provides the bulk of the report-like functionality you expect out 
of your version control tool, but much more prettily than the average 
textual command-line program output.

%prep
%setup
%patch0 -p1
find . -type d -name .svn | xargs %{__rm} -rf

%{__cat} <<EOF >viewvc.httpd
### viewvc sample configuration

#ScriptAlias /viewvc %{_localstatedir}/www/cgi-bin/viewvc.cgi
#ScriptAlias /query %{_localstatedir}/www/cgi-bin/query.cgi
#Alias /viewvc-static %{_localstatedir}/www/viewvc
#
#<Directory %{_localstatedir}/www/viewvc>
#	Allow from all
#</Directory>
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__python} viewvc-install --destdir="%{buildroot}" --prefix="%{_datadir}/viewvc"

### Remove mod_python files
%{__rm} -rf %{buildroot}%{_datadir}/viewvc/bin/mod_python

### Fix python files perms and shellbang
%{__perl} -pi \
    -e 's|/usr/local/bin/python|%{_bindir}/python|g;' \
    -e 's|\s*/usr/bin/env python|%{_bindir}/python|g;' \
    -e 's|CONF_PATHNAME =.*|CONF_PATHNAME = r"%{_sysconfdir}/viewvc/viewvc.conf"|g;' \
    $(find %{buildroot}%{_datadir}/viewvc/ -type f)

### Install CGI's to www directory
%{__mkdir_p} %{buildroot}%{_localstatedir}/www/cgi-bin
%{__install} -p -m0755 %{buildroot}%{_datadir}/viewvc/bin/cgi/*.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/
%{__rm} -rf %{buildroot}%{_datadir}/viewvc/bin/cgi

### Fix paths in configuration
%{__perl} -pi \
    -e 's|^#docroot = .*|docroot = /viewvc-static|;' \
    -e 's|^#cvsgraph_conf = .*|cvsgraph_conf = %{_sysconfdir}/viewvc/cvsgraph.conf|;' \
    -e 's|^#template_dir = .*|template_dir = %{_datadir}/viewvc/templates|;' \
    %{buildroot}%{_datadir}/viewvc/viewvc.conf

### Install config to sysconf directory
%{__install} -Dp -m0644 %{buildroot}%{_datadir}/viewvc/viewvc.conf %{buildroot}%{_sysconfdir}/viewvc/viewvc.conf
%{__rm} -f %{buildroot}%{_datadir}/viewvc/viewvc.conf
%{__install} -Dp -m0644 %{buildroot}%{_datadir}/viewvc/cvsgraph.conf %{buildroot}%{_sysconfdir}/viewvc/cvsgraph.conf
%{__rm} -f %{buildroot}%{_datadir}/viewvc/cvsgraph.conf

### Move static files under %{_localstatedir}/www
%{__mv} %{buildroot}%{_datadir}/viewvc/templates/docroot %{buildroot}%{_localstatedir}/www/viewvc

### Compile the python files
find %{buildroot}%{_datadir}/viewvc/lib -type f -name "*.pyc" | xargs %{__rm} -f
%{__python} -O %{_libdir}/python*/compileall.py %{buildroot}%{_datadir}/viewvc/lib

### Install viewcv Apache configuration
%{__install} -Dp -m0644 viewvc.httpd %{buildroot}/etc/httpd/conf.d/viewvc.conf

### Set mode 755 on executable scripts
%{__grep} -rl '^#!' %{buildroot}%{_datadir}/viewvc | xargs %{__chmod} 0755

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README INSTALL
%config(noreplace) %{_sysconfdir}/viewvc/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/viewvc.conf
%{_datadir}/viewvc/
%dir %{_localstatedir}/www/cgi-bin/
%{_localstatedir}/www/cgi-bin/viewvc.cgi
%{_localstatedir}/www/cgi-bin/query.cgi
%{_localstatedir}/www/viewvc/

%changelog
* Fri Nov 04 2011 Dag Wieers <dag@wieers.com> - 1.1.12-1
- Updated to release 1.1.12.

* Tue May 17 2011 Dag Wieers <dag@wieers.com> - 1.1.11-1
- Updated to release 1.1.11.

* Wed Mar 16 2011 Dag Wieers <dag@wieers.com> - 1.1.10-1
- Updated to release 1.1.10.

* Sat Feb 19 2011 Dag Wieers <dag@wieers.com> - 1.1.9-1
- Updated to release 1.1.9.

* Fri Dec  3 2010 Christoph Maser <cmaser@gmx.de> - 1.1.8-1
- Updated to version 1.1.8.

* Fri Sep 10 2010 Dag Wieers <dag@wieers.com> - 1.1.7-1
- Updated to release 1.1.7.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.

* Wed Mar 31 2010 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 1.1.2-2
- Fix configuration fixes.

* Wed Aug 12 2009 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Sat Jun 06 2009 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Mon May 18 2009 Christoph Maser <cmr@financial.com> - 1.1.0-1
- Updated to release 1.1.0.

* Wed May 06 2009 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Sat Oct 14 2006 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Tue Oct 10 2006 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Fixed group name.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Aug 01 2006 Dag Wieers <dag@wieers.com> - 1.0.1-2
- Provide a better default httpd setup using Alias and ScriptALias /viewvc-static.

* Tue Aug 01 2006 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package based on Mandrake package.
