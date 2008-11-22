# $Id$
# Authority: dag
# Upstream: <trac$lists,edgewall,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Trac

Name: trac
Summary: Integrated SCM and project management tool
Version: 0.11.2.1
Release: 1
License: GPL
Group: Development/Tools
URL: http://projects.edgewall.com/trac/

Source: http://ftp.edgewall.com/pub/trac/Trac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.3, python-setuptools => 0.6
Requires: python >= 2.3, python-sqlite >= 1.0, subversion >= 1.0.0
Requires: python-genshi >= 0.5, python-setuptools >= 0.6, webserver
#Requires: python-clearsilver >= 0.9.3
#Requires: subversion-python >= 1.0.0

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
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >trac.httpd
###
### Sample Trac configuration taken from http://trac.edgewall.org/wiki/TracModPython
###

### The recommended Trac web interface requires mod_python
<IfModule mod_python.c>

### Create your Trac environments as subdirectories of %{_localstatedir}/trac
### They will appear in a listing on your website at /trac/, and be available 
### at /trac/PROJECTNAME/
<Location /trac>
  SetHandler mod_python
  PythonInterpreter main_interpreter
  PythonHandler trac.web.modpython_frontend 
  PythonOption TracEnvParentDir %{_localstatedir}/www/trac
  PythonOption TracUriRoot /trac
</Location>

### Use htpasswd to add Trac accounts to the AuthUserFile
<LocationMatch "/trac/[^/]+/login">
  AuthType Basic
  AuthName "Trac"
  AuthUserFile %{_localstatedir}/www/trac/.htpasswd
  Require valid-user
</LocationMatch>

</IfModule>
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --single-version-externally-managed --optimize="1" --root="%{buildroot}"

%{__install} -Dp -m0644 trac.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/trac.conf
%{__install} -d -m0755 %{buildroot}/%{_localstatedir}/www/trac

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README THANKS UPGRADE contrib/ doc/
%dir %{_sysconfdir}/httpd/
%dir %{_sysconfdir}/httpd/conf.d/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/trac.conf
%{_bindir}/trac*
%dir %{_localstatedir}/www/
%{_localstatedir}/www/trac/
%{python_sitelib}/trac/
%{python_sitelib}/Trac-%{version}-py*.egg-info/

%changelog
* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 0.11.2.1-1
- Updated to release 0.11.2.1.

* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 0.11.2-1
- Updated to release 0.11.2.

* Wed Aug 06 2008 Brandon Davidson <brandond@uoregon.edu> - 0.11.1-1
- Updated to release 0.11.1.
- Added egg.info files required for versioned autoloading by setuptools.
- Added %{_localstatedir}/www/trac to prevent sample apache config from
  erroring due to missing ParentDir

* Wed Jul 30 2008 Brandon Davidson <brandond@uoregon.edu> - 0.11-1
- Updated to release 0.11.
- Now requires/uses python-setuptools.
- New upstream no longer includes shared static content, so this release also
  drops the sample apache config, as it is invalid without any static content.

* Fri Apr 27 2007 Dag Wieers <dag@wieers.com> - 0.10.4-1
- Updated to release 0.10.4.

* Sat Mar 10 2007 Dag Wieers <dag@wieers.com> - 0.10.3.1-1
- Updated to release 0.10.3.1.

* Wed Dec 13 2006 Dag Wieers <dag@wieers.com> - 0.10.3-1
- Updated to release 0.10.3.

* Wed Nov 15 2006 Dag Wieers <dag@wieers.com> - 0.10.2-1
- Updated to release 0.10.2.

* Thu Nov 09 2006 Dag Wieers <dag@wieers.com> - 0.10.1-1
- Updated to release 0.10.1.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Sat Feb 18 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Tue Jul 19 2005 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Mon Jul 11 2005 Matt Whiteley <mattw@cat.pdx.edu> - 0.8.3-1
- Updated to release 0.8.3.

* Wed Jun 01 2005 Matt Whiteley <mattw@cat.pdx.edu> - 0.8.2-1
- Updated to release 0.8.2.
- Fixed env in apache conf.d file.

* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.8-4
- Fixed typo causing missing trac.conf. (Simon Perreault)

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.8-3
- Fixed buildroot in %%install phase. (Dimiter Manevski)

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.8-2
- Remove the deprecated subversion-python requirement. (Dimiter Manevski)

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Fri Jun 04 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Initial package. (using DAR)
