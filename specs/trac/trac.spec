# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: <trac@lists.edgewall.com>

Name: trac
Summary: Integrated SCM and project management tool
Version: 0.7
Release: 1
License: GPL
Group: Development/Tools
URL: http://projects.edgewall.com/trac/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.edgewall.com/pub/trac/trac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.1
Requires: python >= 2.1, subversion-python >= 1.0.0, python-sqlite >= 0.4.3
Requires: python-clearsilver >= 0.9.3, webserver

%description
Trac is a minimalistic web-based software project management and
bug/issue tracking system. It provides an interface to revision
control systems (Subversion), an integrated Wiki and convenient
report facilities.

Trac allows wiki markup in issue descriptions and commit messages,
to create links and seamless references between bugs, tasks,
changesets, files and wiki pages. A timeline shows all project
events in order, making getting an overview of the project and
tracking progress very easy. 

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/lib/|%{_libdir}|g' setup.py

%{__cat} <<EOF >trac.httpd
Alias /trac/ "%{_datadir}/trac/htdocs/"

### Trac need to know where the database is located
<Location "/cgi-bin/trac.cgi">
	SetEnv TRAC_DB "%{_datadir}/trac/myproject.db"
</Location>

### You need this to allow users to authenticate
<Location "/cgi-bin/trac.cgi/login">
	AuthType Basic
	AuthName "trac"
	AuthUserFile %{_datadir}/trac/trac.htpasswd
	Require valid-user
</location>
EOF

%build

%install
%{__rm} -rf %{buildroot}
python ./setup.py install \
	--prefix="%{buildroot}%{_prefix}"

%{__install} -D -m0644 trac.httpd %buildroot}%{_sysconfdir}/httpd/conf.d/trac.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README THANKS UPGRADE
%{_bindir}/*
%{_datadir}/trac/
%{_libdir}/python*/site-packages/trac/

%changelog
* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Initial package. (using DAR)
